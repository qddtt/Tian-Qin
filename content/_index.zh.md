---
title: 首页
date: 2026-06-27
type: landing

design:
  spacing: '3rem'

sections:
  - block: biography
    content:
      username: admin
      text: |-
        我是一名**控制算法工程师**，长期从事自动驾驶矿卡控制系统相关工作，硕士毕业于中国矿业大学（北京）控制科学与工程专业。我的技术基础主要包括 **MPC/LQR 控制**、**自适应/模糊 PID**、**车辆动力学建模**、**参数辨识**，以及自动驾驶矿卡系统的一线工程实践。

        我正在为博士阶段的研究做准备，关注 **强化学习**、**基于学习的控制** 和 **数据驱动自主系统**，尤其关注在载荷变化、矿区道路条件、障碍风险和安全约束下仍能保持可靠性的控制方法。
    design:
      biography:
        style: 'text-align: left;'

  - block: markdown
    content:
      title: 研究方向
      text: |-
        <div class="academic-brief">
          <p class="academic-lead">我的研究兴趣聚焦于复杂非结构化安全关键环境中的重载车辆控制与自主系统。当前工作以模型控制、车辆动力学建模、系统辨识、轨迹跟踪以及自动驾驶矿卡现场经验为基础。</p>

          <div class="research-thread">
            <article>
              <span>基础</span>
              <h3>模型驱动控制</h3>
              <p>MPC、LQR、自适应/模糊 PID、车辆动力学建模、参数辨识，以及面向自动驾驶车辆的轨迹跟踪。</p>
            </article>
            <article>
              <span>应用场景</span>
              <h3>自动驾驶矿卡</h3>
              <p>面向载荷变化、松散路面、长坡道、障碍风险、标定不确定性和安全要求等重载自主系统问题。</p>
            </article>
            <article>
              <span>博士阶段方向</span>
              <h3>基于学习的自主系统</h3>
              <p>探索兼顾可靠性、可解释性与部署约束的数据驱动和强化学习控制方法，用于安全关键自主系统。</p>
            </article>
          </div>
        </div>
    design:
      columns: '1'

  - block: markdown
    content:
      title: 代表性论文
      text: |-
        <div class="publication-list">
          <article class="publication-item">
            <div class="publication-year">2025</div>
            <div>
              <p><strong>Qin T</strong>, Zhu D, Wang C, Yang P, Yang K. <em>Dual-Loop Fuzzy-PID Acceleration Tracking Controller for Autonomous Mining Trucks under Variable Payload Conditions</em>.</p>
              <p class="publication-meta">Coal Engineering, 57(6): 172-179. DOI:10.11799/ce202506022. 关注可变载荷条件下的纵向控制；最大车速误差 0.49 km/h，最大加速度误差 0.103 m/s<sup>2</sup>。</p>
            </div>
          </article>

          <article class="publication-item">
            <div class="publication-year">2025</div>
            <div>
              <p>Wang C, Zhu D, <strong>Qin T</strong>, et al. <em>Lateral Trajectory Tracking of Autonomous Mining Trucks Using MPC with Adaptive Load Compensation</em>.</p>
              <p class="publication-meta">CCC 2025, IEEE. DOI:10.23919/CCC64809.2025.11178743. 关注露天矿道路场景下结合自适应载荷补偿的横向轨迹跟踪。</p>
            </div>
          </article>

          <article class="publication-item">
            <div class="publication-year">2025</div>
            <div>
              <p>Yang P, Zhu D, <strong>Qin T</strong>, et al. <em>Adaptive Heading Tracking Algorithm Based on Vehicle Dynamics Model</em>.</p>
              <p class="publication-meta">CCC 2025, IEEE. DOI:10.23919/CCC64809.2025.11179654. 基于车辆动力学反馈和航向修正；TruckSim/Simulink 验证中平均横向误差由 0.462 m 降至 0.237 m。</p>
            </div>
          </article>

          <article class="publication-item">
            <div class="publication-year">2024</div>
            <div>
              <p><strong>Qin T</strong>, Qiu L, Chen J, et al. <em>Double-Layer Following Controller for Autonomous Vehicles</em>.</p>
              <p class="publication-meta">CCDC 2024, IEEE, pp. 908-913. DOI:10.1109/CCDC62350.2024.10587700. 关注基于 DWA 局部规划与模糊自适应 PID 的自动驾驶跟车控制。</p>
            </div>
          </article>
        </div>

        <p class="section-link"><a href="/zh/publications/">查看全部论文</a></p>
    design:
      columns: '1'

  - block: markdown
    content:
      title: 代表性项目
      text: |-
        <div class="project-list">
          <article class="project-item">
            <h3>露天矿机器人自主运输与装卸系统</h3>
            <p>参与国家重点研发计划项目，围绕自动驾驶矿卡的低速纵向控制、载荷自适应横向 MPC 以及复杂工况下的控制鲁棒性开展工作。</p>
          </article>

          <article class="project-item">
            <h3>rbMPC-truck</h3>
            <p>针对自动驾驶矿卡轨迹跟踪中的 MPC 算法复现与迁移，重点关注控制器对比和代码级理解。</p>
            <p><a href="https://github.com/qddtt/rbMPC-truck">GitHub 仓库</a></p>
          </article>

          <article class="project-item">
            <h3>自动驾驶矿卡现场标定与安全控制</h3>
            <p>包括 LQR 横向控制、双环 PID 纵向控制、AEB 防碰撞逻辑以及基于实车数据的车辆模型辨识。</p>
          </article>

          <article class="project-item">
            <h3>车路云一体化自动驾驶挑战赛</h3>
            <p>面向真实自动驾驶车辆平台进行 LQR 控制器集成与调试，覆盖泊车、避障、变道与掉头等场景。</p>
          </article>
        </div>

        <p class="section-link"><a href="/zh/projects/">查看全部项目</a></p>
    design:
      columns: '1'

  - block: experience
    content:
      title: 教育与经历
      username: admin
    design:
      date_format: '2006年1月'
      is_education_first: true

  - block: awards
    content:
      title: 奖项
      username: admin

  - block: markdown
    content:
      title: 研究笔记
      text: |-
        <div class="notes-preview">
          <p>这里收录的是我公开分享的一部分研究笔记，主要围绕从经典控制走向基于学习的自主系统，内容尽量保持简洁并面向真实应用。</p>
          <p class="section-link"><a href="/zh/notes/">阅读研究笔记</a></p>
        </div>
    design:
      columns: '1'
---
