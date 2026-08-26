# A.R.C. Room Hub — Project Context

## Purpose

A.R.C. Room Hub is a native, local-first room-computing system inspired by Iron Man interfaces. It will combine real-time computer vision, gesture interpretation, a native HUD, wireless TV presentation, and low-voltage physical outputs.

The project is deliberately incremental. Each MARK must produce a demonstrable capability and a learning outcome before the next subsystem is introduced.

## System Context

| Concern | Decision |
|---|---|
| Development | Apple Silicon Mac (`arm64`), macOS |
| Deployment | ASUS TUF, Windows |
| Shared language runtime | Python 3.11 |
| Initial vision stack | NumPy and OpenCV |
| Hand tracking | MediaPipe, introduced in MARK I |
| Native HUD | PySide6, introduced in MARK III |
| Hardware controller | ESP32 with C/C++, introduced in MARK IV |
| Initial device transport | USB serial |
| Later device transport | Local Wi-Fi, introduced in MARK V |
| First physical output | Addressable low-voltage RGB LEDs |
| Later physical I/O | Sensors and servos |
| Image privacy | Local processing only; no cloud storage or transmission |
| Electrical boundary | Low voltage only; no 230V work |

## Architectural Direction

The repository will remain a native application project rather than a web platform. React, Node.js, REST APIs, and browser dashboards are excluded from the central architecture.

The intended subsystem boundaries are:

1. **Vision input** acquires frames from a camera and reports acquisition errors.
2. **Vision processing** performs deterministic transformations and later extracts hand landmarks.
3. **Gesture engine** converts observations over time into semantic commands.
4. **Native HUD** renders state and feedback through PySide6.
5. **Device transport** sends commands through USB serial and later local Wi-Fi.
6. **ESP32 firmware** converts validated commands into low-voltage physical output.
7. **Room awareness** combines later sensor observations into local room state.

These boundaries are conceptual during MARK 0. Files and abstractions should be introduced only when the active milestone needs them.

## High-Level Data Flow

```text
Local camera
    -> frame acquisition
    -> local frame processing
    -> hand observations
    -> temporal gesture engine
    -> application command/state
    -> native PySide6 HUD
    -> USB serial / local Wi-Fi transport
    -> ESP32
    -> addressable RGB LEDs, sensors, servos
```

Raw frames stop at the local vision boundary unless the user explicitly chooses a local diagnostic capture. No camera frame is sent to a cloud service.

## Cross-Platform Strategy

- Use Python 3.11 on macOS and Windows to reduce runtime differences.
- Keep vision algorithms independent from camera enumeration and GUI event loops.
- Isolate device selection, camera backends, permissions, paths, and serial-port names as platform-specific concerns.
- Verify milestone acceptance on the Mac first during development, then add Windows deployment verification when the runtime application becomes relevant.
- Do not assume that camera indices, capture backends, display behavior, or serial device names match between operating systems.

## Privacy and Safety Decisions

- Camera processing is local and ephemeral by default.
- Recording, snapshots, telemetry, and remote streaming are not implicit features.
- Diagnostic images, if ever needed, require an explicit local action and must not be committed to Git.
- The system must degrade safely when a camera, ESP32, sensor, or transport disappears.
- Hardware work is limited to low-voltage, current-limited circuits.
- Work involving mains voltage is outside the project scope.

## Dependency Timing

Dependencies are introduced at the first milestone that needs them:

- MARK 0: Python 3.11, NumPy, OpenCV.
- MARK I: MediaPipe.
- MARK III: PySide6.
- MARK IV: ESP32 firmware toolchain and serial communication library.
- MARK V: local Wi-Fi transport components selected from demonstrated needs.

This avoids learning several unfamiliar systems simultaneously and keeps failures attributable to the current milestone.

## MARK 0 Technical Model

A camera frame is a NumPy array. For a typical color frame, its shape is:

```text
(height, width, channels)
```

OpenCV commonly supplies three-channel camera pixels in BGR order rather than RGB. Each pixel is addressed by row and column, and each channel is usually an unsigned 8-bit integer from 0 through 255. Processing a frame means reading or transforming this numerical array—for example, cropping it, converting it to grayscale, resizing it, or drawing an overlay.

MARK 0 will teach this model before introducing hand-tracking abstractions.

## Decisions Deferred Until Needed

- Exact camera model and final camera placement.
- Final TV mirroring technology.
- Gesture vocabulary and conflict-resolution policy.
- ESP32 board variant, LED model, power budget, sensors, and servos.
- Wi-Fi protocol and message encoding.
- Packaging and auto-start strategy on Windows.

No purchase recommendation should be made before MARK II is complete.

