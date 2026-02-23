# lean-index-qft

Topical index for constructive QFT and mathematical physics formalization in Lean 4. **[How to use this index in your project](https://github.com/mrdouglasny/lean-index/blob/main/docs/use-topic-index.md)**

**62,172 topic-matched declarations** across **31 repositories** (scanned 42 repos, 78,615 declarations).

Tracks Lean declarations related to:
- **Functional analysis**: Hilbert/Banach spaces, bounded/compact operators, Frechet derivatives
- **Measure theory**: measure spaces, integration, Lebesgue/Borel measures, Radon-Nikodym
- **Quantum field theory**: Wick's theorem, perturbation theory, Feynman diagrams, Standard Model, Lorentz group
- **Probability theory**: martingales, conditional expectation, Brownian motion, exchangeability
- **Topological groups**: Haar measure, unitary groups, representations, locally compact groups
- **Operator algebras**: C*-algebras, von Neumann algebras, star algebras
- **Spectral theory**: spectrum, eigenvalues, resolvent, spectral measures
- **Distributions & Schwartz**: Schwartz space, Fourier transforms, Sobolev spaces

See [SELECTION.md](SELECTION.md) for exact selection criteria. See [REPOS.md](REPOS.md) for all indexed repositories.

## Indexed Repos

| Repository | Topic Matches | Description |
|-----------|:---:|-------------|
| [leanprover-community/mathlib4](https://github.com/leanprover-community/mathlib4) | 49,315 | The math library for Lean 4 (indexed via cache, not cloned) |
| [lean-phys-community/PhysLean](https://github.com/lean-phys-community/PhysLean) | 6,461 |  |
| [SStarrySSky/Measure](https://github.com/SStarrySSky/Measure) | 1,812 | 📏 A dependently-typed language on Lean 4 for formalizing physics. Dimensions,... |
| [cameronfreer/exchangeability](https://github.com/cameronfreer/exchangeability) | 818 | Exchangeability, de Finetti's theorem |
| [teorth/analysis](https://github.com/teorth/analysis) | 626 | Tao's analysis formalization |
| [YellPika/quasi-borel-spaces](https://github.com/YellPika/quasi-borel-spaces) | 551 | Quasi-Borel spaces, categorical probability |
| [themathqueen/monlib4](https://github.com/themathqueen/monlib4) | 458 | Von Neumann algebras, quantum information theory |
| [ImperialCollegeLondon/FLT](https://github.com/ImperialCollegeLondon/FLT) | 334 | Fermat's Last Theorem (uses representation theory) |
| [mrdouglasny/OSforGFF](https://github.com/mrdouglasny/OSforGFF) | 318 | Osterwalder-Schrader axioms for Gaussian free field |
| [suomela/fin-dep](https://github.com/suomela/fin-dep) | 284 | Finitely dependent distributions |
| [RemyDegenne/lean-bandits](https://github.com/RemyDegenne/lean-bandits) | 197 | Bandit algorithms, probability bounds |
| [Timeroot/Lean-QuantumInfo](https://github.com/Timeroot/Lean-QuantumInfo) | 196 | Quantum information theory, quantum channels |
| [kkytola/ExtremeValueProject](https://github.com/kkytola/ExtremeValueProject) | 130 | Extreme value theory |
| [JustinMcClung/formal-distribution](https://github.com/JustinMcClung/formal-distribution) | 105 | Lean 4 formalization of Section 1 - Formal Calculus from Nozaradan's... |
| [oliver-butterley/SpectralThm](https://github.com/oliver-butterley/SpectralThm) | 103 | Spectral theorem formalization |
| [FredRaj3/SemicircleLaw](https://github.com/FredRaj3/SemicircleLaw) | 85 | Wigner semicircle law, random matrix theory |
| [or4nge19/MCMC](https://github.com/or4nge19/MCMC) | 79 | Markov chain Monte Carlo |
| [kebekus/ProjectVD](https://github.com/kebekus/ProjectVD) | 50 | Formalizing Value Distribution Theory |
| [leanprover/SampCert](https://github.com/leanprover/SampCert) | 49 | Certified differential privacy sampling |
| [girving/ray](https://github.com/girving/ray) | 47 | Analytic number theory, special functions |
| [vbeffara/RMT4](https://github.com/vbeffara/RMT4) | 33 | Random matrix theory, complex analysis |
| [kkytola/VirasoroProject](https://github.com/kkytola/VirasoroProject) | 27 | Virasoro algebra, Verma modules, conformal field theory |
| [lua-vr/pointwise-birkhoff](https://github.com/lua-vr/pointwise-birkhoff) | 19 | Birkhoff ergodic theorem |
| [alexjgreig/QHL-Lean](https://github.com/alexjgreig/QHL-Lean) | 18 | Quantum Hoare logic |
| [verified-optimization/CvxLean](https://github.com/verified-optimization/CvxLean) | 16 | Convex optimization, functional analysis |
| [girving/interval](https://github.com/girving/interval) | 10 | Interval arithmetic, rigorous numerics |
| [sunoru/finite-groups](https://github.com/sunoru/finite-groups) | 9 | Finite group theory |
| [awodey/joyal](https://github.com/awodey/joyal) | 8 |  |
| [formalproofs/probability](https://github.com/formalproofs/probability) | 8 | Probability theory fundamentals |
| [girving/series](https://github.com/girving/series) | 4 | Power series, analytic functions |
| [Axiomatic-AI/lean-qkd](https://github.com/Axiomatic-AI/lean-qkd) | 2 | Lean blueprint a result in quantum key distribution |

## Usage

### As a consumer

```bash
pip install git+https://github.com/mrdouglasny/lean-index.git
lean-index fetch-db mrdouglasny/lean-index-qft
lean-index search "spectral theorem"
lean-index search --kind theorem --topic probability-theory
lean-index stats
```

### Building locally

```bash
pip install git+https://github.com/mrdouglasny/lean-index.git
cd lean-index-qft
lean-index init                # Downloads Mathlib cache + creates topic-filtered DB
lean-index update              # Discovers repos + indexes + matches topics
lean-index stats
lean-index preview-topics      # Estimate impact of changing topics.yaml
```

## CI

The database is rebuilt weekly and published as a GitHub release. Download the latest with:

```bash
lean-index fetch-db mrdouglasny/lean-index-qft
```
