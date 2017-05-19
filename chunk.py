import argparse
import wavutils
import numpy as np


def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='wav formatter')
    parser.add_argument('--data', required=True, nargs = 2, action='append')
    parser.add_argument('--sample_rate', type=int, default=16000)
    parser.add_argument('--chunk_size', type=int, default=2000)
    args = parser.parse_args()
    return args


def chunk_directory(dir, tag, sample_rate, chunk_size, trim=True):
    """Takes all wav files in the input directory and chunks to float data"""
    iterator = wavutils.load_generic_audio(dir, sample_rate)

    output = None

    for audio, filename in iterator:

        if trim:
            audio = wavutils.trim_silence(audio, 0.01)

        if output is None:
            output = audio
        else:
            output = np.append(output, audio)

        while len(output) > chunk_size:
            line = output[:chunk_size]
            output = output[chunk_size:]

            print(",".join(["%.6f" % number for number in line]) + "," + tag + "\n")


def main():
    """Parses the command line arguments and kicks off the chunker"""
    args = parse_args()

    sample_rate = args.sample_rate
    chunk_size = args.chunk_size

    for arg in args.data:
        source_directory = arg[0]
        data_suffix = arg[1]
        
        chunk_directory(source_directory, data_suffix, sample_rate, chunk_size)


if __name__ == "__main__":
    main()