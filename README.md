
##  Wav chunker

This script is designed to break down wav files into chunks, append a tag then print those chunks to the console.

### Requirements

The script was written in Python 3.5, package requirements for the script are contained in requirements.txt. Use `pip install -r requirements.txt` to install.

### Basic usage

The script is used by specifying each data directory followed by a single character tag to apply to all wav data in that directory. e.g. if our data is located in a subdirectory named 'syntetic' and we want to tag it with an S:

```
python chunk.py --data ./synthetic S
```

There are several option arguments, such as `--chunk_size` and `--sample_rate` which control the length of each chunk (in samples), and the sample rate to process the audio at. The defaults for these are 2000 and 16kHz respectively.
