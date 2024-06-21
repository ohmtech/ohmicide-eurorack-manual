# References

## Menus Reference

```{image} menus.svg
:width: 100%
:align: center
```


## Distortion Quick Reference

| **Distortion** | **{guilabel}`MOD`** | **{guilabel}`BIAS`** | **Description** |
| ------------------- |:--------:| :------:| -------------- |
| [Disto](#disto)       | • | • | It has a nice analog feel. The brightness of the distortion is controllable. |
| [SftClp](#sftclp)     | • | • | Waveshaper, symmetrical and soft. {guilabel}`MOD` will make it asymmetric. |
| [HardClp](#hardclp)   | • | • | Waveshaper, symmetrical and harder. {guilabel}`MOD` will make it asymmetric. |
| [StrgrC](#strgrc)     | • | • | Waveshaper, symmetrical and stronger. {guilabel}`MOD` will make it asymmetric. |
| [Crest](#crest)       | • | • | Waveshaper, symmetrical, and not bijective. {guilabel}`MOD` will make it asymmetric. |
| [Fezz](#fezz)         | • | • | Waveshaper asymmetrical. |
| [Fuss](#fuss)         | • | • | Waveshaper asymmetrical. |
| [Attrac](#attrac)     | • | • | Multiple states distortion. |
| [SmartE](#smarte)     | • | • | Varying waveshape. Use {guilabel}`MOD` to change the waveshape. |
| [Sstrgi](#sstrgi)     | • | • | Waveshaper with ripples. |
| [WavFld](#wavfld)     | • | • | Wavefolding	Cyclic waveshaper. High gain will produce ”tuned” noise. |
| [NoizE](#noize)       |   | • | Cyclic distortion. High gain will produce white noise. |
| [Antipol](#antipol)   | • | • | Crest mangler. {guilabel}`MOD` to 50% will be similar to a **HardClp**. More than 50% will reverse the crest. |
| [Anti+](#anti)        | • | • | Same as antipole, with an additional waveshaper on the crests. |
| [Cross](#cross)       | • | • | Waveshaper that affects the low portion of the signal. |
| [Cubic](#cubic)       |   | • | Waveshaper. Will ‘dry’ the signal. |
| [Vshpe](#vshpe)       | • | • | Will tend to produce a higher pitched sound. |
| [Square](#square)     |   | • | Waveshaped rectifier. Will tend to dry the signal much more than **Vshpe**. |
| [Lowfi](#lowfi)       | • |   | Slew rate limiter. This is an extreme version of a physical limitation that exists on any amplifier. {guilabel}`MOD` will change the slew rate limit, raising it will give more highs. |
| [Lowrfi](#lowrfi)     | • | • | Waveshaped slew rate distortion. |
| [BrwnNz](#brwnnz)     | • |   | Random walk on a waveshaper. {guilabel}`MOD` at 0 will create noise. |
| [Filter](#filter)     | • | • | Waveshaper followed by a resonator low pass filter. The higher the distortion gain, the higher the resonance. {guilabel}`MOD` will change the cutoff frequency. |
| [DwnSpl](#dwnspl)     | • | • | Emulates an analogue sample & hold. {guilabel}`MOD` will change the hold time. | 
| [Bitcrsh](#bitcrsh)   | • | • | Crushes the bit resolution of the signal. May oscillate when used in the Xxx mode. |
| [Jelly](#jelly)       | • | • | Envelope follower driven Distortion. |
| [Fractl](#fractl)     | • | • | Uses a chaotic feedback equation to distort the sound. A bit experimental, pretty weird and analogue sounding. {guilabel}`MOD` will change the recursive depth. Use some {guilabel}`BIAS` to make it unstable. |
| [Accum](#accum)       | • |   | A distortion that can add low frequencies! It behaves a bit like a modulator, but it’s not. Experimental, nice on drums particularly. |
| [TimeFr](#timefr)     | • | • | Freezes portions of the audio signal depending on the {guilabel}`BIAS`, {guilabel}`MOD` and {guilabel}`GAIN`. |
| [Clicks](#clicks)     | • | • | Adds Vinyl clicks, with a click density depending on the {guilabel}`MOD` parameter. |
| [ChastB](#chastb)     | • | • | A floating point mantissa distortion. |
| [SuspB](#suspb)       |   | • | A floating point exponent distortion. |
| [VariWS](#variws)     | • | • | Variable asymmetrical waveshaper. |
| [Vinyl](#vinyl)       |   |   | Features RIAA filters, used in vinyl signal encoding/decoding, and an emulation of stylus degradation. |
| [Vynil](#vynil)       |   | • | Based on the same principles as Vinyl. |
| [Bounce](#bounce)     | • | • | Emulate the behavior of a ball in a cylinder where the top and bottom move accordingly to the sound. The {guilabel}`MOD` varies the ball inertia. |
| [Zippy](#zippy)       | • | • | Distortion using a chaotic oscillator. The {guilabel}`MOD` varies the oscillator frequency. |
| [Valve](#valve)       | • | • | Asymmetrical soft distortion. Produces even order harmonics which reduce when {guilabel}`MOD` rises, resulting in a brighter sound. |


## Distortion Reference

### {guilabel}`FAM`

When {guilabel}`FAM` is on {guilabel}`S` or {guilabel}`X`, after the band processing stage ({guilabel}`XOVER` and {guilabel}`LPF IN`), and except where otherwise noted, the signal is offset by {guilabel}`BIAS` and then {guilabel}`GAIN` (pregain) is applied before the signal enters the distortion. The DC offset introduced by the {guilabel}`BIAS` offset is then compensated.

When {guilabel}`FAM` is on {guilabel}`O`, {guilabel}`BIAS` is used instead to expand or shrink the relation between harmonics generated by the distortion.

There is one exception though for **Fractl**, when {guilabel}`FAM` is on {guilabel}`O`: {guilabel}`BIAS` will control the DC offset (instead of the relation between harmonics), and {guilabel}`MOD` is used instead to control the relation between harmonics generated by the distortion.

### Disto

**Disto** is a limiter where the {guilabel}`MOD` parameter controls the attack and release time, giving an analog feeling. Increasing {guilabel}`MOD` will reduce the attack and release time from a few milliseconds to a few hundreds of microseconds.

### SftClp

**SftClp** is a soft log-shaped waveshaper symmetric curve. Increasing the {guilabel}`MOD` parameter control will make it asymmetric, bringing even harmonic and a warmer, richer sound.

Even though the asymmetry of the waveshaper when using {guilabel}`MOD` implicitly creates a DC offset, the DC offset is compensated later in the algorithm. This is also the case for all the following waveshapers.

The diagram below shows **SftClp** shapes. The plain line is for {guilabel}`MOD` turned fully left, and the shaded lines are examples as {guilabel}`MOD` is turned right.

```{image} SftClp.svg
:width: 75%
:align: center
```

### HardClp

Same as **SftClp**, but with a harder inverse-shaped curve.

```{image} HardClp.svg
:width: 75%
:align: center
```

### StrgrC

Same as **SftClp**, but with a stronger tangent-inverse-shaped curve.

```{image} StrgrC.svg
:width: 75%
:align: center
```

### Crest

**Crest** is a non-bijective waveshaper symmetric curve behaving a bit like a wavefolder around the clipping region. Increasing the {guilabel}`MOD` parameter control will make it asymmetric, bringing even harmonic and a warmer, richer sound.

```{image} Crest.svg
:width: 75%
:align: center
```

### Fezz

**Fezz** is a waveshaper but with an asymmetric curve. Increasing the {guilabel}`MOD` parameter control will push further the asymmetry for a richer sound.

```{image} Fezz.svg
:width: 75%
:align: center
```

### Fuss

Same as **Fuss**, but with a different asymmetric curve, with a "folding" similar to **Crest** in the positive values of the input signal.

```{image} Fuss.svg
:width: 75%
:align: center
```

### Attrac

**Attrac** is a multiple states distortion: at low {guilabel}`GAIN` settings, the current signal voltage is "attracted" to either -5V or 5V, like an electron steered by the two deflection plates of a cathode-ray tube. As the {guilabel}`GAIN` parameter is raised, the attractor enters a more chaotic behavior.

The {guilabel}`MOD` parameter controls the attack and release time of an envelope follower of the input signal, which in turn restrain the chaotic response.

```{note}
As a consequence, if the input signal doesn't have fast enough variations of volume (such as a plain VCO output), {guilabel}`MOD` will have no effect.
```

### SmartE

**SmartE** is a waveshaper with a varying shape. The {guilabel}`MOD` parameter controls the shape of the waveshaper.

```{image} SmartE.svg
:width: 75%
:align: center
```

### Sstrgi

**Sstrgi** is a non-bijective waveshaper symmetric curve with multiple wave folds. Increasing the {guilabel}`MOD` parameter control will make it asymmetric, bringing even harmonic and a warmer, richer sound.

```{image} Sstrgi.svg
:width: 75%
:align: center
```

### WavFld

**WavFld** is a textbook implementation of a puncher (sinus-based) wavefolder. Increasing the {guilabel}`MOD` parameter control will give a new take of this classic.

```{image} WavFld.svg
:width: 75%
:align: center
```

### NoizE

**NoizE** is an implementation of a cyclic triangular wavefolder. Increasing the {guilabel}`GAIN` parameter control will make the output signal more and more noisy. The {guilabel}`MOD` parameter is inactive.

```{image} NoizE.svg
:width: 75%
:align: center
```

### Antipol

**Antipol** is an implementation of a hard clipper. Increasing the {guilabel}`GAIN` and {guilabel}`MOD` parameters controls can make the output signal fold on itself.

```{image} Antipol.svg
:width: 75%
:align: center
```

### Anti+

Same as **Antipol**, but the output signal will fold quicker when hard clipping and increasing the {guilabel}`MOD` parameter control.

```{image} Anti+.svg
:width: 75%
:align: center
```

### Cross

**Cross** is a soft non-bijective waveshaper symmetric curve behaving a bit like a wavefolder around the clipping region. Increasing the {guilabel}`MOD` parameter control will make it asymmetric, bringing even harmonic and a warmer, richer sound.

```{image} Cross.svg
:width: 75%
:align: center
```

### Cubic

**Cubic** is a non-standard symmetric waveshaper curve crushing the low part of the signal. The {guilabel}`MOD` parameter is inactive.

```{image} Cubic.svg
:width: 75%
:align: center
```

### Vshpe

**Vshpe** is a non-standard anti-symmetric waveshaper curve with a V-shape. Increasing the {guilabel}`MOD` parameter control will make it asymmetric, bringing even harmonic and a warmer, richer sound.

```{image} Vshpe.svg
:width: 75%
:align: center
```

### Square

**Square** is a non-standard anti-symmetric waveshaper curve with a U-shape.

```{image} Square.svg
:width: 75%
:align: center
```

### Lowfi

**Lowfi** simulates an operational amplifier integrated circuit with a non-Hi-Fi slew rate, bringing a Lo-Fi type of sound. The lowest {guilabel}`MOD` is, the lowest the slew rate, and the more Lo-Fi it sounds.

### Lowrfi

Same as **Lowfi**, but the operational amplifier integrated circuit also shows strong non-linear properties.

### BrwnNz

**BrwnNz** is a [Brownian noise](https://en.wikipedia.org/wiki/Brownian_noise) or "Random Walk" applied on the input signal. The {guilabel}`MOD` parameter controls the sampling rate of the input signal. The lowest it is, the most it appears as a pure brown noise.

### Filter

**Filter** is a waveshaper followed by a low-pass resonant filter. Increasing the {guilabel}`GAIN` parameter control will make the resonance higher, and the {guilabel}`MOD` parameter controls the low-pass cutoff frequency.

### DwnSpl

**DwnSpl** emulates an analog sample & hold filter with an integrated polynomial band-limited step function combined with a waveshaper. The {guilabel}`MOD` parameter controls the sampling frequency rate. This distortions allows to replicate the effect of vintage digital synthesizers with low sampling rates.

### Bitcrsh

**Bitcrsh** is a typical bitcrusher. Increasing the {guilabel}`MOD` parameter control makes the effect more intense, and so lower the number of bits used to represent the input signal.

### Jelly

**Jelly** is a distortion that can't be described with human words. The algorithm is also a total non-sense and yet, here it is.

### Fractl

**Fractl** is a fractal-based distortion model. Increasing the {guilabel}`MOD` parameter control sets the number of passes of its recursive algorithm.

```{note}
However when {guilabel}`FAM` type is {guilabel}`O`, {guilabel}`BIAS` will control the DC offset (instead of the harmonics tuning) and {guilabel}`MOD` will control the harmonics tuning (instead of the number of passes of the algorithm).
```

### Accum

**Accum** is an experimental distortion that acts like a modulator somehow, but not really.

### TimeFr

**TimeFr** is a delay line that "time-freezes" the input signal, based on an envelope follower. The {guilabel}`MOD` parameter controls the analysis time of that envelope follower.

### Clicks

**Clicks** adds Vinyl clicks. Increasing the {guilabel}`MOD` parameter control will increase the click density.

### ChastB

**ChastB** is an experimental bit-fiddling [floating point mantissa](https://en.wikipedia.org/wiki/Floating-point_arithmetic) digital distortion.

### SuspB

**SuspB** is a experimental bit-fiddling [floating point exponent](https://en.wikipedia.org/wiki/Floating-point_arithmetic) digital distortion.

### VariWS

**VariWS** is an asymmetrical waveshaper with a varying shape. The {guilabel}`MOD` parameter controls the shape of the waveshaper.

```{image} VariWS.svg
:width: 75%
:align: center
```

### Vinyl

**Vinyl** uses the pre-emphasis and complement de-emphasis [RIAA equalization curves](https://en.wikipedia.org/wiki/RIAA_equalization) with soft asymmetrical waveshapers to model non-linearities of the stylus. The {guilabel}`MOD` parameter emulates the stylus degradation over time. 

### Vynil

**Vynil** is a variation of **Vinyl** with a different topology for handling the DC offset implicitly generated by the RIAA equalization curves.

### Bounce

**Bounce** emulates the behavior of a ball in a cylinder where the top and bottom move accordingly to the signal input. The {guilabel}`MOD` parameter controls the gravity of the system and the air friction to limit the ball speed for stability.

### Zippy

**Zippy** is an original distortion based on [Lorenz attractors](https://en.wikipedia.org/wiki/Lorenz_system) with a 1-dimensional projection. Increasing the {guilabel}`MOD` parameter control will make the output signal more chaotic, and so more bright.

### Valve

**Valve** is a soft hyperbolic-tangent-shaped waveshaper symmetric curve. Increasing the {guilabel}`MOD` parameter control will make it asymmetric, bringing even harmonic and a warmer, richer sound.

```{image} Valve.svg
:width: 75%
:align: center
```
