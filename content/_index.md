---
title: 'Home'
date: 2023-10-24
type: landing

design:
  spacing: '5rem'

sections:
  # ── About / Biography ─────────────────────────────────
  - block: biography
    content:
      username: admin
      button:
        text: Download CV
        url: uploads/resume.pdf
    design:
      banner:
        filename: kalen-emsley-Bkci_8qcdvQ-unsplash.jpg
      biography:
        style: 'text-align: justify; font-size: 0.9em;'

  # ── Research Interests ────────────────────────────────
  - block: markdown
    content:
      title: 'Research Interests'
      text: |-
        My research lies at the intersection of **optimal control**, **autonomous navigation**, and **field robotics** — with a focus on unstructured, off-road environments where payload, terrain, and safety constraints interact.

        **Model Predictive Control (MPC) for Autonomous Mining Trucks**
        <span style="font-size:0.85em;">
        Developing real-time MPC frameworks that handle variable payload conditions (30–150 tons), steep grades, and loose terrain in open-pit mines. Current work on adaptive load compensation achieves <b>33% lateral error reduction</b> over LQR baselines.
        </span>

        **Fuzzy-PID & Hybrid Control Architectures**
        <span style="font-size:0.85em;">
        Dual-loop fuzzy-PID controllers for acceleration tracking in mining trucks. Self-adaptive compensation reduces peak-to-peak speed error by <b>8.77%</b> and acceleration error by <b>13.30%</b> compared to pure MPC — combining the robustness of fuzzy logic with the predictive power of MPC.
        </span>

        **Vehicle-Road-Cloud Integration**
        <span style="font-size:0.85em;">
        Deployed LQR controllers on real autonomous vehicle platforms for parking, obstacle avoidance, lane-changing, and U-turns — achieving <b>7th place out of 118 teams</b> in national competition.
        </span>

    design:
      columns: '1'

  # ── Publications ──────────────────────────────────────
  - block: markdown
    id: publications
    content:
      title: 'Publications'
      text: |-
        <span style='font-size: 15px;'>

        <b style='font-size: 17px;'>Journal</b><br>
        <b>Qin T</b>, Zhu D, Wang C, et al. <i>Dual-Loop Fuzzy-PID Acceleration Tracking Controller for Autonomous Mining Trucks under Variable Payload Conditions</i>. <b>Coal Engineering</b>, 2026 (in press).<br>
        <span style='color: #666;'>→ Dual-loop fuzzy PID with self-adaptive compensation. Max speed error 0.49 km/h (1.6%). 8.77% improvement in peak-to-peak error vs. MPC.</span>

        <br><b style='font-size: 17px;'>Conference</b><br>
        <b>Qin T</b>, Qiu L, Chen J, et al. <i>Double-Layer Following Controller for Autonomous Vehicles</i>. <b>CCDC 2024</b>, IEEE, pp. 908–913.<br>
        <span style='color: #666;'>→ DWA + fuzzy-adaptive PID dual-layer controller. 19.5% reduction in lateral acceleration RMS vs. PID-Stanley.</span>

        <br>Wang C, Zhu D, <b>Qin T</b>, et al. <i>Lateral Trajectory Tracking of Autonomous Mining Trucks Using MPC with Adaptive Load Compensation</i>. <b>CCC 2025</b>, IEEE.<br>
        <span style='color: #666;'>→ 33.33% reduction in mean lateral error vs. LQR, improving robustness under variable payload.</span>

        <br>Yang P, Zhu D, <b>Qin T</b>, et al. <i>Adaptive Heading Tracking Algorithm Based on Vehicle Dynamics Model</i>. <b>CCC 2025</b>, IEEE.<br>
        <span style='color: #666;'>→ 47% reduction in lateral error compared to pure pursuit, enhancing navigation precision.</span>

        </span>
    design:
      columns: '1'

  # ── Projects ──────────────────────────────────────────
  - block: markdown
    id: projects
    content:
      title: 'Projects'
      text: |-
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem;">

        <div style="border: 1px solid #e5e7eb; border-radius: 8px; padding: 1.2rem; background: rgba(255,255,255,0.03);">
        <b>rbMPC-truck</b><br>
        <span style="font-size:0.85em; color:#666;">
        Reproduction and migration of Model Predictive Control algorithms for autonomous mining trucks.
        </span>
        <br><span style="font-size:0.8em;">
        <a href="https://github.com/qddtt/rbMPC-truck">github.com/qddtt/rbMPC-truck</a>
        </span>
        </div>

        <div style="border: 1px solid #e5e7eb; border-radius: 8px; padding: 1.2rem; background: rgba(255,255,255,0.03);">
        <b>Unmanned Mining Truck Control System</b><br>
        <span style="font-size:0.85em; color:#666;">
        PLC-based control redundancy system deployed across 165+ unmanned mining trucks at CASIC (2019–2023).
        </span>
        </div>

        <div style="border: 1px solid #e5e7eb; border-radius: 8px; padding: 1.2rem; background: rgba(255,255,255,0.03);">
        <b>Autopilot Challenge 2024</b><br>
        <span style="font-size:0.85em; color:#666;">
        LQR controller integration on real autonomous vehicle platform. 7th/118 teams in vehicle-road-cloud competition.
        </span>
        </div>

        <div style="border: 1px solid #e5e7eb; border-radius: 8px; padding: 1.2rem; background: rgba(255,255,255,0.03);">
        <b>CICV 2023 Adaptive Cruise Controller</b><br>
        <span style="font-size:0.85em; color:#666;">
        DWA + Fuzzy-PID hybrid controller in VTD simulation. Lateral accel RMS < 0.1 m/s², longitudinal < 0.06 m/s².
        </span>
        </div>

        </div>
    design:
      columns: '1'

  # ── Experience ────────────────────────────────────────
  - block: experience
    content:
      title: 'Experience'
      username: admin
    design:
      date_format: 'January 2006'
      is_education_first: true

  # ── Awards ────────────────────────────────────────────
  - block: awards
    content:
      title: 'Awards'
      username: admin

  # ── Skills & Tools ────────────────────────────────────
  - block: markdown
    content:
      title: 'Skills & Tools'
      text: |-
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem;">

        <div>
        <b style="font-size: 0.95rem;">Control & Optimization</b><br>
        <span style="display: inline-block; background: rgba(99,102,241,0.1); color: var(--color-primary); border-radius: 999px; padding: 0.2rem 0.7rem; font-size: 0.8rem; margin: 0.2rem;">Model Predictive Control</span>
        <span style="display: inline-block; background: rgba(99,102,241,0.1); color: var(--color-primary); border-radius: 999px; padding: 0.2rem 0.7rem; font-size: 0.8rem; margin: 0.2rem;">Fuzzy-PID Control</span>
        <span style="display: inline-block; background: rgba(99,102,241,0.1); color: var(--color-primary); border-radius: 999px; padding: 0.2rem 0.7rem; font-size: 0.8rem; margin: 0.2rem;">LQR / DWA</span>
        <span style="display: inline-block; background: rgba(99,102,241,0.1); color: var(--color-primary); border-radius: 999px; padding: 0.2rem 0.7rem; font-size: 0.8rem; margin: 0.2rem;">Trajectory Tracking</span>
        <span style="display: inline-block; background: rgba(99,102,241,0.1); color: var(--color-primary); border-radius: 999px; padding: 0.2rem 0.7rem; font-size: 0.8rem; margin: 0.2rem;">Particle Swarm Opt.</span>
        </div>

        <div>
        <b style="font-size: 0.95rem;">Programming & Tools</b><br>
        <span style="display: inline-block; background: rgba(99,102,241,0.1); color: var(--color-primary); border-radius: 999px; padding: 0.2rem 0.7rem; font-size: 0.8rem; margin: 0.2rem;">Python</span>
        <span style="display: inline-block; background: rgba(99,102,241,0.1); color: var(--color-primary); border-radius: 999px; padding: 0.2rem 0.7rem; font-size: 0.8rem; margin: 0.2rem;">ROS / C++</span>
        <span style="display: inline-block; background: rgba(99,102,241,0.1); color: var(--color-primary); border-radius: 999px; padding: 0.2rem 0.7rem; font-size: 0.8rem; margin: 0.2rem;">MATLAB / Simulink</span>
        <span style="display: inline-block; background: rgba(99,102,241,0.1); color: var(--color-primary); border-radius: 999px; padding: 0.2rem 0.7rem; font-size: 0.8rem; margin: 0.2rem;">PyTorch</span>
        <span style="display: inline-block; background: rgba(99,102,241,0.1); color: var(--color-primary); border-radius: 999px; padding: 0.2rem 0.7rem; font-size: 0.8rem; margin: 0.2rem;">PLC Programming</span>
        </div>

        <div>
        <b style="font-size: 0.95rem;">Simulation & Platforms</b><br>
        <span style="display: inline-block; background: rgba(99,102,241,0.1); color: var(--color-primary); border-radius: 999px; padding: 0.2rem 0.7rem; font-size: 0.8rem; margin: 0.2rem;">VTD (Virtual Test Drive)</span>
        <span style="display: inline-block; background: rgba(99,102,241,0.1); color: var(--color-primary); border-radius: 999px; padding: 0.2rem 0.7rem; font-size: 0.8rem; margin: 0.2rem;">CarSim / TruckSim</span>
        <span style="display: inline-block; background: rgba(99,102,241,0.1); color: var(--color-primary); border-radius: 999px; padding: 0.2rem 0.7rem; font-size: 0.8rem; margin: 0.2rem;">Gazebo</span>
        <span style="display: inline-block; background: rgba(99,102,241,0.1); color: var(--color-primary); border-radius: 999px; padding: 0.2rem 0.7rem; font-size: 0.8rem; margin: 0.2rem;">Baostock / qlib</span>
        </div>

        <div>
        <b style="font-size: 0.95rem;">Research Interests</b><br>
        <span style="display: inline-block; background: rgba(236,72,153,0.1); color: #ec4899; border-radius: 999px; padding: 0.2rem 0.7rem; font-size: 0.8rem; margin: 0.2rem;">Autonomous Mining</span>
        <span style="display: inline-block; background: rgba(236,72,153,0.1); color: #ec4899; border-radius: 999px; padding: 0.2rem 0.7rem; font-size: 0.8rem; margin: 0.2rem;">Field Robotics</span>
        <span style="display: inline-block; background: rgba(236,72,153,0.1); color: #ec4899; border-radius: 999px; padding: 0.2rem 0.7rem; font-size: 0.8rem; margin: 0.2rem;">Optimal Control</span>
        <span style="display: inline-block; background: rgba(236,72,153,0.1); color: #ec4899; border-radius: 999px; padding: 0.2rem 0.7rem; font-size: 0.8rem; margin: 0.2rem;">Vehicle-Road-Cloud</span>
        <span style="display: inline-block; background: rgba(236,72,153,0.1); color: #ec4899; border-radius: 999px; padding: 0.2rem 0.7rem; font-size: 0.8rem; margin: 0.2rem;">Reinforcement Learning</span>
        </div>

        </div>

  # ── Languages ─────────────────────────────────────────
  - block: languages
    content:
      title: 'Languages'
      username: admin
---
