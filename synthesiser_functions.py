# leg5@nyu.edu

import os
import scipy.io.wavfile as wave
import numpy as np


def save_synthesised_speech(speaker, speech_rate, save_dest, text_file=None,
                            utterance=None):
    """
    speaker:            OSX built-in speaker name. e.g., Samantha, Alex
    speech_rate:        number of words per minute
    save_dest:          where to save the file. needs aiff extension.
    text_file:          path to file containing text to be synthesised
    utterance:          can provide a string to say rather than load txt
    """

    if text_file:
        os.system("say -v %s -r %s -f %s -o %s" %
                  (speaker, speech_rate, text_file, save_dest))

    elif utterance:
        os.system("say -v %s %s -r %s -o %s" %
                  (speaker, utterance, speech_rate, save_dest))

    pass


def concatenate_aud_files(file_list, result_dest):
    """
    Concatenate auditory files together, and save result.
    Uses SoX -- format is inferred from file extension.
    """

    # make string which is a list of the files to be joined
    file_command = ' '.join(file_list)

    # execute command
    os.system("sox %s %s" % (file_command, result_dest))

    pass


def aiff_to_wav(aiff_fname, wav_fname):
    """
    Convert aiff file to wav file.
    Uses SoX -- format is inferred from file extension.
    """

    # execute command
    os.system("sox %s %s" % (aiff_fname, wav_fname))

    pass


def remove_silence(wav_file, remove_final, save_dest):
    """
    When synthesising single words, OSX Samantha adds some ending silence.
    This function removes a user-defined amount of silence.

    wav_file:           location of wave file
    remove_final:       how much of the file to remove (in seconds)
    """

    # load file
    fs, stim = wave.read(wav_file)

    # get indices based on sample rate
    stim_length = stim.shape[0]/float(fs)
    n_samples_remove = stim_length-remove_final*float(fs)

    # save the cleaned file
    cleaned_stim = stim[0:n_samples_remove]
    wave.write(save_dest, fs, cleaned_stim)

    pass


def save_empty_wav(wav_length, fs, save_dest):

    # make zero matrix
    empty_wav = np.zeros(wav_length*float(fs))

    # save as wav file
    wave.write(save_dest, fs, empty_wav)

    pass
