---
title: 从 MPC 到强化学习与数据驱动控制：走向离线学习策略
date: 2026-08-18
summary: 一个关于如何以世界模型构建离线训练环境、用强化学习优化直接控制策略，并保留约束意识与安全回退机制的研究构想。
authors:
  - admin
translationKey: mpc-to-offline-learned-policies
show_breadcrumb: true
---

> **成熟度：研究构想。** 本文讨论的是拟议架构、关键假设和验证路线，不代表我已经完成世界模型、强化学习控制器或实车实验，也不报告尚不存在的性能结果。

我的控制研究起点是模型驱动方法。在自动驾驶车辆的轨迹跟踪、参数辨识和现场调试中，我逐渐认识到：控制器在标称模型下表现良好，并不意味着它能够自然应对载荷、地形、轮胎特性、执行器迟滞和传感噪声的持续变化。模型失配不是一次性的标定误差，而可能是系统运行中的常态。这也是我希望从 MPC 进一步走向强化学习与数据驱动控制的主要原因。

## MPC 提供了什么，又留下了什么问题

MPC 的重要价值并不只是“在线求最优解”。它把预测模型、性能目标和状态/输入约束放在同一个框架中，使控制决策具备清晰结构。对状态转移

$$x_{t+1}=f(x_t,u_t,\theta_t)+w_t,$$

当参数 $\theta_t$ 和扰动 $w_t$ 随工况变化时，固定模型的预测会逐渐偏离真实系统。可以在线更新模型或采用鲁棒、自适应 MPC，但更复杂的模型、更大的不确定性集合和更长的预测时域也会增加实时求解负担。

我因此不想把学习方法理解为对控制理论的替代。更合理的方向，是保留 MPC 对目标、约束和安全边界的结构化表达，同时让数据驱动模型扩大系统对变化动力学的描述能力，让强化学习在离线环境中承担策略优化。

## 一个离线学习、在线推理的架构

我目前考虑的架构分为离线训练和车端执行两部分。离线阶段先结合运行数据与物理先验训练世界模型，使其近似不同工况下的状态转移；强化学习在这个可交互模型中搜索策略，奖励与惩罚沿用 MPC 中的跟踪目标、控制平滑性和约束意识。训练完成后，得到直接从状态与工况映射到控制动作的策略 $u_t=\pi_\phi(s_t,c_t)$。

<div class="control-architecture" role="group" aria-label="离线世界模型训练与车端策略执行架构">
  <section class="control-architecture__lane">
    <p class="control-architecture__label">离线训练</p>
    <div class="control-architecture__flow">
      <div class="control-architecture__node">运行数据<br>与物理先验</div>
      <span class="control-architecture__arrow" aria-hidden="true">→</span>
      <div class="control-architecture__node">世界模型<br>多工况动力学</div>
      <span class="control-architecture__arrow" aria-hidden="true">→</span>
      <div class="control-architecture__node">强化学习优化<br>MPC 启发的目标与约束</div>
      <span class="control-architecture__arrow" aria-hidden="true">→</span>
      <div class="control-architecture__node control-architecture__node--accent">离线学习策略</div>
    </div>
  </section>
  <section class="control-architecture__lane">
    <p class="control-architecture__label">车端执行</p>
    <div class="control-architecture__flow">
      <div class="control-architecture__node">状态估计<br>与工况上下文</div>
      <span class="control-architecture__arrow" aria-hidden="true">→</span>
      <div class="control-architecture__node">策略推理</div>
      <span class="control-architecture__arrow" aria-hidden="true">→</span>
      <div class="control-architecture__node">安全监督</div>
      <span class="control-architecture__arrow" aria-hidden="true">→</span>
      <div class="control-architecture__node control-architecture__node--accent">执行器</div>
    </div>
    <p class="control-architecture__fallback"><strong>异常路径：</strong>越界、分布外状态或诊断异常 → 已验证的基线控制器</p>
  </section>
</div>

这里的“离线”不是指简单地用历史数据拟合一个策略，而是先建立可以产生反事实轨迹的动力学环境，再在其中优化策略。它降低了在真实系统上进行大规模探索的风险，但也引入了新的核心问题：策略可能利用世界模型的误差，在模型中取得高回报，却无法迁移到真实系统。

## 车端不是字面意义上的“查表”

对于连续、高维状态，完整查找表会迅速受到维度灾难限制。更准确的实现是轻量策略推理：将状态、参考量和工况上下文输入一个紧凑策略网络，以一次前向计算产生控制动作。它保留了“训练时计算较重、部署时计算较轻”的目标，也便于测量确定性的执行延迟。

在这一设想中，车端主控制循环不持续在线求解 MPC。MPC 更像设计框架、离线教师和对照基线：它帮助定义代价、约束与可接受行为，并为学习策略提供可比较的性能边界。

## 安全不能只写进奖励函数

奖励惩罚可以减少危险行为，却不能自动等同于约束保证。车端仍需要独立于学习策略的安全监督器，检查输入边界、状态约束、模型适用范围和系统诊断信息。当策略输出不可接受或当前状态明显偏离训练分布时，监督器应拒绝该动作并切换到已验证的基线控制器。

这并不意味着安全问题已经解决。监督器能否覆盖关键失效模式、切换是否连续、基线控制器在异常工况下是否仍有可行域，都必须单独验证。对安全关键系统而言，“何时不相信学习策略”与“怎样提高平均性能”同样重要。

## 从仿真到实车的验证路线

我会把验证分成三个阶段。第一阶段在仿真中改变动力学参数、外部扰动、观测噪声和执行器迟滞，并比较在线 MPC、传统基线控制器、无安全监督的学习策略以及完整架构。评价指标不仅包括跟踪误差，还应包括约束违反次数与幅度、控制平滑性、最坏工况性能、推理延迟、分布外检测率和回退触发率。

第二阶段进入硬件在环，重点检查计算周期、信号丢失、通信延迟、执行器饱和及控制切换。第三阶段才是受控条件下的实车测试，并逐步扩大工况范围。只有当世界模型误差、策略性能和安全回退都能被独立测量时，离线学习策略才具备继续走向部署的依据。

这条路线最终要回答三个问题：世界模型在多大误差下仍能支持可靠策略？MPC 启发的目标与约束能否有效限制策略搜索？在未见工况中，安全监督和基线回退能否比单纯追求平均回报更稳健？这些问题，而不是某个算法名称，是我下一步希望系统研究的内容。

## 参考文献

1. Wang C, Zhu D, **Qin T**, Yang K. [*Lateral Trajectory Tracking of Autonomous Mining Trucks Using MPC with Adaptive Load Compensation*](https://doi.org/10.23919/CCC64809.2025.11178743). CCC 2025.
2. Ha D, Schmidhuber J. [*World Models*](https://arxiv.org/abs/1803.10122). 2018.
3. Ball P J, Lu C, Parker-Holder J, Roberts S. [*Augmented World Models Facilitate Zero-Shot Dynamics Generalization From a Single Offline Environment*](https://proceedings.mlr.press/v139/ball21a.html). ICML 2021.
4. Zhang X, Bujarbaruah M, Borrelli F. [*Near-Optimal Rapid MPC using Neural Networks: A Primal-Dual Policy Learning Framework*](https://arxiv.org/abs/1912.04744). 2019.
5. Pfrommer S, Gautam T, Zhou A, Sojoudi S. [*Safe Reinforcement Learning with Chance-constrained Model Predictive Control*](https://proceedings.mlr.press/v168/pfrommer22a.html). L4DC 2022.
