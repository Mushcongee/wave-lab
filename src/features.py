import numpy as np
def rms_energy(signal: np.ndarray) -> float:
    """
    Root-mean-square energy: a measure of loudness.
    Formula: sqrt(mean(signal ** 2))
    Sanity check: for a pure sine wave of amplitude A, RMS should equal A / sqrt(2).
    """
    return np.sqrt(np.mean(signal ** 2))


def zero_crossing_rate(signal: np.ndarray) -> float:
    """
    Fraction of adjacent sample pairs where the sign flips (- to + or + to -).
    Higher for noisy/high-frequency signals, lower for smooth low-frequency ones.
    Hints
    -----
    - np.sign(signal) gives -1/0/1 per sample.
    - Compare np.sign(signal[:-1]) to np.sign(signal[1:]) -- where they differ, a
    crossing happened.
    - A boolean mask of 'where they differ' summed and divided by length gives the
    rate.
    """
    sign = np.sign(signal)
    crossings = sign[1:] != sign[:-1]
    return np.sum(crossings) / (len(signal) - 1)

def spectral_centroid(signal: np.ndarray, sample_rate: int = 48000) -> float:
    """
    The "center of mass" of the frequency spectrum -- roughly, the brightness of a
    sound.
    Hints
    -----
    - magnitudes = np.abs(np.fft.fft(signal))
    - freqs = np.fft.fftfreq(len(signal), d=1/sample_rate)
    - Only keep the positive-frequency half (freqs >= 0) using a boolean mask.
    - Centroid = weighted average of freqs, weighted by magnitudes:
    sum(freqs * magnitudes) / sum(magnitudes)
    """
    magnitudes = np.abs(np.fft.fft(signal))
    freqs = np.fft.fftfreq(len(signal), d=1/sample_rate)
    return (sum(freqs * magnitudes) / sum(magnitudes))


if __name__ == "__main__":
    from signals import generate_sine_wave

    # RMS: a 440 Hz, amplitude-1 sine should read ~0.7071 (= 1 / sqrt(2))
    sine_440 = generate_sine_wave(440, 1.0, amplitude=1.0)
    print(f"RMS of 440Hz amp-1 sine: {rms_energy(sine_440):.4f}  (expect ~{1/np.sqrt(2):.4f})")

    # Spectral centroid: lower-frequency tone should have a lower centroid
    c_220 = spectral_centroid(generate_sine_wave(220, 1.0))
    c_880 = spectral_centroid(generate_sine_wave(880, 1.0))
    print(f"centroid 220Hz: {c_220:.1f} Hz")
    print(f"centroid 880Hz: {c_880:.1f} Hz")
    print(f"220Hz centroid < 880Hz centroid? {c_220 < c_880}")