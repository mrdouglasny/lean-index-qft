# Selection Criteria

This document describes exactly which Lean declarations are included in this index. Only declarations matching at least one criterion below are indexed — everything else is excluded.

## Topic: operator-algebras

### Module prefixes (confidence: 1.0)
- `Mathlib.Analysis.CStarAlgebra` — C*-algebra theory
- `Mathlib.Analysis.VonNeumannAlgebra` — von Neumann algebras
- `Mathlib.Analysis.SpecialFunctions.ContinuousFunctionalCalculus` — functional calculus
- `Mathlib.Analysis.NormedSpace.Star.*` — star-normed spaces

### Type mentions (confidence: 0.8)
- `CStarAlgebra`, `VonNeumannAlgebra`
- `StarAlgebra`, `StarRing`
- `ContinuousFunctionalCalculus`, `NNSpectrumClass`

### Name patterns (confidence: 0.6)
- `.*CStar.*`, `.*VonNeumann.*`, `.*StarAlg.*`

## Topic: spectral-theory

### Module prefixes (confidence: 1.0)
- `Mathlib.Analysis.InnerProductSpace.Spectrum` — spectrum in inner product spaces
- `Mathlib.Analysis.NormedSpace.Spectrum` — spectrum in normed algebras
- `Mathlib.Analysis.CStarAlgebra.Spectrum` — spectrum in C*-algebras
- `Mathlib.FieldTheory.IsAlgClosed.Spectrum` — spectrum over algebraically closed fields
- `Mathlib.LinearAlgebra.Eigenspace.*` — eigenspaces

### Type mentions (confidence: 0.8)
- `Spectrum`, `IsEigenvalue`, `eigenspace`
- `HasEigenvalue`, `resolvent`

### Name patterns (confidence: 0.6)
- `.*Spectrum.*`, `.*Spectral.*`, `.*Eigen.*`, `.*Resolvent.*`

## Topic: functional-analysis

### Module prefixes (confidence: 1.0)
- `Mathlib.Analysis.InnerProductSpace.*` — Hilbert space theory
- `Mathlib.Analysis.NormedSpace.*` — Banach space theory
- `Mathlib.Analysis.Normed.*` — normed structures
- `Mathlib.Analysis.LocallyConvex.*` — locally convex spaces
- `Mathlib.Topology.Algebra.Module.*` — topological modules
- `Mathlib.Analysis.Calculus.*` — Frechet derivatives, calculus

### Type mentions (confidence: 0.8)
- `InnerProductSpace`, `NormedSpace`, `NormedAddCommGroup`
- `ContinuousLinearMap`, `ContinuousLinearEquiv`
- `IsBoundedLinearMap`, `UniformSpace`

### Name patterns (confidence: 0.6)
- `.*Hilbert.*`, `.*Banach.*`, `.*BoundedLinear.*`, `.*CompactOp.*`, `.*Frechet.*`

## Topic: measure-theory

### Module prefixes (confidence: 1.0)
- `Mathlib.MeasureTheory.*` — full measure theory

### Type mentions (confidence: 0.8)
- `MeasureSpace`, `MeasurableSpace`, `Measure`
- `Integrable`, `MeasureTheory.Integral`, `SignedMeasure`

### Name patterns (confidence: 0.6)
- `.*Measur.*`, `.*Integral.*`, `.*Borel.*`, `.*RadonNikodym.*`

## Topic: probability-theory

### Module prefixes (confidence: 1.0)
- `Mathlib.Probability.*` — probability theory

### Type mentions (confidence: 0.8)
- `ProbabilityMeasure`, `IsProbabilityMeasure`
- `Martingale`, `Submartingale`, `Supermartingale`
- `ConditionalExpectation`, `IndepFun`

### Name patterns (confidence: 0.6)
- `.*Martingale.*`, `.*Brownian.*`, `.*Gaussian.*`
- `.*Stochastic.*`, `.*Probability.*`, `.*Exchangeab.*`

## Topic: topological-groups

### Module prefixes (confidence: 1.0)
- `Mathlib.Topology.Algebra.Group.*` — topological groups
- `Mathlib.Topology.Algebra.ContinuousMonoidHom` — continuous homomorphisms
- `Mathlib.MeasureTheory.Measure.Haar.*` — Haar measure
- `Mathlib.Topology.Algebra.UniformGroup` — uniform groups
- `Mathlib.RepresentationTheory.*` — representation theory

### Type mentions (confidence: 0.8)
- `TopologicalGroup`, `ContinuousMul`, `LocallyCompactSpace`
- `IsHaarMeasure`, `UnitaryGroup`
- `Representation`, `GroupAlgebra`

### Name patterns (confidence: 0.6)
- `.*Haar.*`, `.*Unitary.*`, `.*Pontryagin.*`, `.*Representation.*`

## Topic: distributions-schwartz

### Module prefixes (confidence: 1.0)
- `Mathlib.Analysis.Distribution.*` — distribution theory
- `Mathlib.Analysis.SchwartzSpace` — Schwartz space
- `Mathlib.Analysis.Fourier.*` — Fourier analysis
- `Mathlib.Analysis.SpecialFunctions.Integrals` — special integrals

### Type mentions (confidence: 0.8)
- `SchwartzMap`, `Distribution`
- `FourierTransform`, `SobolevSpace`

### Name patterns (confidence: 0.6)
- `.*Schwartz.*`, `.*Fourier.*`, `.*Sobolev.*`, `.*Distribution.*`

---

## How selection works

1. **Mathlib declarations** are downloaded from the official docs cache (~384K total).
2. Each declaration is tested against the criteria above.
3. Only declarations matching **at least one criterion** from **any topic** are stored.
4. Confidence scores: **1.0** (module prefix) > **0.8** (type mention) > **0.6** (name pattern).

## Previewing changes

```bash
lean-index preview-topics                                    # current topics.yaml
lean-index preview-topics --config-file modified-topics.yaml # proposed changes
```
