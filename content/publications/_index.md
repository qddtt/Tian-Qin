---
title: Publications
date: 2026-06-27
summary: Publications in autonomous vehicles, model predictive control, adaptive/fuzzy PID control, and autonomous mining trucks.
---

My publications focus on control algorithms for autonomous vehicles and mining trucks, especially under tracking accuracy, payload variation, vehicle dynamics, obstacle interaction, and robustness constraints.

## Journal

**Qin T**, Zhu D, Wang C, Yang P, Yang K. *Dual-Loop Fuzzy-PID Acceleration Tracking Controller for Autonomous Mining Trucks under Variable Payload Conditions*. **Coal Engineering**, 2025, 57(6): 172-179. DOI: [10.11799/ce202506022](https://doi.org/10.11799/ce202506022).

- **Problem:** Longitudinal dynamics change substantially between empty and full-load autonomous mining-truck operation.
- **Method:** Dual-loop fuzzy-PID acceleration tracking controller with an outer speed-tracking loop, an inner acceleration-control loop, and online PID adjustment according to payload state.
- **Result:** Stable speed and acceleration tracking under variable-payload conditions, with a maximum speed error of 0.49 km/h and a maximum acceleration error of 0.103 m/s<sup>2</sup>.
- **My contribution:** First-author work on variable-payload longitudinal control, including controller design, simulation analysis, and paper preparation.

## Conference

**Qin T**, Qiu L, Chen J, Fu H, Zhu D, Yang K. *Double-Layer Following Controller for Autonomous Vehicles*. **2024 36th Chinese Control and Decision Conference (CCDC)**, IEEE, 2024, pp. 908-913. DOI: [10.1109/CCDC62350.2024.10587700](https://doi.org/10.1109/CCDC62350.2024.10587700).

- **Problem:** Autonomous following needs to handle high-speed overtaking, sharp turns, and dynamic obstacle avoidance while maintaining safe distance and smoothness.
- **Method:** Two-layer following-control framework combining DWA local planning with fuzzy-adaptive PID.
- **Result:** The upper layer plans a safe local path from lane markings and target-vehicle information, while the lower layer adapts PID parameters online for lateral/longitudinal tracking.
- **My contribution:** First-author controller design, ROS/VTD simulation evaluation, and manuscript writing.

Wang C, Zhu D, **Qin T**, Yang K. *Lateral Trajectory Tracking of Autonomous Mining Trucks Using MPC with Adaptive Load Compensation*. **2025 44th Chinese Control Conference (CCC)**, IEEE, 2025. DOI: [10.23919/CCC64809.2025.11178743](https://doi.org/10.23919/CCC64809.2025.11178743).

- **Problem:** Lateral trajectory tracking accuracy degrades on complex open-pit mine roads under payload variation.
- **Method:** MPC strategy with adaptive load compensation and real-time vehicle-parameter updates for empty/full-load states.
- **Result:** The controller optimizes control outputs to reduce the effect of payload fluctuation on prediction and trajectory tracking.
- **My contribution:** Mining-truck control context, experiment support, and validation discussion for load-adaptive MPC.

Yang P, Zhu D, **Qin T**, Yang K. *Adaptive Heading Tracking Algorithm Based on Vehicle Dynamics Model*. **2025 44th Chinese Control Conference (CCC)**, IEEE, 2025. DOI: [10.23919/CCC64809.2025.11179654](https://doi.org/10.23919/CCC64809.2025.11179654).

- **Problem:** Pure pursuit makes limited use of target-path heading information and can lose tracking accuracy on complex mine roads.
- **Method:** Improved pure-pursuit algorithm with vehicle-dynamics feedback and heading correction.
- **Result:** Average lateral error decreased from 0.462 m to 0.237 m in TruckSim/Simulink validation.
- **My contribution:** Vehicle-dynamics control context and manuscript support.

## Thesis

**Qin T.** *Trajectory Tracking Control of Unmanned Mining Trucks in Open-Pit Mines*. M.S. thesis, China University of Mining and Technology, Beijing, 2025. Supervisor: Prof. Kehu Yang.

- **Problem:** Open-pit autonomous mining trucks must track trajectories on unstructured mine roads under large payload variations and strict safety constraints, which makes coupled lateral and longitudinal control difficult.
- **Method:** Designed an MPC path-tracking controller based on a four-degree-of-freedom kinematic model, with an ADRC acceleration tracking controller at the lower layer, integrated into a dual-layer tracking architecture.
- **Result:** Full-condition simulations on typical mine paths show improved trajectory tracking accuracy, faster disturbance rejection, and stronger robustness under variable payload; the four-degree-of-freedom kinematic MPC achieves a better balance between tracking accuracy and computational efficiency.
- **Related publications:** Chapters 2–4 correspond to the CCDC 2024 following-control paper, the two CCC 2025 papers listed above, and the *Coal Engineering* journal paper.
