import unittest
from os.path import abspath

from src.util import audio_util


class TestAudioUtil(unittest.TestCase):

    def test_mp3_to_wav(self):
        infile = abspath('208.mp3')
        outfile = abspath('208.wav')
        audio_util.mp3_to_wav(infile, outfile)
