# Factory Mode

Depending on electrical conditions or ambiant temperature, your module CV and knobs might be slightly off and might require recalibration.

Also, should you have a problem with the module, our support team will ask you to run "test mode" to have a rough idea of what the problem is.

This operation requires a bit of care because the module will need to be powered by your Eurorack case in order to complete successfully. You will also need a simple LFO and VCO.

To enter test mode and calibration:

1. Turn off your Eurorack system
1. Remove all the Eurorack patch cables connected to the module
1. Remove the module from the rack (but keep its power cord attached)
1. Place the module on a non-conductive surface
1. Press the {guilabel}`FLASH` button at the back of the module, keep it pressed, and turn on your Eurorack system. The test mode welcome screen will appear
1. Press {guilabel}`TYPE`, the screen will turn entirely red. Check that the screen is working properly, and press {guilabel}`TYPE` again
1. Check that the {guilabel}`MOD` LED is blinking, press {guilabel}`TYPE`
1. Check that the {guilabel}`BIAS` LED is blinking, press {guilabel}`TYPE`
1. Turn {guilabel}`TYPE` 10 times on the left, then 10 times on the right
1. Put the {guilabel}`FAM` switch to {guilabel}`S`, then {guilabel}`X` and then {guilabel}`O`
1. Turn the {guilabel}`GAIN` knob fully on the left, then fully on the right, then press {guilabel}`TYPE`
1. Repeat the previous step for the {guilabel}`XOVER`, {guilabel}`MOD`, {guilabel}`BIAS`, {guilabel}`LPF IN`, {guilabel}`LPF OUT` knobs, and then for the {guilabel}`GAIN`, {guilabel}`MOD`, {guilabel}`BIAS` and {guilabel}`XOVER` trims.
1. Acknowledge that you have already removed all patch cables and press {guilabel}`TYPE`
1. Wait until the module calibrates CVs automatically, then press {guilabel}`TYPE`
1. Use your LFO in sinus mode and connect it to the {guilabel}`GAIN` CV
1. Repeat the previous step for {guilabel}`MOD`, {guilabel}`LPF IN`, {guilabel}`LPF OUT`, {guilabel}`BIAS`, {guilabel}`XOVER`, {guilabel}`TYPE` and {guilabel}`FAM` CVs
1. Use your VCO in sinus mode and connect it to the **right** input {guilabel}`IN` first
1. Repeat the previous step with the left input {guilabel}`IN`
1. Connect a patch cable from {guilabel}`OUT` left to your audio output and make sure a 440Hz tone is playing, press {guilabel}`TYPE`
1. Repeat the previous step with {guilabel}`OUT` right
1. The "QC passed" stamp appears, which means that your module is in specs (no problem were found) and calibration is complete
1. Turn off your Eurorack system, and reinstall the module into your rack
1. Turn on your Eurorack system
