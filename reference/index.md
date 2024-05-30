# References

## Menus Reference

```{image} menus.svg
:width: 100%
:align: center
```


## Distortion Reference

| **Distortion** | **{guilabel}`MOD`** | **{guilabel}`BIAS`** | **Description** |
| ------------------- |:--------:| :------:| -------------- |
| Disto   | • | • | It has a nice analog feel. The brightness of the distortion is controllable. |
| SftClp  | • | • | Waveshaper, symmetrical and soft. {guilabel}`MOD` will make it asymmetric. |
| HardClp | • | • | Waveshaper, symmetrical and harder. {guilabel}`MOD` will make it asymmetric. |
| StrgrC	 | • | • | Waveshaper, symmetrical and stronger. {guilabel}`MOD` will make it asymmetric. |
| Crest	 | • | • | Waveshaper, symmetrical, and not bijective. {guilabel}`MOD` will make it asymmetric. |
| Fezz	 | • | • | Waveshaper asymmetrical. |
| Fuss	 | • | • | Waveshaper asymmetrical. |
| Attrac	 | • | • | Multiple states distortion. |
| SmartE	 | • | • | Varying waveshape. Use {guilabel}`MOD` to change the waveshape. |
| Sstrgi	 | • | • | Waveshaper with ripples. |
| WavFld	 | • | • | Wavefolding	Cyclic waveshaper. High gain will produce ”tuned” noise. |
| NoizE	 |   | • | Cyclic distortion. High gain will produce white noise. |
| Antipol | • | • | Crest mangler. {guilabel}`MOD` to 50% will be similar to a hardclip. More than 50% will reverse the crest. |
| Anti+	 | • | • | Same as antipole, with an additional waveshaper on the crests. |
| Cross	 | • | • | Waveshaper that affects the low portion of the signal. |
| Cubic	 |   | • | Waveshaper. Will ‘dry’ the signal. |
| Vshpe	 | • | • | Will tend to produce a higher pitched sound. |
| Square	 |   | • | Waveshaped rectifier. Will tend to dry the signal much more than Rectifier. |
| Lowfi	 | • |   | Slew rate limiter. This is an extreme version of a physical limitation that exists on any amplifier. {guilabel}`MOD` will change the slew rate limit, raising it will give more highs. |
| Lowrfi	 | • | • | Waveshaped slew rate distortion. |
| BrwnNz	 | • |   | Random walk on a waveshaper. {guilabel}`MOD` at 0 will create noise. |
| Filter	 | • | • | Waveshaper followed by a resonator low pass filter. The higher the distortion gain, the higher the resonance. {guilabel}`MOD` will change the cutoff frequency. |
| DwnSpl	 | • | • | Emulates an analogue sample & hold. {guilabel}`MOD` will change the hold time. | 
| Bitcrsh | • | • | Crushes the bit resolution of the signal. May oscillate when used in the Xxx mode. |
| Jelly	 | • | • | Enveloppe Follower driven Distortion. |
| Fractl	 | • | • | Uses a chaotic feedback equation to distort the sound. A bit experimental, pretty weird and analogue sounding. {guilabel}`MOD` will change the recursivity depth. Use some {guilabel}`BIAS` to make it unstable. |
| Accum	 | • |   | A distortion that can add low frequencies! It behaves a bit like a modulator, but it’s not. Experimental, nice on drums particularly. |
| TimeFr	 | • | • | Freezes portions of the audio signal depending on the {guilabel}`BIAS`, {guilabel}`MOD` and {guilabel}`GAIN`. |
| Clicks	 | • | • | Adds Vinyl clicks, with a click density depending on the {guilabel}`MOD` parameter. |
| ChastB	 | • | • | A floating point mantissa distortion. |
| SuspB	 |   | • | A floating point exponent distortion. |
| VariWS	 | • | • | Variable asymmetrical waveshaper. |
| Vinyl	 |   |   | Features RIAA filters, used in vinyl signal encoding/decoding, and an emulation of stylus degradation. |
| Vynil	 |   | • | Based on the same principles as Hip. |
| Bounce	 | • | • | Emulate the behaviour of a ball in a cylinder where the top and bottom move accordingly to the sound. The {guilabel}`MOD` varies the ball inertia. |
| Zippy	 | • | • | Distortion using a chaotic oscillator. The {guilabel}`MOD` varies the oscillator frequency. |
| Valve	 | • | • | Asymmetrical soft distortion. Produces even order harmonics which reduce when {guilabel}`MOD` rises, resulting in a brighter sound. |
