# lean-index-qft

Topic index for constructive QFT and mathematical physics formalization in Lean 4. **[How to use this index in your project](https://github.com/mrdouglasny/lean-index/blob/main/docs/use-topic-index.md)**

**67,382 topic-matched declarations** across **30 repositories** (scanned 41 repos, 71K declarations).

Tracks Lean declarations related to:
- **Functional analysis** (27,028 matches): Hilbert/Banach spaces, bounded/compact operators, Frechet derivatives
- **Measure theory** (22,216 matches): measure spaces, integration, Lebesgue/Borel measures, Radon-Nikodym
- **Probability theory** (5,634 matches): martingales, conditional expectation, Brownian motion, exchangeability
- **Topological groups** (5,224 matches): Haar measure, unitary groups, representations, locally compact groups
- **Operator algebras** (3,060 matches): C*-algebras, von Neumann algebras, star algebras
- **Spectral theory** (2,568 matches): spectrum, eigenvalues, resolvent, spectral measures
- **Distributions & Schwartz** (1,652 matches): Schwartz space, Fourier transforms, Sobolev spaces

See [SELECTION.md](SELECTION.md) for exact selection criteria. See [REPOS.md](REPOS.md) for all indexed repositories.

## Non-Mathlib Repos

| Repository | Topic Matches | Description |
|-----------|:---:|-------------|
| [SStarrySSky/Measure](https://github.com/SStarrySSky/Measure) | 1,812 | Measure theory formalization |
| [cameronfreer/exchangeability](https://github.com/cameronfreer/exchangeability) | 818 | Exchangeability, de Finetti's theorem |
| [teorth/analysis](https://github.com/teorth/analysis) | 626 | Tao's analysis formalization |
| [YellPika/quasi-borel-spaces](https://github.com/YellPika/quasi-borel-spaces) | 551 | Quasi-Borel spaces, categorical probability |
| [themathqueen/monlib4](https://github.com/themathqueen/monlib4) | 458 | Von Neumann algebras, quantum information |
| [ImperialCollegeLondon/FLT](https://github.com/ImperialCollegeLondon/FLT) | 334 | Fermat's Last Theorem (representation theory) |
| [mrdouglasny/OSforGFF](https://github.com/mrdouglasny/OSforGFF) | 318 | Osterwalder-Schrader for Gaussian free field |
| [suomela/fin-dep](https://github.com/suomela/fin-dep) | 284 | Finite dependent processes |
| [RemyDegenne/lean-bandits](https://github.com/RemyDegenne/lean-bandits) | 197 | Bandit algorithms, probability bounds |
| [Timeroot/Lean-QuantumInfo](https://github.com/Timeroot/Lean-QuantumInfo) | 196 | Quantum information theory |
| [kkytola/ExtremeValueProject](https://github.com/kkytola/ExtremeValueProject) | 130 | Extreme value theory |
| [oliver-butterley/SpectralThm](https://github.com/oliver-butterley/SpectralThm) | 103 | Spectral theorem formalization |
| [FredRaj3/SemicircleLaw](https://github.com/FredRaj3/SemicircleLaw) | 85 | Wigner semicircle law, random matrix theory |
| [or4nge19/MCMC](https://github.com/or4nge19/MCMC) | 79 | Markov chain Monte Carlo |
| [vbeffara/RMT4](https://github.com/vbeffara/RMT4) | 33 | Random matrix theory, complex analysis |
| [kkytola/VirasoroProject](https://github.com/kkytola/VirasoroProject) | 27 | Virasoro algebra, Verma modules |

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
