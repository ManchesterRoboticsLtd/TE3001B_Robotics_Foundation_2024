<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/ManchesterRoboticsLtd/TE3001B_Fundamentals_of_Robotics/blob/main/Misc/Logos/Logotipo%20Vertical%20Bco_Transparente.png">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/ManchesterRoboticsLtd/TE3001B_Fundamentals_of_Robotics/blob/main/Misc/Logos/Logotipo%20Vertical%20Azul%20transparente.png">
  <img alt="Shows ITESM logo in black or white." width="160" align="right">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/ManchesterRoboticsLtd/TE3001B_Fundamentals_of_Robotics/blob/main/Misc/Logos/MCR2_Logo_White.png">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/ManchesterRoboticsLtd/TE3001B_Fundamentals_of_Robotics/blob/main/Misc/Logos/MCR2_Logo_Black.png">
  <img alt="Shows MCR2 logo in black or white." width="150" align="right">
</picture>

---
# TE3001B: Robotics Foundation

  ## Introduction
   * This course, developed by Manchester Robotics ltd. (MCR2), introduces the basic concepts and general knowledge of the ROS environment to the user.
   * The course is divided into five session, carefully designed for the user to learn about the different aspects of ROS  from topics and messages to control and simulation using ROS.
   * This course will be based on challenges to make the student aware of ROS basics and ROS communication with hardware.
   * This branch contains all the presentations, activities and files required for the “TE3001B: Fundamentación de Robótica” course of the Tec de Monterrey.
   * This repository is organised by sessions, each subfolder contains all the neccesary files for each one of the activities of this course.
   
## General Information
* Duration 5 Weeks
* Classes: Thursdays  (1 – 3 PM) / 5 Weeks
* Starts: 15 February.
* Ends: 14 March
* ZOOM Link Classes: https://itesm.zoom.us/j/4779422764

## Live Sessions (Recordings)
https://drive.google.com/drive/folders/1q1FLw9df18JEB5NbzqEM48_30Une512R?usp=drive_link

 
## General Requirements
General requirements. Please be aware that a set of requirements especific for each session will be shown in each session subsection (Some items may be repeated).
* Computer with access to Zoom (online classes).
* Computer with Ubuntu 22.04 and ROS Humble or MCR2 virtual machine.
* Knowledge of Windows. 
* Basic knowledge of Ubuntu (recommended).
* Basic understanding of robotics (recommended).
* Access to the following materials
  * Arduino IDE
  * Webcam
  * ESP32 from ExpressIf
  * H-Bridge (L298 or similar)
  * DC Motor with encoder
  * Breadboard
  * LEDs
  * 220 o 330 Ohm Resistors
  * 1k to 10k potentiometer

