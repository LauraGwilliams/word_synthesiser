# leg5@nyu.edu
# synthesise a list of words

import os
from synthesiser_functions import save_synthesised_speech, aiff_to_wav


def synthesise_word_wav(word, speaker, save_dir, speech_rate=200):
	"""
	Generate a .wav file for a written word.
	Synthesis uses the built in iOS Mac synthesiser.


	word:		  string object, the word to by synthesised
	speaker:	  one of the iOS built-in speakers
	save_dir:	  directory to save the files
	speech_rate:  integer, in words per minute
	"""

	# make aiff and wav file dir
	aiff_dest = '%s/%s.aiff' % (save_dir, word)
	result_dest = '%s/%s_s-%s_r-%s.wav' % (save_dir, word, speaker, speech_rate)

	# first, generate .aiff file for this word
	save_synthesised_speech(speaker, speech_rate, aiff_dest, utterance=word)

	# convert to wav
	aiff_to_wav(aiff_dest, result_dest)

	# remove the aiff
	os.remove(aiff_dest)

	# done!
	pass

