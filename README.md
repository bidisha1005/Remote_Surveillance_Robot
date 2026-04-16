# Surveillance Robot (ROS2)

## Setup

```bash
git clone https://github.com/bidisha1005/Remote_Surveillance_Robot.git
cd ~/Remote_Surveillance_Robot
colcon build --symlink-install

# Source workspace
source install/setup.bash
```

---

## Run Robot

### ▶️ RViz (Visualization)

```bash
ros2 launch surveillance_robot_description display.launch.py
```

---

### 🌍 Gazebo (Simulation)

```bash
source ~/Remote_Surveillance_Robot/install/setup.bash
ros2 launch surveillance_robot_description robot_launch.py
```

---

## Notes

* If ROS2 is not sourced:

```bash
source /opt/ros/humble/setup.bash
```

* If build fails:

```bash
colcon build --symlink-install
```
