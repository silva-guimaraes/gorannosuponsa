import sys
import os
import pysubs2


def add_delay_to_subtitles(subtitles, target_text, delay):
    found_target = False

    # Iterate through each subtitle
    for subtitle in subtitles:
        if target_text in subtitle.text:
            found_target = True
        elif found_target:
            # Add the specified delay to the subtitle start and end times
            subtitle.start += delay
            subtitle.end += delay

    if found_target:
        # Save the modified subtitles to a new file
        subtitles.save("modified_subtitles.srt")
        print("Delay added to subsequent subtitles.")
    else:
        print("Target subtitle not found.")


if len(sys.argv) == 0:
    os.exit(1)

subtitles = pysubs2.load(sys.argv[1])
target_text = "～♪"
# target_text = "~♪"
delay = float(sys.argv[2]) * 1000

add_delay_to_subtitles(subtitles, target_text, delay)
