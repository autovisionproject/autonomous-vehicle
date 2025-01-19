import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

class LatentDiffusionModel(nn.Module):
    def __init__(self, latent_dim, num_timesteps, lr, weight_decay, checkpoint_dir, device):
        super(LatentDiffusionModel, self).__init__()
        self.latent_dim = latent_dim
        self.num_timesteps = num_timesteps
        self.device = device
        self.checkpoint_file = f"{checkpoint_dir}/weights/LatentDiffusionModel_network.pt"
        self.checkpoint_optimizer = f"{checkpoint_dir}/weights/optimizers/LatentDiffusionModel_network.pt"

        # Beta schedule for forward diffusion
        self.beta_schedule = torch.linspace(0.0001, 0.02, num_timesteps, device=device)
        self.alpha = 1.0 - self.beta_schedule
        self.alpha_cumprod = torch.cumprod(self.alpha, dim=0).to(device)

        self.epsilon_predictor = nn.Sequential(
            nn.Linear(latent_dim, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, latent_dim)
        ).to(device)

        self.optimizer = optim.Adam(self.parameters(), lr=lr, weight_decay=weight_decay)
        self.scheduler = optim.lr_scheduler.ReduceLROnPlateau(self.optimizer, 'min', factor=0.3, patience=8)
    def forward(self, h_t, timestep):
        if isinstance(timestep, int):
            timestep = torch.tensor(timestep, dtype=torch.long, device=self.device)

        timestep = torch.clamp(timestep, 0, self.num_timesteps - 1)
        beta_t = self.beta_schedule[timestep]
        alpha_t = 1.0 - beta_t
        alpha_cumprod_t = self.alpha_cumprod[timestep]
        # Forward diffusion: Add noise to h_t
        noise = torch.randn_like(h_t, requires_grad=False)  # Standard normal noise
        h_t_noisy = torch.sqrt(alpha_cumprod_t) * h_t + torch.sqrt(1 - alpha_cumprod_t) * noise
        # Reverse diffusion: Predict the noise
        epsilon_pred = self.epsilon_predictor(h_t_noisy)
        h_t_pred = (h_t_noisy - torch.sqrt(1 - alpha_t) * epsilon_pred) / torch.sqrt(alpha_t)

        return h_t_pred, noise,epsilon_pred

    def compute_diffusion_loss(self,predicted_epsilon, epsilon):
        loss = F.mse_loss(predicted_epsilon, epsilon)
        return loss

    def save_checkpoint(self):
        torch.save(self.state_dict(), self.checkpoint_file)
        torch.save(self.optimizer.state_dict(), self.checkpoint_optimizer)

    def load_checkpoint(self):
        self.load_state_dict(torch.load(self.checkpoint_file, map_location=self.device))
        self.optimizer.load_state_dict(torch.load(self.checkpoint_optimizer, map_location=self.device))

