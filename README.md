## Beyond the Map: Learning to Navigate Unseen Urban Dynamics Using Diffusion-Guided Deep Reinforcement Learning
<img src="results/time.png" alt="Time 1" width="900px">
<p style="font-size: 14px; font-weight: normal; text-align: center;"> Sequential observations at different intervals show minimal changes in subsequent scenes and nearly identical actions between closely spaced frames. This indicates that minor variations in observations do not significantly influence vehicle behavior. Such stability is crucial, as it provides a robust foundation for developing a generalized solution capable of effectively addressing environmental uncertainties.</p>

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

## Test Scenarios
The table below lists the YAML configuration files used for testing various scenarios. 
Source dir: config/experiments/dgdrl

| **Dense Tests**                   | **Regular Tests**                  | **Empty Tests**                  |
|-----------------------------------|-------------------------------------|----------------------------------|
| test-dense_t03_wnew.yaml          | test-regular_t01_wtrain.yaml       | test-empty_t01_wnew.yaml        |
| test-dense_t04_wnew.yaml          | test-regular_t02_wnew.yaml         | test-empty_t01_wtrain.yaml      |
| test-dense_t05_wnew.yaml          | test-regular_t02_wtrain.yaml       | test-empty_t02_wnew.yaml        |
| test-dense_t01_wtrain.yaml        | test-regular_t03_wnew.yaml         | test-empty_t02_wtrain.yaml      |
| test-dense_t01_wnew.yaml          | test-regular_t04_wnew.yaml         | test-empty_t03_wnew.yaml        |
| test-dense_t02_wnew.yaml          | test-regular_t05_wnew.yaml         | test-empty_t03_wtrain.yaml      |
| test-dense_t02_wtrain.yaml        | test-regular_t03_wtrain.yaml       | test-empty_t04_wnew.yaml        |
| test-dense_t03_wtrain.yaml        | test-regular_t04_wtrain.yaml       | test-empty_t04_wtrain.yaml      |
| test-dense_t04_wtrain.yaml        | test-regular_t05_wtrain.yaml       | test-empty_t05_wnew.yaml        |

## Results

a) **Model Comparision**  

<img src="results/Result.PNG" alt="Model Comparision" width="650px">

b) **Safety measures during unexpected events.**  

<img src="results/safty.png" alt="Safety measures during unexpected events" width="650px">

c) **Model’s ability to generalize beyond its training environment**  

<img src="results/lanechange.png" alt="Model’s ability to generalize beyond its training environment" width="650px">

d) **Exploring Unseen States: Success and Failures**  
<img src="results/tunnels.png" alt="Exploring Unseen States: Success and Failures" width="650px">

e) **Handling traffic lights**  
<img src="results/redlight.png" alt="Handling traffic lights" width="650px">


## 🙏 Acknowledgement
This repo is built upon the following projects:

1. [rlfold](https://github.com/DanielCoelho112/rlfold)  
2. [carla-roach](https://github.com/zhejz/carla-roach)
