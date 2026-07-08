---
title: Notes
date: 2026-06-27
summary: Selected research notes on MPC, reinforcement learning, learning-based control, and autonomous mining systems.
---

This section is for selected public research notes. It does not mirror my private learning archive; instead, it records application-facing ideas that connect my current control background with future PhD research.

## MPC to Learning-Based Control Roadmap

My current foundation is model-based: MPC, LQR, adaptive/fuzzy PID, vehicle dynamics modeling, parameter identification, and trajectory tracking. The next research step is to study how learning can improve adaptation while preserving safety and interpretability.

Questions I am tracking:

- How can reinforcement learning improve control policies under uncertain payload and terrain conditions?
- How can model-based MPC provide structure or safety constraints for learning-based controllers?
- How can data from field operation be used without overfitting to one vehicle, road, or mine scenario?
- How can safety logic such as AEB be integrated with learning-enabled control without weakening deployment reliability?

## Reinforcement Learning Foundations for Control Engineers

I am studying reinforcement learning from a control perspective: Markov decision processes, value functions, policy gradients, dynamic programming, and stability-aware learning. My goal is not to replace control theory, but to understand where learning can help when modeling assumptions are incomplete.

## Field Robotics Questions from Autonomous Mining Trucks

Autonomous mining trucks are a strong testbed for robust autonomy because they combine heavy payloads, rough terrain, repetitive routes, safety constraints, and real operational pressure. These conditions make them useful for studying the boundary between model-based control and adaptive learning.

Near-term note topics:

- Variable payload as a control and learning challenge
- MPC as a safety layer for reinforcement learning
- Data-driven controller adaptation in repetitive industrial routes
- Evaluation metrics beyond tracking error
