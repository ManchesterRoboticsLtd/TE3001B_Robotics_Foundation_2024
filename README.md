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
TBD

 
## General Requirements
General requirements. Please be aware that a set of requirements especific for each session will be shown in each session subsection (Some items may be repeated).
* Computer with access to Zoom (online classes).
* Computer with Ubuntu 22.04 and ROS Humble or MCR2 virtual machine.
* Knowledge of Windows. 
* Basic knowledge of Ubuntu (recommended).
* Basic understanding of robotics (recommended).
* Access to the following materials
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
  
  **Mini challenge:** Generate a node that send a signal to another node to process it.
  
  **Requirements:** Computer with access to Zoom, Ubuntu 22.04 and ROS Melodic Installed (Full installation). In case Ubuntu 22.04 cannot be installed, MCR2 offers a Virtual Machine with ROS preinstalled (installation instructions in Week 1 Folder).
  
  ### Week 2: (ROS Practicalities)  
  This week will introduce some useful ROS practicalities.
  * ROS Namespaces
  * ROS Parameters
  * Activity 1: Parametrise previous nodes
  * ROS Custom Messages
  * Q&A
  
  **Mini challenge:**: P/PI Controller from scratch to a 1st order simulated system.
  
  **Requirements:** Requirements of Session 1.

  ### Week 3: ROS-Hardware Communication
  This week will introduce hardware communication between ROS and the Hackerboard using ROSSerial.
  * Micro ROS
  * Data acquisition
  * ESP32
  * Encoder Basic Theory
  * Q&A Session.
  
  **Requirements:** Requirements of Session 1, Installation of the Arduino IDE and the micro ROS package in the VM or Ubuntu. Access to the requested electric and electronic hardware.
  
  ### Week 4: ROS Data Acquisition
  This week will introduce how to acquire data between ROS and the Hackerboard using ROSserial.
  
  **Mini challenge:** Acquire data from the encoders using Arduino.
  **Final Challenge:** PID Controller using ROS and compare with simulation.
  * Q&A Session.
  
  **Requirements:** Requirements of Session 1 and Session 3.
  
  ### Week 5: Final Challenge
  Final Challenge presentation week.
  
  **Final Challenge:**: PID Controller using ROS
  
  **Requirements:** Requirements of Session 1 and Session 3.

