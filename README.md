__Simple set of scripts to synthesise words (or non-words) and save them as .wav files__

The underlying synthesiser is built into MacOS. A list of available voices is included in "available_macosx_voices.txt"; or, you can type `say -v '?'` in terminal for this information.

The speech rate is in words per minute (wpm). Average speech rate is ~200 wpm.

_Simple as it gets -- just save a single synthesised word:_

```python
# modules
import os  # this is just to figure out the current directory
from synthesise_word_list import synthesise_word_wav

# directories
save_dir = os.getcwd()  # save in current directory

# params
word_to_say = 'hello'
speaker = 'Samantha'
speech_rate = 150

# run command
synthesise_word_wav(word_to_say, speaker, save_dir, speech_rate)
```

_Load a word list .txt file, loop through each word and save:_

```python
# modules
from synthesise_word_list import synthesise_word_wav

# directories
word_list_file = 'my_word_list.txt'
save_dir = 'where_to_save_files'

# params
speaker = 'Samantha'
speech_rate = 150

with open(word_list_file) as f:
    
    # load file as list
    words = f.read().splitlines()

    # loop through each word and save
    for word in words:
		synthesise_word_wav(word, speaker, save_dir, speech_rate)
```