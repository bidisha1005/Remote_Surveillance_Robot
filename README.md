```markdown
# 🤖 Remote Surveillance Robot (ROS 2 + Gazebo)

## 📌 Overview
This project implements a **Remote Surveillance Robot** using **ROS 2 (Humble)** and **Gazebo simulation**. The robot is a differential-drive mobile platform equipped with a camera sensor to enable real-time monitoring in a simulated environment.

The system addresses the limitations of fixed surveillance systems by providing a **mobile, adaptable, and remotely controlled solution** for monitoring hazardous or large-scale environments.

---

## 🎯 Objectives

- Design and simulate a mobile surveillance robot  
- Enable real-time camera streaming  
- Implement teleoperation using ROS 2 topics (`/cmd_vel`)  
- Deploy the robot in a realistic Gazebo environment with obstacles  

---

## 🚀 Features

- 🛞 Differential drive robot (2-wheel locomotion)  
- 🎮 Teleoperation using keyboard input  
- 📷 Live camera feed publishing (`/camera/image_raw`)  
- 📍 Odometry tracking (`/odom`)  
- 🌍 Custom Gazebo world with obstacles  
- 🔁 ROS 2 publisher-subscriber communication  
- 🔗 TF tree broadcasting for robot state  

---

## 🏗️ System Architecture

### 🔹 Control Flow
```

User Input (Keyboard)
↓
teleop_twist_keyboard
↓
/cmd_vel topic
↓
Gazebo Diff Drive Plugin
↓
Robot Movement
↓
Odometry (/odom) + TF Broadcast

```

### 📷 Camera Pipeline
```

Gazebo Rendering
↓
Camera Sensor Plugin
↓
sensor_msgs/Image
↓
/camera/image_raw
↓
Visualization (image_tools)

```

---

## ⚙️ Tech Stack

### 🧠 Software
- ROS 2 Humble  
- Gazebo Classic  
- Python 3  
- URDF (Robot Description)  
- Xacro (URDF Macros)  
- SDF (Simulation Environment)  

### 🛠️ Libraries & Tools
- gazebo_ros_diff_drive  
- gazebo_ros_camera  
- robot_state_publisher  
- teleop_twist_keyboard  
- image_tools  
- colcon (build system)  

---

## 🧮 Core Algorithm

### Differential Drive Kinematics
```

v_left  = v - (ω × d / 2)
v_right = v + (ω × d / 2)

```

Where:  
- `v` = linear velocity  
- `ω` = angular velocity  
- `d` = wheel separation  

---

## 🧪 Simulation Environment

- 📐 Area: 10m × 10m  
- 🧱 4 boundary walls (2m height)  
- 📦 Static obstacles (wood cubes)  
- ⚙️ Physics-enabled simulation  

---

## ▶️ How to Run

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/bidisha1005/Remote_Surveillance_Robot.git
cd ~/Remote_Surveillance_Robot
````

### 2️⃣ Build the Workspace

```bash
colcon build
source install/setup.bash
```

### 3️⃣ Launch Simulation

```bash
ros2 launch surveillance_robot_description robot_launch.py
```

### 4️⃣ Teleoperate Robot

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

### 5️⃣ View Camera Feed

```bash
ros2 run image_tools showimage
```

---

## 📊 Results

* Robot successfully spawned in Gazebo
* Smooth teleoperation using keyboard
* Real-time camera feed streaming
* Proper ROS topic communication
* TF tree and odometry functioning correctly

---

## 📚 Key Learnings

* ROS 2 publisher-subscriber architecture
* URDF/Xacro robot modeling
* Gazebo simulation and plugin integration
* Differential drive kinematics
* Sensor data streaming via ROS topics

---

## 🔮 Future Work

* Autonomous navigation (SLAM + Nav2)
* Object detection using computer vision
* Multi-robot coordination
* Real-world hardware deployment

---

## 📄 License

This project is for academic and educational purposes.

---

```