## Weekly Sessions

  ### Week 1: (Intorduction)
  This week will introduce the teaching team and the basics of ROS.
  * Who we are? Introduction to MCR2.
  * Introduction to Robotics
  * Introduction to VM, Ubuntu
  * Introduction to ROS
  * Overview of the ROS Environment: Topics, messages, ROS.
  * Activity 1 (Talker and Listener)
  * Launch files
  *	Activity 2: Launch Files
  * Q&A
  
  **Mini challenge:** Generate a node that send a signal to another node to process it. The mini challenge and further instructions for this session is located in the folder Challenge.
  
  **Requirements:** Computer with access to Zoom, Ubuntu 22.04 and ROS Melodic Installed (Full installation). In case Ubuntu 22.04 cannot be installed, MCR2 offers a Virtual Machine with ROS preinstalled (installation instructions in Week 1 Folder).
  
  ### Week 2: (ROS Practicalities)  
  This week will introduce some useful ROS practicalities.
  * ROS Namespaces
  * ROS Parameters
  * Activity 1: Parametrise previous nodes
  * ROS Custom Messages
  * Q&A
  
  **Mini challenge:**: Create a Simple P or PI controller for a simulated first order process.
  
  **Requirements:** Requirements of Session 1.

  ### Week 3: ROS-Hardware Communication and Data acquisition
  This week is intended for the students to learn how to connect ROS with external hardware using micro-ROS tools that will be required in the following sessions.
  * Micro ROS
  * Data acquisition
  * ESP32
  * Encoder Basic Theory
  * Q&A Session.
  
  **Requirements:** Requirements of Session 1, Installation of the Arduino IDE and the micro ROS package in the VM or Ubuntu. Access to the requested electric and electronic hardware.
  **Mini challenge:** GPIO and analog input, PWM.
  
  ### Week 4: ROS Data Acquisition + Control
  This session is intended for the students to learn how to control external hardware using micro-ROS tools that will be required in the final challenge.
  
  **Final Challenge:** Control in open loop the speed and direction of a motor using a MCU, controlled from a computer using rosserial..
  * Q&A Session.
  
  **Requirements:** Requirements of Session 1 and Session 3.
  
  ### Week 5: Final Challenge
  Final Challenge presentation week.
  
  **Final Challenge:**: PID Controller using ROS
  
  **Requirements:** Requirements of Session 1 and Session 3.

  ### Useful Links: 
  #### Ubuntu
   * [Ubuntu Installation](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview)
  
  #### ROS
   * [ROS Installation](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html)
   * [ROS book](https://github.com/fmrico/book_ros2)
   * [ROS Packages](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package.html)
   * [ROS Workspace](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html)
   * [ROS Nodes](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes.html)
   * [Topics](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics.html)
   * [Publisher and Subscribers](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html)
   * [ROS Launch](https://docs.ros.org/en/humble/How-To-Guides/Launch-file-different-formats.html)
   * [ROS Custom Interfaces](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Custom-ROS2-Interfaces.html)
   * [Parameters](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Using-Parameters-In-A-Class-Python.html)

  #### Embedded Systems
   * [micro-ROS](https://micro.ros.org/)
   * [micro-ROS-Arduino](https://github.com/micro-ROS/micro_ros_arduino)
   * [DC Motor](https://en.wikipedia.org/wiki/DC_motor)
   * [H-Bridge](https://www.youtube.com/watch?v=fVgnUWIWzZ8&ab_channel=NorthwesternRobotics)
   * [Rotary Encoder](https://en.wikipedia.org/wiki/Rotary_encoder)
   * [Rotary Encoder](https://www.encoder.com/article-what-is-an-encoder)
  
  #### Virtual Machine: 
   * [VM Ware](https://customerconnect.vmware.com/en/downloads/details?downloadGroup=WKST-PLAYER-1750&productId=1377&rPId=111473)
   * [ROS Preinstalled VM](https://manchesterrobotics-my.sharepoint.com/:u:/g/personal/mario_mtz_manchester-robotics_com/EWcRInLzqDZNpxqWlH3X0sQBGXgbTSj9Qp1VX7O_sGy4zQ?e=sIq2xd)

  #### Resources
   * [Introduction to Autonomous Mobile Robots](https://ieeexplore.ieee.org/book/6267528)
   * [PID Control](https://ieeexplore.ieee.org/document/1453566)
   * [Closed Loop Control](https://www.electronics-tutorials.ws/systems/closed-loop-system.html)
   * [Nonlineraities and robustness](https://ieeexplore.ieee.org/document/8603065)
   * [Open loop control Tutorial](https://www.electronics-tutorials.ws/systems/open-loop-system.html)
   * [Open Loop Control Tutorial](https://www.electronicshub.org/open-loop-system/)
   * [Open Loop Control Book](https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Signal_Processing_and_Modeling/Introduction_to_Linear_Time-Invariant_Dynamic_Systems_for_Students_of_Engineering_(Hallauer)/14%3A_Introduction_to_Feedback_Control/14.02%3A_Definitions_and_Examples_of_Open-Loop_Control_Systems)
     
   ---
  
