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
        I am a **Control Algorithm Engineer** working on autonomous mining-truck control systems, with an M.S. in Control Science and Engineering from China University of Mining and Technology, Beijing. My work connects **MPC/LQR control**, **adaptive/fuzzy PID**, **vehicle dynamics modeling**, **parameter identification**, and field experience in autonomous mining-truck systems.

        I am preparing for PhD study in **reinforcement learning**, **learning-based control**, and **data-driven autonomy**, with an interest in methods that remain reliable under payload variation, mine-road conditions, obstacle risk, and safety constraints.
    design:
      biography:
        style: 'text-align: left;'

  - block: markdown
    content:
      title: Research Focus
      text: |-
        <div class="academic-brief">
          <p class="academic-lead">I study control and autonomy for heavy-duty vehicles operating in unstructured, safety-critical environments. My current work is grounded in model-based control, vehicle dynamics modeling, system identification, trajectory tracking, and field experience with autonomous mining trucks.</p>

          <div class="research-thread">
            <article>
              <span>Foundation</span>
              <h3>Model-Based Control</h3>
              <p>MPC, LQR, adaptive/fuzzy PID, vehicle dynamics modeling, parameter identification, and trajectory tracking for autonomous vehicles.</p>
            </article>
            <article>
              <span>Application Context</span>
              <h3>Autonomous Mining Trucks</h3>
              <p>Heavy-duty autonomy under payload variation, loose terrain, steep grades, obstacle risk, calibration uncertainty, and safety requirements.</p>
            </article>
            <article>
              <span>PhD Direction</span>
              <h3>Learning-Based Autonomy</h3>
              <p>Data-driven and reinforcement-learning-based control methods that preserve reliability, interpretability, and deployment awareness in safety-critical systems.</p>
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
            <div class="publication-year">2025</div>
            <div>
              <p><strong>Qin T</strong>, Zhu D, Wang C, Yang P, Yang K. <em>Dual-Loop Fuzzy-PID Acceleration Tracking Controller for Autonomous Mining Trucks under Variable Payload Conditions</em>.</p>
              <p class="publication-meta">Coal Engineering, 57(6): 172-179. DOI:10.11799/ce202506022. Focus: longitudinal control under empty/full-load dynamics; maximum speed error 0.49 km/h and maximum acceleration error 0.103 m/s<sup>2</sup>.</p>
            </div>
          </article>

          <article class="publication-item">
            <div class="publication-year">2025</div>
            <div>
              <p>Wang C, Zhu D, <strong>Qin T</strong>, et al. <em>Lateral Trajectory Tracking of Autonomous Mining Trucks Using MPC with Adaptive Load Compensation</em>.</p>
              <p class="publication-meta">CCC 2025, IEEE. DOI:10.23919/CCC64809.2025.11178743. Focus: adaptive load compensation for lateral trajectory tracking on open-pit mine roads.</p>
            </div>
          </article>

          <article class="publication-item">
            <div class="publication-year">2025</div>
            <div>
              <p>Yang P, Zhu D, <strong>Qin T</strong>, et al. <em>Adaptive Heading Tracking Algorithm Based on Vehicle Dynamics Model</em>.</p>
              <p class="publication-meta">CCC 2025, IEEE. DOI:10.23919/CCC64809.2025.11179654. Focus: vehicle-dynamics feedback and heading correction; average lateral error decreased from 0.462 m to 0.237 m.</p>
            </div>
          </article>

          <article class="publication-item">
            <div class="publication-year">2024</div>
            <div>
              <p><strong>Qin T</strong>, Qiu L, Chen J, et al. <em>Double-Layer Following Controller for Autonomous Vehicles</em>.</p>
              <p class="publication-meta">CCDC 2024, IEEE, pp. 908-913. DOI:10.1109/CCDC62350.2024.10587700. Focus: DWA local planning with fuzzy-adaptive PID for autonomous following.</p>
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
            <h3>Open-Pit Mine Robot Autonomy</h3>
            <p>National Key Research and Development Program work on low-speed autonomous mining-truck control, including adaptive/fuzzy PID longitudinal control and load-adaptive MPC for lateral trajectory tracking.</p>
          </article>

          <article class="project-item">
            <h3>rbMPC-truck</h3>
            <p>Reproduction and migration of MPC algorithms for autonomous mining-truck trajectory tracking, with emphasis on controller comparison and code-level understanding.</p>
            <p><a href="https://github.com/qddtt/rbMPC-truck">GitHub repository</a></p>
          </article>

          <article class="project-item">
            <h3>Field Calibration and Safety Control for Autonomous Mining Trucks</h3>
            <p>LQR lateral control, dual-loop PID longitudinal control, AEB anti-collision logic, and two-degree-of-freedom vehicle model identification from real-vehicle data.</p>
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
