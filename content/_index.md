---
title: 'Home'
date: 2023-10-24
type: landing

design:
  # Default section spacing
  spacing: "4rem"

# Note: `username` refers to the user's folder name in `content/authors/`

# Page sections
sections:
  - block: biography
    content:
      username: admin
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download Résumé
        url: uploads/resume.pdf
    design:
      banner:
        # Upload your cover image to the `assets/media/` folder and reference it here
        filename: kalen-emsley-Bkci_8qcdvQ-unsplash.jpg
      biography:
        # Customize the style of your biography text
        style: 'text-align: justify; font-size: 0.8em;'

  - block: experience
    content:
      title: Skills & Hobbies
      username: admin
    design:
      # Hugo date format
      date_format: 'January 2006'
      # Education or Experience section first?
      is_education_first: true

  # - block: publications
  #   content:
  #     title: Publications
  #     username: admin
  - block: markdown
    id: section-2
    content:
      title: Publications
      subtitle: In submit
      text: 
        <b>Qin Tian</b>, Zhu Desheng, Wang Chunhui, et al. <i>Dual-Loop Fuzzy-PID Acceleration Tracking Controller for Autonomous Mining Trucks under Variable Payload Conditions</i>[J]. Coal Engineering. [Decision in Process]<br>
        <span style="font-size: 24px;">Targeting large-scale dynamic payload variations in mining trucks, developed a dual-loop fuzzy PID control architecture with parameter self-adaptive compensation.</span>
        # Outcome: Achieved a maximum speed error of 0.49 km/h (1.6% of the running speed) and maximum acceleration error of 0.103 m/s².
# Comparison: Compared with MPC, the peak-to-peak speed error reduced by 8.77%, and the acceleration error reduced by 13.30%.
# Conference
# Qin T, Qiu L, Chen J, et al. Double-Layer Following Controller for Autonomous Vehicles. 2024 36th Chinese Control and Decision Conference (CCDC).IEEE 2024:908-913.
# A dual-layer controller integrating DWA and fuzzy-adaptive PID was proposed for autonomous vehicles. This method resulted in a 19.5% reduction in the root mean square of lateral acceleration compared to the PID-Stanley algorithm, enhancing comfort while ensuring safety.
# Wang C, Zhu D, Qin T, et al. Lateral Trajectory Tracking of Autonomous Mining Trucks Using MPC with Adaptive Load Compensation. Chinese Control and Conference (CCC), IEEE 2025.
# The proposed model predictive control (MPC) algorithm with adaptive load compensation showed a 33.33% decrease in mean lateral error compared to the LQR algorithm under varying payload conditions, improving the system's robustness and accuracy in dynamic environments.
# Yang P, Zhu D, Qin T, et al. Adaptive Heading Tracking Algorithm Based on Vehicle Dynamics Model. Chinese Control and Conference (CCC), IEEE 2025.
# The adaptive heading tracking algorithm demonstrated a 47% reduction in lateral error compared to traditional pure tracking algorithms, significantly enhancing control precision and stability in the autonomous navigation of mining trucks.

  - block: skills
    content:
      title: Skills & Hobbies
      username: admin
  - block: awards
    content:
      title: Awards
      username: admin
  - block: languages
    content:
      title: Languages
      username: admin
---
