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
    timearray = np.arange(sample_rate * duration)
    angle = 2 * np.pi * frequency * timearray
    signal = amplitude * np.sin(angle)
    return signal

# TODO: implement
signal = generate_sine_wave(440, 1.0)
print(signal.shape)
print(signal.dtype)
print(signal[:5])
# raise NotImplementedError