# A.R.C. Room Hub Learning Log

Use this file to capture understanding, evidence, and the next small step. Entries should describe concepts in the learner's own words rather than merely listing completed commands.

## Current Position

- Active milestone: MARK 0 — Camera and Frame Fundamentals
- Current topic: Python 3.11 environment and camera-frame representation
- Status: Mac environment inspected; Python 3.11 setup not started

## What I Learned

- A camera frame will be handled as a NumPy array.
- A typical color frame has dimensions `(height, width, channels)`.
- OpenCV commonly represents three-channel images in BGR channel order.
- Pixel channels are commonly unsigned 8-bit values between 0 and 255.
- Camera images must remain local and ephemeral by default in this project.

## What I Practiced

- Inspected the machine architecture and available Python commands without changing the system.

## Evidence

- Machine architecture: `arm64`.
- macOS version: `26.6.2`.
- Homebrew executable: `/opt/homebrew/bin/brew`.
- Active `python3`: CPython `3.14.5` at `/opt/homebrew/opt/python@3.14/bin/python3.14`.
- `python3.11`: not currently installed.
- Available Homebrew Python 3.11 formula at inspection time: `3.11.16`.

## Questions or Unclear Points

- To be completed by the learner during the first frame exercise.

## Next Small Step

Understand the difference between the Python interpreter and a virtual environment. Then install Homebrew Python 3.11 without replacing the existing Python 3.14.

## Entry Template

Copy this section after each meaningful learning checkpoint:

```text
### YYYY-MM-DD — Topic

What I learned:

What I practiced:

What worked:

What did not work or remains unclear:

Evidence:

Next small step:
```
