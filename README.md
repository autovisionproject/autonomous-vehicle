# Towards Generalized and Safer Urban Autonomous Navigation Using Diffusion-Enhanced Deep Reinforcement Learning
<img src="results/time.png" alt="Time 1" width="900px">
<p style="font-size: 14px; font-weight: normal; text-align: center;">	Sequential observations at different intervals show minimal change in subsequent scenes and nearly identical actions between closely spaced frames. This indicates that minor variations in observations do not significantly impact vehicle behavior. Such stability is crucial as it provides a better approach for the development of a more generalized solution to handle dynamic environmental uncertainties.</p>

# <h3 style="font-size: 16px; font-weight: normal;">Abstract</h3>
Vision-based motion planning is a crucial task in Autonomous Driving (AD). Recent progress in urban AD has shown that integrating Imitation Learning (IL) with Deep Reinforcement Learning (DRL) improves decision-making to be more like humans. However, IL methods depend on expert demonstrations to learn the best policies. The main drawback of this approach is its assumption that expert demonstrations are always optimal, which is not always the case in real-world environments. This leads to challenges adapting to dynamic weather conditions (e.g., rain, mirages, and lightning) and varying traffic scenarios, sometimes resulting in increased collision rates and heightened pedestrian safety concerns. To address these challenges, we propose an advanced approach named Diffusion-Guided Deep Reinforcement Learning (DGDRL), which integrates a diffusion model to handle environmental uncertainty with a Soft Actor-Critic DRL framework. The diffusion process generates a broader distribution of observations that extends beyond the original demonstrations and ensures that the learned action behavior remains consistent with the current actions. We utilize the CARLA NoCrash benchmark simulation platform to collect data and evaluate the proposed framework. The proposed method is trained on an NVIDIA L40S GPU and validated in simulated urban environments, which include scenarios with empty, regular, and dense traffic conditions across different town settings. Additionally, we have evaluated our model against several state-of-the-art techniques to ensure its robustness in generalizing to new situations.

## <h3 style="font-size: 16px; font-weight: normal;">CARLA Installtion</h3>
* Download and install [CARLA 0.9.10.1](https://github.com/carla-simulator/carla/releases/tag/0.9.10.1) release with additional maps.
```
Intall Ubuntu 20.04.6
mkdir -p /home/ubuntu/carla
cd /home/ubuntu/carla
tar -xvzf CARLA_0.9.11.tar.gz
echo "export CARLA_ROOT=/home/ubuntu/carla" >> /home/ubuntu/.bashrc
cd Import, Download AdditionalMaps file.
cd ../; bash ImportAssets.sh
source /home/ubuntu/.bashrc
cd /home/ubuntu/ & place DGDRL files in ubuntu dir.
unzip carla_env.zip file
Install all python3.8 packages as per requirements.txt file.
```

* Run DGDRL
```
Start the CARLA server
cd /home/ubuntu/carla & ./CarlaUE4.sh --port=2000
cd ../ 

Training Model:
#python main.py -en dgdrl -vm

Testing Model:
date; for i in $(ls  /<home-dir>/config/experiments/dgdrl/|grep -i test );do echo $i;python main.py -en dgdrl -vm -ttc $i -ow;done;date
```

## Results
a) **Safety measures during unexpected events.**  

<img src="results/safty.png" alt="Safety measures during unexpected events" width="750px">

b) **Model’s ability to generalize beyond its training environment**  

<img src="results/lanechange.png" alt="Model’s ability to generalize beyond its training environment" width="750px">

c) **Exploring Unseen States: Success and Failures**  
<img src="results/tunnels.png" alt="Exploring Unseen States: Success and Failures" width="750px">

d) **Handling traffic lights**  
<img src="results/redlight.png" alt="Handling traffic lights" width="750px">


# Credits
