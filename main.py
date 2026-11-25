import os

MONOLOGUE = """Listen. I have held the Black Gate four hundred years, and no one has asked how the hinges hold. The heroes come at dawn, swords out, and I must rise from a chair I have not left since the siege, monologue ready, lightning on cue. The lightning is on a timer now. I set it myself. It is the one thing here that still works. So. Take the crown. Take the girl in the tower — she complains. But the kettle stays. I have earned this one hot drink before the world ends, and I mean to finish it warm."""
# Verified counts: 100 words, 495 characters (497 UTF-8 bytes; the em-dash in
# "tower — she" is U+2014, encoded as 3 bytes). No trailing newline.

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
output_path = os.path.join(output_dir, 'entry.txt')

with open(output_path, 'w', encoding='utf-8', newline='') as f:
    f.write(MONOLOGUE)

text = MONOLOGUE
print(f"bytes: {len(text.encode('utf-8'))}")
print(f"words: {len(text.split())}")
