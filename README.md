# Surveillance Robot (ROS2)

## Setup

```bash
git clone https://github.com/bidisha1005/Remote_Surveillance_Robot.git
cd surveillance_robot_ws

# Install dependencies
rosdep install --from-paths src --ignore-src -r -y

# Build workspace
colcon build

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
ros2 launch surveillance_robot_description gazebo.launch.py
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
