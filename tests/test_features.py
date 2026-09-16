import numpy as np
import pytest

from src.signals import generate_sine_wave
from src.features import rms_energy, zero_crossing_rate, spectral_centroid


def test_rms_energy_of_sine_wave():
    """For a pure sine wave of amplitude A, RMS should equal A / sqrt(2)."""
    amplitude = 1.0
    signal = generate_sine_wave(frequency=440, duration=1.0, amplitude=amplitude)

    result = rms_energy(signal)
    expected = amplitude / np.sqrt(2)

    assert result == pytest.approx(expected, rel=1e-3)


def test_rms_energy_scales_with_amplitude():
    """Doubling the amplitude should double the RMS."""
    signal_1x = generate_sine_wave(frequency=440, duration=1.0, amplitude=1.0)
    signal_2x = generate_sine_wave(frequency=440, duration=1.0, amplitude=2.0)

    assert rms_energy(signal_2x) == pytest.approx(2 * rms_energy(signal_1x), rel=1e-6)


def test_rms_energy_of_silence():
    """A flat zero signal should have zero RMS energy."""
    signal = np.zeros(1000)
    assert rms_energy(signal) == 0.0


@pytest.mark.skip(reason="zero_crossing_rate not implemented yet")
def test_zero_crossing_rate_of_sine_wave():
    pass


@pytest.mark.skip(reason="spectral_centroid not implemented yet")
def test_spectral_centroid_of_sine_wave():
    pass
