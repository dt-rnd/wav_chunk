import librosa
import fileutils
import numpy as np

"""
    Wav utils
    adapted from: https://github.com/ibab/tensorflow-wavenet
"""

def trim_silence(audio, threshold=0.1):
    '''Removes silence at the beginning and end of a sample.'''
    energy = librosa.feature.rmse(audio)
    frames = np.nonzero(energy > threshold)
    indices = librosa.core.frames_to_samples(frames)[1]
    return audio[indices[0]:indices[-1]] if indices.size else audio[0:0]

def load_generic_audio(directory, sample_rate):
    '''Generator that yields audio waveforms from the directory.'''
    files = fileutils.find_files(directory)
    for filename in files:
        audio, _ = librosa.load(filename, sr=sample_rate, mono=True)
        yield audio, filename