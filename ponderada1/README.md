## Instalação

```bash
# Clone o repositório
git clone https://github.com/VZeferino/ponderada1.git

# Construa o projeto
colcon build
source install/local_setup.bash #ou zsh
```
## Teste

```bash
#Inicie o gazebo
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

```bash
#Inicie o rviz
 ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:=map.yaml 
```

[Assista ao Vídeo de Demonstração](https://youtu.be/ewbGKju4fxE)

# Para executar o launch file

```bash
ros2 launch ponderada launch_file_name.launch.py
```
