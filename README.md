# Qrobo
### 运行
#### 1. 启动仿真
```bash
source devel/setup.bash
roslaunch src/sim.launch 
```
#### 2. 启动机器人
先等待 Gazebo 完全启动，显示仿真世界画面后，再启动机器人，否则容易出错
```bash
source devel/setup.bash
roslaunch src/bringup.launch
```
#### 3. 启动控制节点
```bash
source devel/setup.bash
roslaunch qrobo_sim teleop_key.launch 
```
启动后，选中该终端，切换至英文输入法，根据提示使用相应按键控制机器人运动

---
### 配置
#### 仿真世界
`src/sim.launch` 文件中，注释为“参数”的变量。

`~/gazebo_models_worlds_collection/worlds` 中提供了很多设计好的仿真世界文件。
#### 机器人运行模式
`src/bringup.launch` 文件中，注释为“参数”的变量。
