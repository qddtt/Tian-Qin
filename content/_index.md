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
        I am a control and autonomous-systems researcher with an M.Sc. in Control Science and Engineering from China University of Mining and Technology, Beijing. My work connects **model-based control**, **trajectory tracking**, **vehicle model calibration**, and field experience in autonomous mining-truck systems.

        I am preparing for PhD study in **reinforcement learning**, **learning-based control**, and **data-driven autonomy**, with an interest in methods that remain reliable under payload variation, mine-road conditions, and safety constraints.
    design:
      biography:
        style: 'text-align: left;'

  - block: markdown
    content:
      title: Research Focus
      text: |-
        <div class="academic-brief">
          <p class="academic-lead">I study control and autonomy for heavy-duty vehicles operating in unstructured, safety-critical environments. My current work is grounded in model-based control, vehicle dynamics, trajectory tracking, model calibration, and field experience with unmanned mining trucks.</p>

          <div class="research-thread">
            <article>
              <span>Foundation</span>
              <h3>Model-Based Control</h3>
              <p>MPC, LQR, fuzzy-PID, vehicle dynamics, model calibration, parameter identification, and trajectory tracking for autonomous vehicles.</p>
            </article>
            <article>
              <span>Application Context</span>
              <h3>Autonomous Mining Trucks</h3>
              <p>Heavy-duty autonomy under payload variation, loose terrain, steep grades, communication limits, and safety requirements.</p>
            </article>
            <article>
              <span>PhD Direction</span>
              <h3>Learning-Based Autonomy</h3>
              <p>Reinforcement learning and data-driven control methods that preserve reliability, interpretability, and deployment awareness in safety-critical systems.</p>
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
              <p class="publication-meta">Coal Engineering, accepted. Focus: variable-payload acceleration tracking; maximum speed error 0.49 km/h and maximum acceleration error 0.103 m/s^2.</p>
            </div>
          </article>

          <article class="publication-item">
            <div class="publication-year">2025</div>
            <div>
              <p>Wang C, Zhu D, <strong>Qin T</strong>, et al. <em>Lateral Trajectory Tracking of Autonomous Mining Trucks Using MPC with Adaptive Load Compensation</em>.</p>
              <p class="publication-meta">CCC 2025, IEEE. Focus: load-adaptive MPC in Simulink/TruckSim; full-load lateral MAE reduced by 33.33% compared with LQR.</p>
            </div>
          </article>

          <article class="publication-item">
            <div class="publication-year">2025</div>
            <div>
              <p>Yang P, Zhu D, <strong>Qin T</strong>, et al. <em>Adaptive Heading Tracking Algorithm Based on Vehicle Dynamics Model</em>.</p>
              <p class="publication-meta">CCC 2025, IEEE. Focus: heading-corrected pure pursuit with vehicle-dynamics modeling; average lateral error decreased from 0.462 m to 0.237 m.</p>
            </div>
          </article>

          <article class="publication-item">
            <div class="publication-year">2024</div>
            <div>
              <p><strong>Qin T</strong>, Qiu L, Chen J, et al. <em>Double-Layer Following Controller for Autonomous Vehicles</em>.</p>
              <p class="publication-meta">CCDC 2024, IEEE, pp. 908-913. Focus: DWA local planning with fuzzy-adaptive PID; lateral and longitudinal acceleration RMS improved by 19.5% and 37.3%.</p>
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
            <h3>Autonomous Transportation and Loading/Unloading System for Large Open-Pit Mine Robots</h3>
            <p>National Key Research and Development Program work on low-speed unmanned mining-truck control, including adaptive/fuzzy-PID longitudinal control and load-adaptive MPC for lateral trajectory tracking.</p>
          </article>

          <article class="project-item">
            <h3>rbMPC-truck</h3>
            <p>Reproduction and migration of MPC algorithms for autonomous mining-truck trajectory tracking, with emphasis on controller comparison and code-level understanding.</p>
            <p><a href="https://github.com/qddtt/rbMPC-truck">GitHub repository</a></p>
          </article>

          <article class="project-item">
            <h3>Field Calibration and Safety Control for Autonomous Mining Trucks</h3>
            <p>Vehicle-response parameter calibration, longitudinal speed/braking validation, and remote safety-control strategies for autonomous mining-truck operation under slopes, payload changes, and mine-road variation.</p>
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
