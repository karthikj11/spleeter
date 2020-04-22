from spleeter.audio.adapter import get_default_audio_adapter

TEST_AUDIO_DESCRIPTOR = 'audio_example.mp3'
TEST_OFFSET = 0
TEST_DURATION = 600.
TEST_SAMPLE_RATE = 44100

def audio_data():
    waveform , _ = get_default_audio_adapter().load(
        TEST_AUDIO_DESCRIPTOR,
        TEST_OFFSET,
        TEST_DURATION,
        TEST_SAMPLE_RATE)
    return waveform
print (audio_data())
print (audio_data().shape)