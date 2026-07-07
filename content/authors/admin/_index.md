---
title: Qin Tian

first_name: Tian
last_name: Qin

superuser: true

role: Control Algorithm Engineer

organizations:
  - name: China University of Mining and Technology, Beijing
    url: https://www.cumtb.edu.cn/
  - name: Intelligent Energy Systems and Autonomous Mining Laboratory
    url: ''

bio: I work on control and autonomy for heavy-duty vehicles, with a foundation in MPC, LQR, adaptive/fuzzy PID, vehicle dynamics modeling, parameter identification, trajectory tracking, and field-deployed autonomous mining-truck systems. My PhD direction is data-driven and reinforcement-learning-based control for safety-critical autonomous systems.

profiles:
  - icon: at-symbol
    url: 'mailto:qintian0142@163.com'
    label: Email
  - icon: brands/github
    url: https://github.com/qddtt
    label: GitHub

education:
  - area: M.S. in Control Science and Engineering
    institution: China University of Mining and Technology, Beijing (211)
    date_start: 2023-09-01
    date_end: 2025-09-01
    summary: |
      - GPA: 3.59/4.0
      - Supervisor: Prof. Kehu Yang
      - Lab: Intelligent Energy Systems and Autonomous Mining Laboratory
      - Core coursework: Linear System Theory (96), Adaptive Control (94), Advanced Signal Processing (93)
      - Research focus: MPC, adaptive/fuzzy PID, vehicle dynamics modeling, parameter identification, and autonomous mining trucks

  - area: B.Eng. in Electronic Information Engineering
    institution: Sichuan University (985)
    date_start: 2015-09-01
    date_end: 2019-06-01
    summary: |
      - Core coursework: C Programming (91), Computer Communication and Networks (86), Communication Principles Laboratory (88), Analog Electronics, Signals and Systems

work:
  - position: Control Algorithm Engineer
    company_name: Mindway Science and Technology Co., Ltd.
    company_url: ''
    company_logo: ''
    date_start: 2025-10-01
    date_end: ''
    summary: |
      - Developed and deployed lateral/longitudinal control code for autonomous mining trucks, including LQR lateral control and dual-loop PID longitudinal control for path tracking, speed tracking, and braking
      - Independently implemented AEB anti-collision logic using time-domain trajectory prediction and OBB detection for safety-critical mine-road scenarios
      - Performed system identification from real-vehicle data for a two-degree-of-freedom vehicle dynamics model, supporting LQR tuning and vehicle validation

  - position: Hardware Engineer
    company_name: China Aerospace Science and Industry Corporation (CASIC)
    company_url: ''
    company_logo: ''
    date_start: 2019-07-01
    date_end: 2023-08-01
    summary: |
      - Participated in industrial-vehicle control-system calibration and on-site debugging, including engine-throttle calibration
      - Coordinated joint debugging among vehicle controllers, sensors, and actuators; adjusted control parameters and interface configurations to resolve response lag and communication anomalies
      - Supported on-site testing, data logging, and issue reproduction, feeding calibration results back into control-strategy and hardware-configuration iterations

skills:
  - name: Control and Autonomy
    items:
      - name: Model Predictive Control
        description: MPC design, trajectory tracking, constraint handling, and controller comparison
        percent: 90
        icon: devicon/python
      - name: Fuzzy-PID Control
        description: Adaptive control, dual-loop tracking, and robustness improvement
        percent: 85
        icon: devicon/python
      - name: ROS / C++
        description: Robot operating system and autonomous driving stack integration
        percent: 80
        icon: devicon/ros
      - name: MATLAB / Simulink
        description: Control simulation, vehicle dynamics modeling, and rapid prototyping
        percent: 80
        icon: devicon/matlab
      - name: Model Calibration
        description: Vehicle dynamics modeling, parameter identification, and real-vehicle data based tuning
        percent: 80
        icon: hero/adjustments-horizontal
      - name: Python
        description: Scientific computing, experiment analysis, and algorithm prototyping
        percent: 85
        icon: devicon/python
      - name: PyTorch
        description: Learning-based control and reinforcement learning foundations
        percent: 45
        icon: devicon/pytorch
  - name: Research Direction
    items:
      - name: Autonomous Mining Trucks
        description: Heavy-duty autonomy in open-pit and unstructured environments
        percent: 95
        icon: hero/truck
      - name: Field Robotics
        description: Robust autonomy under terrain, payload, obstacle, and safety constraints
        percent: 85
        icon: hero/cpu-chip
      - name: Learning-Based Control
        description: Data-driven and reinforcement learning methods for autonomous systems
        percent: 65
        icon: hero/academic-cap

languages:
  - name: Chinese
    percent: 100
  - name: English (IELTS 6.5; Reading 8.0)
    percent: 75

awards:
  - title: China Intelligent Connected Vehicle Challenge (CICV) 2023
    date: '2023-11-25'
    awarder: Chinese Association for Artificial Intelligence (CAAI)
    summary: |
      Contribution Award (Top 5%). For adaptive cruise and following tasks, used DWA for local path planning and fuzzy PID for speed/acceleration tracking; lateral and longitudinal acceleration RMS values were below 0.10 m/s<sup>2</sup> and 0.06 m/s<sup>2</sup>.
  - title: Autopilot Challenge of the Vehicle-Road-Cloud Integration 2024
    date: '2024-06-01'
    awarder: China Association of Automobile Manufacturers
    summary: |
      Innovation Award (Top 5%, ranked 7th among 118 teams). Integrated and tuned an LQR lateral controller on a real autonomous-driving platform for low-speed parking and obstacle-avoidance validation.
  - title: National Post-Graduate Mathematical Contest in Modeling
    date: '2024-09-21'
    awarder: China Academic Degrees and Graduate Education Development Center
    summary: |
      Participation Award (Top 20%). Fitted Steinmetz-equation parameters with nonlinear optimization, analyzed operating-condition variables, and improved magnetic-component loss model accuracy by 5%.
---

I am a control and autonomous-systems researcher with an M.S. in Control Science and Engineering from China University of Mining and Technology, Beijing. My research focuses on Model Predictive Control (MPC), adaptive/fuzzy PID, vehicle dynamics modeling, parameter identification, and trajectory tracking for autonomous mining trucks in unstructured open-pit environments.

Before and after graduate study, I have worked on deployment-facing control problems for autonomous mining trucks, from industrial-vehicle calibration and on-site joint debugging at CASIC to LQR/PID controller deployment, AEB anti-collision logic, and real-vehicle system identification at Mindway. That field experience shapes my research taste: I care about autonomy methods that remain reliable when payload, terrain, model mismatch, obstacles, and safety constraints interact in the real world.

For PhD study, I hope to extend this control foundation toward reinforcement learning, learning-based control, and data-driven methods for autonomous systems. My goal is to connect model-based reliability with adaptive learning methods for complex robotic and vehicle systems.
