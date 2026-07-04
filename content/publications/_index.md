---
title: Publications
date: 2026-06-27
summary: Publications in autonomous vehicles, model predictive control, fuzzy-PID control, and autonomous mining trucks.
---

My publications focus on control algorithms for autonomous vehicles and mining trucks, especially under tracking accuracy, payload variation, vehicle dynamics, and robustness constraints.

## Journal

**Qin T**, Zhu D, Wang C, Yang P, Yang K. *Dual-Loop Fuzzy-PID Acceleration Tracking Controller for Autonomous Mining Trucks under Variable Payload Conditions*. **Coal Engineering**, accepted.

- **Problem:** Longitudinal acceleration tracking becomes unstable when autonomous mining trucks operate under variable payload conditions.
- **Method:** Dual-loop fuzzy-PID controller with self-adaptive compensation.
- **Result:** Maximum speed error of 0.49 km/h and maximum acceleration error of 0.103 m/s^2; peak-to-peak speed and acceleration errors improved by 8.77% and 13.30% compared with MPC.
- **My contribution:** First-author work on variable-payload longitudinal control, including controller design, experiment analysis, and paper preparation.

## Conference

**Qin T**, Qiu L, Chen J, Fu H, Zhu D, Yang K. *Double-Layer Following Controller for Autonomous Vehicles*. **36th Chinese Control and Decision Conference (CCDC)**, IEEE, 2024, pp. 908-913.

- **Problem:** Following control needs to balance tracking accuracy and comfort in autonomous driving scenarios.
- **Method:** Dynamic Window Approach combined with a fuzzy-adaptive PID controller.
- **Result:** Lateral and longitudinal acceleration RMS improved by 19.5% and 37.3% compared with PID-Stanley.
- **My contribution:** First-author two-layer following controller in ROS/VTD, including controller development, simulation evaluation, and manuscript writing.

Wang C, Zhu D, **Qin T**, et al. *Lateral Trajectory Tracking of Autonomous Mining Trucks Using MPC with Adaptive Load Compensation*. **CCC 2025**, IEEE.

- **Problem:** Lateral tracking performance degrades under large payload variation in mining truck operation.
- **Method:** MPC with adaptive load compensation for trajectory tracking.
- **Result:** Full-load lateral mean absolute error was reduced by 33.33% compared with LQR.
- **My contribution:** Mining-truck control context and experiment support for load-adaptive MPC in Simulink/TruckSim.

Yang P, Zhu D, **Qin T**, et al. *Adaptive Heading Tracking Algorithm Based on Vehicle Dynamics Model*. **CCC 2025**, IEEE.

- **Problem:** Pure pursuit tracking can lose precision when vehicle dynamics and heading response are not adequately modeled.
- **Method:** Heading-corrected pure pursuit using a vehicle dynamics model.
- **Result:** Average lateral error decreased from 0.462 m to 0.237 m in TruckSim/Simulink validation.
- **My contribution:** Vehicle-dynamics control context and manuscript support.
