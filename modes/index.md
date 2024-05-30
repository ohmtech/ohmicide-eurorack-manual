# Running Modes

Ohmicide has 4 distinct running modes.

## Producer Mode

```{image} producer.png
:align: left
```

The **Producer** mode, the default when the module is switched on, is typically used at home or in the studio. No menu diving, and every change of parameter is instant. This allows for example to cycle through the entire list of distortions {guilabel}`TYPE` by just turning the encoder, letting one to "dial-in" the perfect distortion for the input sound quickly.

## Performer Modes

```{image} performer.png
:align: left
```

The more advanced **Performer** modes accessible through the {guilabel}`Perf` sub-menu are typically used when preparing for live conditions with limited rack space. The Ohmicide software plug-in originally introduced the "Melohman" feature which allowed to "play" the plug-in using a MIDI keyboard, and this feature was adapted to Eurorack and its CV/Gate-centric workflow.

### Switch Mode

```{image} performer_simple.png
:align: left
```

The **Switch** Performer mode is exactly like **Producer** mode, except a click on the encoder is needed to activate the selected distortion. Compared to the **Producer** mode, this allows to "jump" to a specific distortion without hearing all the distortions in between.

To access **Switch** mode, press {guilabel}`TYPE` for 2 seconds, a menu will appear. By rotating {guilabel}`TYPE`, navigate to {guilabel}`Perf` and click {guilabel}`TYPE`. {guilabel}`Switch` is already selected, press {guilabel}`TYPE`. The module will go back to its initial screen, except the frame around the current distortion is dashed.

Rotate {guilabel}`TYPE` to select the distortion. The screen will blink and show the current active distortion, and the latent one. The latent one will become the current active distortion when {guilabel}`TYPE` is pressed again.

```{note}
The distortion becomes active exactly when the {guilabel}`TYPE` button is released. This allows to be more precise in Live conditions, and is a common feature found on DJ consoles.
```

To go back to **Producer** mode, press {guilabel}`TYPE` for 2 seconds. {guilabel}`Prod` is already selected, press {guilabel}`TYPE`. You are back in the default mode.


### CV and Trigger Modes

```{image} performer_cv.png
:align: left
```
```{image} performer_step.png
:align: left
```

The **CV** mode and **Trigger** Performer modes work as a mini-sequencer inside Ohmicide, with as much as 16 individual sequences. In **Producer** mode, you can double click on {guilabel}`TYPE` and save the current Ohmicide knobs and distos configuration in a step of the current selected sequence, for a maximum of 8 steps. In those two modes, the {guilabel}`TYPE` knob and associated CV refers to a step in the sequence.

This sequence can be then played back either as a classical step sequencer using **Trigger** mode where the {guilabel}`TYPE` jack input acts as a trigger input, or using it as a CV to address steps in any order using **CV** mode.

The sequence length can be tuned from 1 to 8 steps, and the {guilabel}`TYPE` CV input in **CV** mode can be configured to handle either ±5V or 0..5V depending on the capabilities of the module controlling it.

For even more playability, each knob of a sequence can be configured further:

- **Latch**, the default option, which allows the knob to override the current sequencer step value as soon as it is turned, until another preset is loaded,
- **Relative**, which allows to modulate slightly around the sequencer step value using the knob,
- **Override**, which ignores the sequencer step knob value.

```{image} performer_cur_seq.png
:align: left
```

To select the current sequence, press the {guilabel}`TYPE` encoder for 2 seconds, navigate to {guilabel}`Perf`, then {guilabel}`#Seq`. Press the encoder. By rotating the {guilabel}`TYPE` encoder choose the current sequence from 1 to 16. Once selected, navigate to {guilabel}`Back` by turning the encoder to the left, press the encoder, and repeat this to go back to the initial screen.

```{image} save_step.png
:align: left
```

To save the current configuration of the knobs and switches, first make sure you are in **Producer** mode. Then press the {guilabel}`TYPE` encoder two times quickly, and the {guilabel}`Save Step` menu will appear. To save a step into the sequence, rotate the encoder to the desired step and press the encoder. The step is then saved and the module will go back to the initial screen.

```{note}
Should you have entered the {guilabel}`Save Step` menu by mistake, turn the encoder to the left to navigate to {guilabel}`Back` and exit the menu without saving. 
```

To activate {guilabel}`CV` mode or {guilabel}`Trig` mode, press the {guilabel}`TYPE` encoder for 2 seconds, navigate to {guilabel}`Perf` and then choose one of those two modes and press the encoder. The module will go back to the initial screen and will show a mini representation of the sequence.

```{image} performer_seq_len.png
:align: left
```

To change the length of the sequence, press the {guilabel}`TYPE` encoder for 2 seconds, navigate to {guilabel}`Perf` and then {guilabel}`#Steps`. Press the encoder, and rotate it to choose the desired length from 1 to 8. Once selected, navigate to {guilabel}`Back`, press the encoder, and repeat this to go back to the initial screen. The screen will now show the new sequence length.

To change the start of the sequence, rotate the {guilabel}`TYPE` encoder. The screen will blink and show the current active start, and the latent one. The latent one will become the current active start when the encoder is pressed again. In **Trigger** mode this will also reset the current step.

Pressing the encoder while in **Trigger** mode will reset the current step.

There are 2 ways to reset a step:

- Either go to the first step immediatly. In that mode the next trigger received will increment to the **second step**,
- Or go the last step of the sequence. In that mode the next trigger received will increment to the **first step**.

```{image} step_reset.png
:align: left
```

To change the step reset mode, press the {guilabel}`TYPE` encoder for 2 seconds, navigate to {guilabel}`Perf` and then {guilabel}`Steps Reset`. Press the encoder, and rotate it to choose the desired mode, either {guilabel}`Inst` (_ie._ instant), or {guilabel}`Next` (_ie._ on next trigger).

```{image} pots.png
:align: left
```

```{image} pots_opt.png
:align: left
```

Finally to change the knobs option, press the {guilabel}`TYPE` encoder for 2 seconds, navigate to {guilabel}`Perf`, then {guilabel}`Pots`. Navigate to the knob you desired to change, press the encoder and rotate it to choose either {guilabel}`Latch`, {guilabel}`Relat` (Relative) or {guilabel}`Ovrd` (Override).
