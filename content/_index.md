---
title: Home
date: 2026-06-27
type: landing

design:
  spacing: '4.5rem'

sections:
  - block: biography
    content:
      username: admin
      button:
        text: Download CV
        url: uploads/cv-qin-tian.pdf
    design:
      banner:
        filename: kalen-emsley-Bkci_8qcdvQ-unsplash.jpg
      biography:
        style: 'text-align: justify; font-size: 0.95em;'

  - block: markdown
    content:
      title: Research Arc
      text: |-
        I study control and autonomy for heavy-duty vehicles operating in complex, unstructured environments. My current work is grounded in **Model Predictive Control (MPC)**, fuzzy-PID control, trajectory tracking, and field-deployed unmanned mining truck systems.

        My PhD goal is to extend this foundation toward **reinforcement learning**, **learning-based control**, and **data-driven autonomy**. I am especially interested in methods that combine the reliability of model-based control with the adaptability of learning methods under payload variation, terrain uncertainty, and safety constraints.

        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:1rem;margin-top:1.25rem;">
          <div style="border:1px solid rgba(148,163,184,.35);border-radius:8px;padding:1rem;">
            <strong>Control Foundation</strong><br>
            <span style="font-size:.9rem;">MPC, LQR, fuzzy-PID, trajectory tracking, and vehicle dynamics modeling.</span>
          </div>
          <div style="border:1px solid rgba(148,163,184,.35);border-radius:8px;padding:1rem;">
            <strong>Field Context</strong><br>
            <span style="font-size:.9rem;">Autonomous mining trucks, variable payloads, steep grades, loose terrain, and safety-critical deployment.</span>
          </div>
          <div style="border:1px solid rgba(148,163,184,.35);border-radius:8px;padding:1rem;">
            <strong>PhD Direction</strong><br>
            <span style="font-size:.9rem;">Learning-based and data-driven control for robust autonomous systems.</span>
          </div>
        </div>
    design:
      columns: '1'

  - block: markdown
    content:
      title: Selected Publications
      text: |-
        **Journal**

        **Qin T**, Zhu D, Wang C, et al. *Dual-Loop Fuzzy-PID Acceleration Tracking Controller for Autonomous Mining Trucks under Variable Payload Conditions*. **Coal Engineering**, 2026 (in press).

        **Conference**

        **Qin T**, Qiu L, Chen J, et al. *Double-Layer Following Controller for Autonomous Vehicles*. **CCDC 2024**, IEEE, pp. 908-913.

        Wang C, Zhu D, **Qin T**, et al. *Lateral Trajectory Tracking of Autonomous Mining Trucks Using MPC with Adaptive Load Compensation*. **CCC 2025**, IEEE.

        Yang P, Zhu D, **Qin T**, et al. *Adaptive Heading Tracking Algorithm Based on Vehicle Dynamics Model*. **CCC 2025**, IEEE.

        [View all publications](/publications/)
    design:
      columns: '1'

  - block: markdown
    content:
      title: Selected Projects
      text: |-
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1rem;">
          <div style="border:1px solid rgba(148,163,184,.35);border-radius:8px;padding:1rem;">
            <strong>rbMPC-truck</strong><br>
            <span style="font-size:.9rem;">Reproduction and migration of MPC algorithms for autonomous mining truck trajectory tracking.</span><br>
            <a href="https://github.com/qddtt/rbMPC-truck">github.com/qddtt/rbMPC-truck</a>
          </div>
          <div style="border:1px solid rgba(148,163,184,.35);border-radius:8px;padding:1rem;">
            <strong>Unmanned Mining Truck Control System</strong><br>
            <span style="font-size:.9rem;">PLC-based controller and redundancy logic supporting 165+ unmanned mining trucks in field operation.</span>
          </div>
          <div style="border:1px solid rgba(148,163,184,.35);border-radius:8px;padding:1rem;">
            <strong>Vehicle-Road-Cloud Autopilot Challenge</strong><br>
            <span style="font-size:.9rem;">LQR controller integration on a real autonomous vehicle platform; ranked 7th among 118 teams.</span>
          </div>
        </div>

        [View all projects](/projects/)
    design:
      columns: '1'

  - block: markdown
    content:
      title: Research Notes
      text: |-
        I use the notes section for selected, public-facing research reflections that connect my control background with learning-based methods.

        - MPC to learning-based control roadmap
        - Reinforcement learning foundations for control researchers
        - Field robotics questions from autonomous mining truck deployment

        [Read selected notes](/notes/)
    design:
      columns: '1'

  - block: experience
    content:
      title: Experience
      username: admin
    design:
      date_format: 'January 2006'
      is_education_first: true

  - block: awards
    content:
      title: Awards
      username: admin

  - block: languages
    content:
      title: Languages
      username: admin
---
