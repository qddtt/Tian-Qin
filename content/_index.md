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


  - block: markdown
    id: section-2
    content:
    title: Publications
    text: |
      <span style='font-size: 14px;'>

      <b>Journal:</b><br>
      <b>Qin T</b>, Zhu Desheng, Wang Chunhui, et al. 
      <i>Dual-Loop Fuzzy-PID Acceleration Tracking Controller for Autonomous Mining Trucks under Variable Payload Conditions</i> [J]. Coal Engineering. [Decision in Process]<br>
      -- Target: Addressed dynamic payload variations with a dual-loop fuzzy PID with self-adaptive compensation.<br>
      -- Outcome: Maximum speed error 0.49 km/h (1.6%), acceleration error 0.103 m/s².<br>
      -- Comparison: Compared to MPC, peak-to-peak speed error reduced by 8.77%, acceleration error reduced by 13.30%.<br><br>

      <b>Conference:</b><br>
      <b>Qin T</b>, Qiu L, Chen J, et al. 
      <i>Double-Layer Following Controller for Autonomous Vehicles</i>. 2024 36th Chinese Control and Decision Conference (CCDC), IEEE 2024:908–913.<br>
      -- Proposed a DWA and fuzzy-adaptive PID dual-layer controller. Reduced lateral acceleration RMS by 19.5% compared to PID-Stanley.<br><br>

      Wang C, Zhu D, <b>Qin T</b>, et al. 
      <i>Lateral Trajectory Tracking of Autonomous Mining Trucks Using MPC with Adaptive Load Compensation</i>. Chinese Control and Conference (CCC), IEEE 2025.<br>
      -- Achieved 33.33% reduction in mean lateral error compared to LQR, improving robustness.<br><br>

      Yang P, Zhu D, <b>Qin T</b>, et al. 
      <i>Adaptive Heading Tracking Algorithm Based on Vehicle Dynamics Model</i>. Chinese Control and Conference (CCC), IEEE 2025.<br>
      -- Demonstrated 47% reduction in lateral error compared to pure pursuit, enhancing navigation precision.<br>

      </span>


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
