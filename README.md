# lean-index-qft

Topic index for constructive QFT formalization in Lean 4.

Tracks Lean declarations related to:
- **Operator algebras**: C*-algebras, von Neumann algebras, spectral theory
- **Functional analysis**: Hilbert/Banach spaces, bounded/compact operators
- **Measure theory**: measure spaces, integration, probability measures
- **Distributions & Schwartz**: Schwartz space, Fourier transforms, Sobolev spaces

See [SELECTION.md](SELECTION.md) for exact selection criteria.

## Usage

```bash
pip install git+https://github.com/mrdouglasny/lean-index.git
cd lean-index-qft
lean-index init      # Downloads Mathlib cache + creates topic-filtered DB
lean-index search "C*-algebra"
lean-index search --topic operator-algebras --kind theorem
lean-index stats
lean-index preview-topics   # Show match counts before changing topics
```
