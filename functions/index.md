# Functions

```{image} signal_path.svg
:width: 100%
:align: center
```

The signal is first splitted into 2 bands using the {guilabel}`XOVER` parameter. The lower band is not processed, allowing to preserve the bass content for more control.

The higher band then goes into a Low-pass filter which frequency is controlled with {guilabel}`LPF IN`. This allows to remove smoothly some harmonic content before new one is added in the distortion stage.

The distortion is selected using the {guilabel}`TYPE` parameter. 37 different distortions are available, ranging from wave shapers, wave folding, saturation, overdrive, fuzz, bit crushing and completely novel distortions including a fractal chaotic feedback equation, cyclic distortions, slew rate limiters, sample & hold analog emulation, noise based distortions, a ball bouncing on walls which velocity is controlled by the input signal, a fridge emulation or one based on Lorenz strange attractors.

Each distortion then has 3 variants using the {guilabel}`FAM` switch:

- {guilabel}`S`, "Standard" which is the raw algorithm
- {guilabel}`X`, "Xxx" which simulates a tube amp
- {guilabel}`O`, "Odd" which brings inharmonic distortions

The distortion can be further controlled using the {guilabel}`BIAS` and {guilabel}`MOD` parameters:

For {guilabel}`FAM` Standard and Xxx, the {guilabel}`BIAS` parameter emulates malfunctioning hardware circuirty and adds a DC offset before the distortion is applied. But don't worry, this DC offset is removed later in the signal path.

For {guilabel}`FAM` Odd, the {guilabel}`BIAS` parameter controls the distance between harmonics: normally a distortion harmonics are all multiplicative of the fundamental. {guilabel}`FAM` Odd allows to expand or shrink the relation between those harmonics, making it "inharmonic":
For example, if we consider a 100 Hz sinus input signal, and {guilabel}`BIAS` at the neutral position, the distortion would generate harmonics at multiples of 100 Hz as shown on the following diagram on the left.
If we turn the {guilabel}`BIAS` knob slightly on the right, the "harmonics" will expand but won't be multiplicative of the root frequency anymore. Note that the root frequency is preserved.

```{image} fam_o.svg
:width: 75%
:align: center
```

The {guilabel}`MOD` parameter is then specific for each distortion. For example it brings even harmonics for wave shapers, or change the base parameters of the algorithm itself.

Each distortion has of course a {guilabel}`GAIN` parameter from very low to extreme gain settings, with very low noise at extreme gain settings thanks to its clean audio analog circuitry.

Finally the distorted signal reaches another Low-pass filter which frequency is controlled with {guilabel}`LPF OUT`. This allows to "tame" the distortion by removing progressively the harmonics generated in the distortion stage.

In total, Ohmicide has 111 distinct sound possibilities, with {guilabel}`BIAS` and {guilabel}`MOD` for infinite number of variations.

The Ohmicide has an automatic gain staging which preserves on output the power of the input signal. This allows to play with the module without fearing the module would suddenly be extremely loud.

Every parameter can be CV controlled, and on top of that, {guilabel}`GAIN`, {guilabel}`MOD`, {guilabel}`BIAS` and {guilabel}`XOVER` also have attenuverters.
