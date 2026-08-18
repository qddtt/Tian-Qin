---
title: 论文
date: 2026-06-27
summary: 关于自动驾驶车辆、模型预测控制、自适应/模糊 PID 控制以及自动驾驶矿卡的论文发表。
---

我的论文主要围绕自动驾驶车辆与矿卡控制算法展开，尤其关注轨迹跟踪精度、载荷变化、车辆动力学、障碍交互以及鲁棒性约束等问题。

## 期刊论文

**Qin T**, Zhu D, Wang C, Yang P, Yang K. *Dual-Loop Fuzzy-PID Acceleration Tracking Controller for Autonomous Mining Trucks under Variable Payload Conditions*. **Coal Engineering**, 2025, 57(6): 172-179. DOI: [10.11799/ce202506022](https://doi.org/10.11799/ce202506022).

- **问题：** 自动驾驶矿卡在空载与满载工况下的纵向动力学差异显著。
- **方法：** 采用双环模糊 PID 加速度跟踪控制器，外环负责速度跟踪，内环负责加速度控制，并依据载荷状态在线调整 PID 参数。
- **结果：** 在可变载荷条件下实现稳定的速度与加速度跟踪，最大速度误差为 0.49 km/h，最大加速度误差为 0.103 m/s<sup>2</sup>。
- **我的贡献：** 第一作者，负责可变载荷纵向控制器设计、仿真分析和论文撰写。

## 会议论文

**Qin T**, Qiu L, Chen J, Fu H, Zhu D, Yang K. *Double-Layer Following Controller for Autonomous Vehicles*. **2024 36th Chinese Control and Decision Conference (CCDC)**, IEEE, 2024, pp. 908-913. DOI: [10.1109/CCDC62350.2024.10587700](https://doi.org/10.1109/CCDC62350.2024.10587700).

- **问题：** 自动驾驶跟车需要在高速超车、急转弯和动态避障过程中同时保持安全车距与平顺性。
- **方法：** 构建结合 DWA 局部规划与模糊自适应 PID 的双层跟车控制框架。
- **结果：** 上层依据车道线和目标车信息规划安全局部路径，下层在线调整 PID 参数实现横纵向跟踪。
- **我的贡献：** 第一作者，负责控制器设计、ROS/VTD 仿真评估和论文撰写。

Wang C, Zhu D, **Qin T**, Yang K. *Lateral Trajectory Tracking of Autonomous Mining Trucks Using MPC with Adaptive Load Compensation*. **2025 44th Chinese Control Conference (CCC)**, IEEE, 2025. DOI: [10.23919/CCC64809.2025.11178743](https://doi.org/10.23919/CCC64809.2025.11178743).

- **问题：** 复杂露天矿道路和载荷变化会削弱自动驾驶矿卡的横向轨迹跟踪精度。
- **方法：** 采用带自适应载荷补偿和实时车辆参数更新的 MPC 控制策略，适配空载与满载状态。
- **结果：** 控制器通过优化控制输出降低载荷波动对预测和轨迹跟踪的影响。
- **我的贡献：** 参与矿卡控制场景建模、实验支持和载荷自适应 MPC 的验证讨论。

Yang P, Zhu D, **Qin T**, Yang K. *Adaptive Heading Tracking Algorithm Based on Vehicle Dynamics Model*. **2025 44th Chinese Control Conference (CCC)**, IEEE, 2025. DOI: [10.23919/CCC64809.2025.11179654](https://doi.org/10.23919/CCC64809.2025.11179654).

- **问题：** 传统纯跟踪方法对目标路径航向信息利用不足，在复杂矿区道路上可能损失跟踪精度。
- **方法：** 提出融合车辆动力学反馈与航向修正的改进纯跟踪算法。
- **结果：** 在 TruckSim/Simulink 验证中，平均横向误差由 0.462 m 降至 0.237 m。
- **我的贡献：** 参与车辆动力学控制场景分析和论文支持。

## 学位论文

**秦天.** *露天矿无人驾驶矿用卡车轨迹跟踪控制*. 硕士学位论文，中国矿业大学（北京），2025. 导师：杨克虎 教授.

- **问题：** 露天矿无人驾驶矿卡在非结构化道路、大范围载荷变化与严格安全约束下，横纵向轨迹跟踪面临多重挑战。
- **方法：** 基于四自由度运动学模型设计 MPC 路径跟踪控制器，底层采用 ADRC 加速度跟踪控制，集成上层路径跟踪与下层动态响应的双层控制架构。
- **结果：** 典型矿区路径全工况仿真表明，所提方案在轨迹跟踪精度、动态响应速度与抗扰鲁棒性上表现更优；四自由度运动学 MPC 在控制精度与运算效率间取得较优平衡。
- **相关成果：** 论文第 2–4 章内容分别对应上述 CCDC 2024 跟车论文、两篇 CCC 2025 会议论文及《煤炭工程》期刊论文。
