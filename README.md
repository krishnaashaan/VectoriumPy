# VectoriumPy
![License](https://img.shields.io/github/license/krishnaashaan/vectoriumPy)
![Physics](https://img.shields.io/badge/Physics-Powered-red)
![NumPy](https://img.shields.io/badge/Numpy-Used-blue)


<p align="center">
  <img src="VectoriumPy/Logo/Vectorium_logo.png" width="500" alt="Vectorium logo">
</p>

VectoriumPy is a small, modular Python library of common physics formulas, helpers, and lightweight simulation utilities aimed at education, quick calculations, and small-scale experiments.

Project status: This repository contains the result of an intensive one-month development effort to gather, implement, and test compact physics utilities and examples. The codebase was created and refined over a single month with the goal of providing clear, well-tested helpers for teaching and experimentation.

I plan to add way more functions in the future

## Quick summary

- Lightweight functions for kinematics, forces, energy, electricity, waves, and example scripts.
- Well-suited for notebooks, teaching demos, and short scripts — not a full physics engine.

## Install
IT should be avaliable to install in a couple of Months
Install editable from source:

```bash
pip install -e .
```

Recommended: create and activate a virtual environment before installing.

## Usage (quick)

Run the example scripts or import modules from the package. Example from a Python REPL:

```python
from vectoriumPy.Kinematics.motion import avg_velocity
avg_v = avg_velocity(50, 50)
print(avg_v)
```

See [src/vectoriumPy/examples/examples.py](src/vectoriumPy/examples/examples.py) for runnable examples.

## Project layout

- [src/vectoriumPy/](src/vectoriumPy/)
  - `Kinematics/` — motion and projectile utilities
  - `Force/` — force-related formulas (gravity, friction, centripetal)
  - `Energy/` — kinetic, potential and mechanical energy helpers
  - `Electricity/` — circuits, capacitance, electric field helpers
  - `Waves/` — basic light and sound calculations
  - `Thermodynamics/` — calculations related to thermodynamics
  - `Magnetism/`- calculations related to magnetic fields 
  - `examples/` — small runnable examples showing common usage
  - `Tests/` — unit tests for core functions

## Tests

Run tests with pytest from the repository root:

```bash
python -m pytest -q
```

## Contributing

Contributions are welcome. Suggested workflow:

1. Fork the repo and create a feature branch.
2. Add tests for new functions under [src/vectoriumPy/Tests](src/vectoriumPy/Tests).
3. Open a PR with a clear description of changes.

## License

See [LICENSE](LICENSE) for license terms.

## Files explained (key modules)

This project contains a set of focused modules. Brief descriptions of the main files:

- [src/vectoriumPy/Kinematics/motion.py](src/vectoriumPy/Kinematics/motion.py): Common kinematics helpers (velocity, acceleration, displacement calculations).
- [src/vectoriumPy/Kinematics/projectile_motion.py](src/vectoriumPy/Kinematics/projectile_motion.py): Projectile motion utilities (range, time of flight, max height).
- [src/vectoriumPy/Force/Force.py](src/vectoriumPy/Force/Force.py): Force calculations (gravitational force, friction, centripetal force).
- [src/vectoriumPy/Energy/energy.py](src/vectoriumPy/Energy/energy.py): Energy-related helpers (kinetic, potential, mechanical energy, work, power).
- [src/vectoriumPy/Electricity/electricity.py](src/vectoriumPy/Electricity/electricity.py): Basic electricity formulas (Ohm's law, power, energy in circuits).
- [src/vectoriumPy/Electricity/circuit.py](src/vectoriumPy/Electricity/circuit.py): Series/parallel resistance and simple circuit helpers.
- [src/vectoriumPy/Electricity/electric_fields.py](src/vectoriumPy/Electricity/electric_fields.py): Electric field and point-charge helpers.
- [src/vectoriumPy/Waves/light.py](src/vectoriumPy/Waves/light.py): Light/wave optics helpers (wavelength, frequency relations).
- [src/vectoriumPy/Waves/sound.py](src/vectoriumPy/Waves/sound.py): Sound-wave calculations (speed, Doppler shift basics).
- [src/vectoriumPy/Thermodynamics/Thermodynamics.py](src/vectoriumPy/Thermodynamics/Thermodynamics.py): Calculations related to thermodynamics (First Law, Entropy, Enthalpy, Gibbs, Helmholtz, Ideal Gas Law).
- [src/vectoriumPy/examples/examples.py](src/vectoriumPy/examples/examples.py): Small example scripts demonstrating library usage.
- [src/vectoriumPy/Tests/](src/vectoriumPy/Tests/): Unit tests covering core functions.
