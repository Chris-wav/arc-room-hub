# A.R.C. Room Hub Roadmap

## Advancement Rule

Only the active MARK may be implemented. A MARK is complete only when every acceptance criterion is demonstrated. Record meaningful learning in `LEARNING_LOG.md` before advancing.

## MARK 0 — Camera and Frame Fundamentals

### Goal

Create a reproducible Python 3.11 vision environment and understand how OpenCV represents and processes a live camera frame.

### Learning Outcomes

- Explain what a NumPy array represents.
- Explain frame shape, dimensions, channels, data type, and pixel-value range.
- Explain the practical difference between OpenCV BGR and RGB ordering.
- Understand the camera read loop and resource cleanup.

### Acceptance Criteria

- [ ] Python 3.11 runs on the Apple Silicon Mac and reports the expected architecture.
- [ ] The project uses an isolated virtual environment.
- [ ] NumPy and OpenCV import successfully inside that environment.
- [ ] A learner-written program opens the local camera and validates each frame read.
- [ ] The program prints a frame's shape, data type, and representative pixel data.
- [ ] The program displays a live frame locally and exits on an intentional user action.
- [ ] The camera and OpenCV windows are released cleanly on normal exit and failure.
- [ ] At least one basic transformation—such as grayscale, crop, resize, or channel conversion—is explained and demonstrated.
- [ ] No image is uploaded, remotely transmitted, or implicitly saved.
- [ ] The learner can explain the frame-processing pipeline in their own words.

## MARK I — Hand Tracking

### Goal

Detect and visualize hand landmarks locally from live camera frames.

### Acceptance Criteria

- [ ] MARK 0 is complete.
- [ ] MediaPipe is introduced with its role explained before use.
- [ ] At least one hand is detected under ordinary room lighting.
- [ ] Landmark coordinates and confidence-related output are understood at a basic level.
- [ ] Landmarks are drawn on the local preview without cloud processing.
- [ ] No-hand and temporary tracking-loss states are handled without crashing.
- [ ] Processing speed is measured on the development Mac and recorded.

## MARK II — Gesture Engine

### Goal

Convert hand observations over time into stable, named gestures without coupling them to hardware actions.

### Acceptance Criteria

- [ ] MARK I is complete.
- [ ] At least three gestures have explicit, documented definitions.
- [ ] Gesture classification is separated from camera capture and rendering.
- [ ] Temporal smoothing or debouncing prevents rapid false activation.
- [ ] Unknown and ambiguous observations produce no command.
- [ ] Gesture behavior is testable from recorded landmark-like data without a live camera.
- [ ] A local demonstration reports stable semantic gesture events.
- [ ] False activations observed in a defined test session are recorded and reviewed.

## MARK III — Native A.R.C. HUD and TV Mirroring

### Goal

Present vision and gesture state through a native PySide6 HUD and mirror it wirelessly to the television.

### Acceptance Criteria

- [ ] MARK II is complete.
- [ ] The HUD runs as a native PySide6 application, not a browser application.
- [ ] Camera processing does not freeze the GUI event loop.
- [ ] The HUD displays current system and gesture state clearly.
- [ ] Start, stop, error, and camera-unavailable states are visible.
- [ ] The HUD can be shown on or mirrored to the television over a wireless local connection.
- [ ] Closing the HUD releases camera and worker resources cleanly.
- [ ] The selected mirroring method and observed latency are documented.

## MARK IV — ESP32 and Physical RGB Lighting

### Goal

Control addressable low-voltage RGB LEDs through an ESP32 over USB serial.

### Acceptance Criteria

- [ ] MARK III is complete.
- [ ] Hardware choices follow a documented low-voltage power and current budget.
- [ ] ESP32 firmware receives and validates commands over USB serial.
- [ ] A versioned command format separates messages from implementation details.
- [ ] At least three lighting states can be triggered intentionally.
- [ ] Malformed, unknown, and interrupted commands fail safely.
- [ ] The computer application detects connection and disconnection without crashing.
- [ ] No 230V circuit or modification is involved.

## MARK V — Wireless Communication

### Goal

Replace or supplement USB serial control with reliable local Wi-Fi communication.

### Acceptance Criteria

- [ ] MARK IV is complete.
- [ ] Transport-independent commands remain unchanged or have a documented migration.
- [ ] The ESP32 accepts authenticated or otherwise locally constrained commands over Wi-Fi.
- [ ] Connection state, timeout, retry, and reconnection behavior are explicit.
- [ ] Loss of Wi-Fi places outputs in a documented safe state.
- [ ] USB serial remains available for diagnosis or recovery.
- [ ] No camera frames are transmitted as part of device control.

## MARK VI — Sensors and Room Awareness

### Goal

Add low-voltage sensor inputs and combine them into useful, explainable room state.

### Acceptance Criteria

- [ ] MARK V is complete.
- [ ] Each sensor has a documented purpose, range, sampling policy, and failure state.
- [ ] Sensor readings are validated and timestamped locally.
- [ ] Room state distinguishes unavailable, stale, and valid observations.
- [ ] At least one useful automation combines sensor state with an explicit user command or gesture.
- [ ] Servo movement, if introduced, has safe mechanical and software limits.
- [ ] Sensor or servo failure cannot create an unsafe hardware state.

## MARK VII — Stable Iron Man Hub v1.0

### Goal

Integrate the proven milestones into a repeatable, maintainable room hub deployment.

### Acceptance Criteria

- [ ] MARK VI is complete.
- [ ] The application installs and runs reproducibly on the Windows ASUS TUF using Python 3.11 or an agreed packaged runtime.
- [ ] Startup, shutdown, reconnect, and recovery paths are documented and tested.
- [ ] Core vision, gesture, HUD, transport, and device behaviors have automated tests where hardware is not required.
- [ ] A repeatable manual end-to-end test covers the physical system.
- [ ] Logs contain operational events but no captured images or sensitive credentials.
- [ ] Configuration and secrets are separated from source control.
- [ ] Known limitations and safe operating instructions are documented.
- [ ] The complete hub runs through an agreed stability session without an unrecovered failure.

