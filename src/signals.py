import numpy as np
def generate_sine_wave(frequency: float, duration: float, sample_rate: int = 48000,
amplitude: float = 1.0) -> np.ndarray:
    """
    Generate a pure sine wave.
    Parameters
    ----------
    frequency : float
    Frequency of the tone in Hz (e.g. 440.0 for concert A).
    duration : float
    Length of the signal in seconds.
    sample_rate : int
    Number of samples per second.
    amplitude : float
    Peak amplitude of the wave.
    Returns
    -------
    np.ndarray
    1D array of shape (int(duration * sample_rate),) containing the waveform.
    Hints
    -----
    - Build a time array first: the timestamp of every sample, from 0 to `duration`,
    spaced 1/sample_rate apart. Look up np.linspace or np.arange.
    - A sine wave is: amplitude * sin(2 * pi * frequency * t) for each timestamp t.
    - np.sin operates elementwise on a whole array at once -- no loop needed.
    """
    timearray = np.arange(sample_rate * duration) / sample_rate
    angle = 2 * np.pi * frequency * timearray
    signal = amplitude * np.sin(angle)
    return signal

def generate_chord(frequencies: list[float], duration: float, sample_rate: int = 48000, amplitude: float = 1.0) -> np.ndarray:
    """
    Generate a chord: the sum of sine waves at each given frequency.
    Parameters
    ----------
    frequencies : list[float]
    e.g. [261.63, 329.63, 392.00] for a C major triad.
    duration, sample_rate, amplitude : same as generate_sine_wave.
    Returns
    -------
    np.ndarray
    1D array -- the summed waveform. Normalize the result so its max absolute
    value stays at `amplitude` (otherwise more notes = louder, which isn't realistic).
    Hints
    -----
    - Call generate_sine_wave once per frequency and add the results together.
    - A short Python for-loop over `frequencies` (a handful of notes) is fine here --
    vectorization matters for looping over *samples* (thousands), not over 3-5 notes.
    - After summing, rescale: divide by (max(abs(signal)) / amplitude) to prevent
    clipping.
    """
    chordarray = np.zeros(int(sample_rate * duration))
    for i in frequencies:
        chordarray += generate_sine_wave(i, duration, sample_rate, amplitude)
    peak = np.max(np.abs(chordarray))
    chordarray = chordarray / peak * amplitude
    return chordarray

one = generate_sine_wave(440, 1.0)
chord = generate_chord([440, 550, 660], 1.0, amplitude=1.0)
