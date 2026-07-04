---
title: Home
date: 2026-06-27
type: landing

design:
  spacing: '3rem'

sections:
  - block: biography
    content:
      username: admin
      text: |-
        I am an M.Sc. student in Control Science and Engineering at China University of Mining and Technology, Beijing. My work connects **model-based control**, **trajectory tracking**, and field experience in autonomous mining-truck systems.

        I am preparing for PhD study in **reinforcement learning**, **learning-based control**, and **data-driven autonomy**, with an interest in methods that remain reliable under payload, terrain, and safety constraints.
      button:
        text: Download CV
        url: /uploads/cv-qin-tian.pdf
    design:
      biography:
        style: 'text-align: left;'

  - block: markdown
    content:
      title: Research Focus
      text: |-
        <div class="academic-brief">
          <p class="academic-lead">I study control and autonomy for heavy-duty vehicles operating in unstructured, safety-critical environments. My current work is grounded in model-based control, trajectory tracking, and field experience with unmanned mining trucks.</p>

          <div class="research-thread">
            <article>
              <span>Foundation</span>
              <h3>Model-Based Control</h3>
              <p>MPC, LQR, fuzzy-PID, vehicle dynamics, constraint handling, and trajectory tracking for autonomous vehicles.</p>
            </article>
            <article>
              <span>Application Context</span>
              <h3>Autonomous Mining Trucks</h3>
              <p>Heavy-duty autonomy under payload variation, loose terrain, steep grades, communication limits, and safety requirements.</p>
            </article>
            <article>
              <span>PhD Direction</span>
              <h3>Learning-Based Autonomy</h3>
              <p>Reinforcement learning and data-driven control methods that preserve reliability, interpretability, and deployment awareness.</p>
            </article>
          </div>
        </div>
    design:
      columns: '1'

  - block: markdown
    content:
      title: Selected Publications
      text: |-
        <div class="publication-list">
          <article class="publication-item">
            <div class="publication-year">2026</div>
            <div>
              <p><strong>Qin T</strong>, Zhu D, Wang C, et al. <em>Dual-Loop Fuzzy-PID Acceleration Tracking Controller for Autonomous Mining Trucks under Variable Payload Conditions</em>.</p>
              <p class="publication-meta">Coal Engineering, in press. Focus: variable-payload acceleration tracking for low-speed unmanned mining trucks.</p>
            </div>
          </article>

          <article class="publication-item">
            <div class="publication-year">2025</div>
            <div>
              <p>Wang C, Zhu D, <strong>Qin T</strong>, et al. <em>Lateral Trajectory Tracking of Autonomous Mining Trucks Using MPC with Adaptive Load Compensation</em>.</p>
              <p class="publication-meta">CCC 2025, IEEE. Focus: MPC-based trajectory tracking under load variation.</p>
            </div>
          </article>

          <article class="publication-item">
            <div class="publication-year">2024</div>
            <div>
              <p><strong>Qin T</strong>, Qiu L, Chen J, et al. <em>Double-Layer Following Controller for Autonomous Vehicles</em>.</p>
              <p class="publication-meta">CCDC 2024, IEEE, pp. 908-913. Focus: planning-control integration and comfort-aware following control.</p>
            </div>
          </article>
        </div>

        <p class="section-link"><a href="/publications/">View all publications</a></p>
    design:
      columns: '1'

  - block: markdown
    content:
      title: Selected Projects
      text: |-
        <div class="project-list">
          <article class="project-item">
            <h3>rbMPC-truck</h3>
            <p>Reproduction and migration of MPC algorithms for autonomous mining-truck trajectory tracking, with emphasis on controller comparison and code-level understanding.</p>
            <p><a href="https://github.com/qddtt/rbMPC-truck">GitHub repository</a></p>
          </article>

          <article class="project-item">
            <h3>Unmanned Mining Truck Control System</h3>
            <p>PLC-based controller design, redundancy logic, safety-critical signal handling, and fault diagnosis from field engineering work before graduate study.</p>
          </article>

          <article class="project-item">
            <h3>Vehicle-Road-Cloud Autopilot Challenge</h3>
            <p>LQR controller integration on a real autonomous vehicle platform for parking, obstacle avoidance, lane changing, and U-turn scenarios; ranked 7th among 118 teams.</p>
          </article>
        </div>

        <p class="section-link"><a href="/projects/">View all projects</a></p>
    design:
      columns: '1'

  - block: experience
    content:
      title: Education and Experience
      username: admin
    design:
      date_format: 'January 2006'
      is_education_first: true

  - block: awards
    content:
      title: Awards
      username: admin

  - block: markdown
    content:
      title: Research Notes
      text: |-
        <div class="notes-preview">
          <p>I keep selected public notes on the transition from classical control to learning-based autonomy. The notes are intentionally concise and application-facing.</p>
          <p class="section-link"><a href="/notes/">Read selected notes</a></p>
        </div>
    design:
      columns: '1'
---
