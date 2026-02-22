# Selection Criteria

This document describes exactly which Mathlib declarations are included in this index. Only declarations matching at least one criterion below are indexed — everything else is excluded.

## Topic: operator-algebras

### Module prefixes (confidence: 1.0)
- `Mathlib.Analysis.CStarAlgebra` — C*-algebra theory
- `Mathlib.Analysis.VonNeumannAlgebra` — von Neumann algebras
- `Mathlib.Analysis.SpecialFunctions.ContinuousFunctionalCalculus` — functional calculus
- `Mathlib.Analysis.NormedSpace.Star.*` — star-normed spaces
- `Mathlib.Analysis.InnerProductSpace.Spectrum` — spectrum in inner product spaces

### Type mentions (confidence: 0.8)
- `CStarAlgebra`, `VonNeumannAlgebra`
- `StarAlgebra`, `StarRing`
- `Spectrum`, `ContinuousFunctionalCalculus`, `NNSpectrumClass`

### Name patterns (confidence: 0.6)
- `.*CStar.*`, `.*VonNeumann.*`, `.*Spectrum.*`, `.*StarAlg.*`

## Topic: functional-analysis

### Module prefixes (confidence: 1.0)
- `Mathlib.Analysis.InnerProductSpace.*` — Hilbert space theory
- `Mathlib.Analysis.NormedSpace.*` — Banach space theory
- `Mathlib.Analysis.Normed.*` — normed structures
- `Mathlib.Topology.Algebra.Module.LinearMap` — continuous linear maps
- `Mathlib.Analysis.LocallyConvex.*` — locally convex spaces

### Type mentions (confidence: 0.8)
- `InnerProductSpace`, `NormedSpace`, `NormedAddCommGroup`
- `ContinuousLinearMap`, `ContinuousLinearEquiv`
- `IsBoundedLinearMap`, `IsCompact`, `Hilbert`

### Name patterns (confidence: 0.6)
- `.*Hilbert.*`, `.*Banach.*`, `.*BoundedLinear.*`, `.*CompactOp.*`

## Topic: measure-theory

### Module prefixes (confidence: 1.0)
- `Mathlib.MeasureTheory.*` — full measure theory
- `Mathlib.Probability.*` — probability theory

### Type mentions (confidence: 0.8)
- `MeasureSpace`, `MeasurableSpace`, `Measure`
- `ProbabilityMeasure`, `GaussianMeasure`
- `Integrable`, `MeasureTheory.Integral`

### Name patterns (confidence: 0.6)
- `.*Measur.*`, `.*Integral.*`, `.*Borel.*`

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
