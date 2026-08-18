---
title: 秦天

first_name: 天
last_name: 秦

superuser: true

role: 控制算法工程师

organizations:
  - name: 中国矿业大学（北京）
    url: https://www.cumtb.edu.cn/
  - name: 智能能源与自主采矿实验室
    url: ''

bio: 我从事重载车辆控制与自主系统相关工作，技术基础包括 MPC、LQR、自适应/模糊 PID、车辆动力学建模、参数辨识、轨迹跟踪，以及自动驾驶矿卡现场部署经验。博士阶段拟聚焦安全关键自主系统中的数据驱动与强化学习控制。

profiles:
  - icon: at-symbol
    url: 'mailto:qintian0142@163.com'
    label: 邮箱
  - icon: brands/github
    url: https://github.com/qddtt
    label: GitHub

education:
  - area: 控制科学与工程硕士
    institution: 中国矿业大学（北京）（211）
    date_start: 2023-09-01
    date_end: 2025-09-01
    summary: |
      - GPA：3.59/4.0
      - 导师：杨克虎教授
      - 实验室：智能能源与自主采矿实验室
      - 核心课程：线性系统理论（96）、自适应控制（94）、高级信号处理（93）
      - 研究重点：MPC、自适应/模糊 PID、车辆动力学建模、参数辨识与自动驾驶矿卡

  - area: 电子信息工程学士
    institution: 四川大学（985）
    date_start: 2015-09-01
    date_end: 2019-06-01
    summary: |
      - 核心课程：C 程序设计（91）、计算机通信与网络（86）、通信原理实验（88）、模拟电子技术、信号与系统

work:
  - position: 控制算法工程师
    company_name: 迈德威科技有限公司
    company_url: ''
    company_logo: ''
    date_start: 2025-10-01
    date_end: ''
    summary: |
      - 面向自动驾驶矿卡开发并部署横纵向控制代码，包括 LQR 横向控制和双环 PID 纵向路径跟踪、速度跟踪与制动控制
      - 基于时域轨迹预测与 OBB 检测独立实现 AEB 防碰撞逻辑，用于安全关键矿区道路场景
      - 基于实车数据开展二自由度车辆动力学模型辨识，支持 LQR 参数整定与整车验证

  - position: 硬件工程师
    company_name: 中国航天科工集团
    company_url: ''
    company_logo: ''
    date_start: 2019-07-01
    date_end: 2023-08-01
    summary: |
      - 参与工业车辆控制系统标定与现场联调，包括发动机油门标定
      - 协调控制器、传感器与执行器的联合调试，调整控制参数和接口配置，解决响应滞后与通信异常
      - 支持现场测试、数据记录与问题复现，并将结果反馈到控制策略和硬件配置迭代中

skills:
  - name: 控制与自主系统
    items:
      - name: 模型预测控制
        description: MPC 设计、轨迹跟踪、约束处理与控制器对比
        percent: 90
        icon: devicon/python
      - name: 模糊 PID 控制
        description: 自适应控制、双环跟踪与鲁棒性提升
        percent: 85
        icon: devicon/python
      - name: ROS / C++
        description: 机器人操作系统与自动驾驶栈集成
        percent: 80
        icon: devicon/ros
      - name: MATLAB / Simulink
        description: 控制仿真、车辆动力学建模与快速原型验证
        percent: 80
        icon: devicon/matlab
      - name: 模型标定
        description: 车辆动力学建模、参数辨识与基于实车数据的调参
        percent: 80
        icon: hero/adjustments-horizontal
      - name: Python
        description: 科学计算、实验分析与算法原型实现
        percent: 85
        icon: devicon/python
      - name: PyTorch
        description: 基于学习的控制与强化学习基础
        percent: 45
        icon: devicon/pytorch
  - name: 研究方向
    items:
      - name: 自动驾驶矿卡
        description: 露天矿及非结构化环境中的重载自主系统
        percent: 95
        icon: hero/truck
      - name: 野外机器人
        description: 面向地形、载荷、障碍与安全约束的鲁棒自主
        percent: 85
        icon: hero/cpu-chip
      - name: 基于学习的控制
        description: 面向自主系统的数据驱动与强化学习方法
        percent: 65
        icon: hero/academic-cap

languages:
  - name: 中文
    percent: 100
  - name: 英语（IELTS 6.5；阅读 8.0）
    percent: 75

awards:
  - title: 中国智能网联汽车挑战赛（CICV）2023
    date: '2023-11-25'
    awarder: 中国人工智能学会
    summary: |
      贡献奖（前 5%）。在自适应巡航与跟车任务中，采用 DWA 局部路径规划与模糊 PID 速度/加速度跟踪；横向与纵向加速度均方根分别低于 0.10 m/s<sup>2</sup> 和 0.06 m/s<sup>2</sup>。
  - title: 车路云一体化自动驾驶挑战赛 2024
    date: '2024-06-01'
    awarder: 中国汽车工业协会
    summary: |
      创新奖（前 5%，118 支队伍中排名第 7）。在真实自动驾驶平台上集成并调试 LQR 横向控制器，完成低速泊车与避障验证。
  - title: 全国研究生数学建模竞赛
    date: '2024-09-21'
    awarder: 中国学位与研究生教育发展中心
    summary: |
      参赛奖（前 20%）。采用非线性优化拟合 Steinmetz 方程参数，分析工况变量并将磁性器件损耗模型精度提升 5%。
---

我是一名控制算法工程师，长期从事自动驾驶矿卡控制系统相关工作，硕士毕业于中国矿业大学（北京）控制科学与工程专业。我的技术工作主要围绕模型预测控制（MPC）、LQR、自适应/模糊 PID、车辆动力学建模、参数辨识，以及面向露天矿非结构化环境的自动驾驶矿卡轨迹跟踪。

在研究生阶段前后，我持续参与面向真实部署的自动驾驶矿卡控制问题，包括航天科工阶段的工业车辆标定与现场联调，以及迈德威阶段的 LQR/PID 控制部署、AEB 防碰撞逻辑和基于实车数据的车辆系统辨识。这样的现场经验也塑造了我的研究兴趣：我更关注那些在载荷变化、地形扰动、模型失配、障碍风险和安全约束共同作用下，仍然能够保持可靠性的自主方法。

博士阶段，我希望在现有控制基础之上，进一步拓展到强化学习、基于学习的控制和数据驱动方法，探索如何把模型驱动的可靠性与学习方法的适应能力结合起来，用于复杂机器人和车辆自主系统。
