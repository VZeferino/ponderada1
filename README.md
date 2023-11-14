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


# Para executar o launch file de mapeamento 

```bash
ros2 launch ponderada map_launch.py
```

Esse launch abre o gazebo, o teleop e também o rviz, basta você mapear o ambiente e depois salvar o mapa usando o comando:
```bash
ros2 run nav2_map_server map_saver_cli -f <nome-do-mapa>
```
[Mapeamento](https://youtu.be/vVFTszQk8FM).

# Para executar o launch file de navegação
```bash
ros2 launch ponderada navigation_launch.py
```
Com esse launch o robô vai procurar o melhor caminho utilizando o alvo dado no nó go_to_pose
[Navegação](https://youtu.be/WqxoV84tRCY)
