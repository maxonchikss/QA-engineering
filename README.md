# Practical Work 1: Black-Box Testing & Test Documentation

## Overview
This module demonstrates practical skills in Black-Box testing methodology, test design, and defect documentation. The work was conducted on two mobile Android applications: 
1. HatUp: An MVP app for street musicians (designed testability requirements and injected 5 controlled defects).
2. Yap: A mobile messenger app (executed comprehensive black-box testing and documented 8 critical/medium defects).

## Objectives
- Analyze functional requirements and system architecture without accessing the source code.
- Design comprehensive test cases covering happy paths, edge cases, and negative scenarios.
- Execute manual tests on Android emulators and physical devices.
- Document discovered defects with clear reproduction steps, severity assessment, and expected vs. actual results.
- Align documentation with GOST 19.401-78 and ISO/IEC/IEEE 29119 standards.

## Tools and Environment
- Target Applications: HatUp (Java, Room DB, MVVM), Yap (Kotlin, Jetpack Compose, Firebase)
- Testing Environment: Android Studio Emulator (API 34), Physical Device (Samsung Galaxy A53, API 33)
- Documentation: Markdown, Jira-style bug tracking templates

## Key Achievements
- Designed and executed over 30 detailed test scenarios.
- Successfully identified and documented 8 defects in the "Yap" application, including:
  - Privacy leaks (FCM push notifications received after account logout).
  - Logic flaws in voice message recording (cancellation on micro-swipes).
  - State desynchronization (UI elements not updating globally).
- Designed 5 controlled defects for the "HatUp" application to simulate real-world QA handover scenarios.

## Artifacts
- [Injected Defects Specification (HatUp)](artifacts/injected-defects-hatup.md)
- [Test Cases (Yap)](artifacts/test-cases-yap.md)
- [Bug Reports (Yap)](artifacts/bug-reports-yap.md)
