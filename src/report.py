import pandas as pd
from src.signals import generate_sine_wave, generate_chord
from src.features import rms_energy, zero_crossing_rate, spectral_centroid
def build_feature_table(metadata_path: str) -> pd.DataFrame:
    """
    For every row in metadata.csv: generate the signal (sine or chord depending on
    how many frequencies are listed), compute rms/zcr/spectral_centroid, and collect
    everything into one DataFrame with columns:
    name, label, duration, rms, zcr, spectral_centroid
    Hints
    -----
    - pd.read_csv the metadata file.
    - The 'frequencies' column is a string like '261.63;329.63' -- split on ';' and
    convert to floats to decide sine vs chord.
    - Build a list of dicts (one per row) as you go, then pd.DataFrame(list_of_dicts)
    at the end -- much faster than appending to a DataFrame row by row.
    """
    # TODO: implement
    # raise NotImplementedError
    df = pd.read_csv(metadata_path)
    result_list = []
    for index, row in df.iterrows():
        result_dict = {}
        result_dict['name'] = row['name']
        result_dict['label'] = row['label']
        result_dict['duration'] = row['duration'] 
        if row['label'] == "single_note":
            signal = generate_sine_wave(float(row['frequencies']), row['duration'])
        else:
            freqlist = row['frequencies'].split(';')
            freqlist = [float(freq) for freq in freqlist]
            signal = generate_chord(freqlist, row['duration'])
        result_dict['rms'] = rms_energy(signal)
        result_dict['zcr'] = zero_crossing_rate(signal)
        result_dict['spectral_centroid'] = spectral_centroid(signal)
        result_list.append(result_dict)
    result_df = pd.DataFrame(result_list)
    return result_df

    
