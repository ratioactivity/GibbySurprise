import random
import time
import sys

# Surprise messages
messages = [
    "✨ You are made of stardust and chaos. ✨",
    "🌻 Even radioactive clocks think you're glowing. 🌻",
    "🚬 The vape won’t kill you, but the vibes might. 🌀",
    "🐟 You are a majestic sturgeon, and no one can take that from you.",
    "🦴 Your bones contain more serotonin than you think. Probably. Don’t test it.",
    "📻 Gibby FM coming at you live with late-night emotional resilience.",
    "💀 Death is inevitable. Might as well be interesting about it.",
    "🌊 Reminder: no one is prepared for how powerful you are when joyful."
]

ascii_art = r"""
     __
    /  \__
   (     @\___
   /         O
  /   (_____/
/_____/ U

   RADIOACTIVE FISH SAYS:
   YOU ARE STRONGER THAN YOUR WORST DAY.
"""

def rainbow(text):
    colors = ['\033[91m','\033[93m','\033[92m','\033[96m','\033[94m','\033[95m']
    reset = '\033[0m'
    result = ''
    for i, char in enumerate(text):
        result += colors[i % len(colors)] + char
    return result + reset

def typewriter(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    print("\n\n🎁 UNWRAPPING JOY MODULE...\n")
    time.sleep(1)
    typewriter(rainbow(random.choice(messages)))
    time.sleep(1)
    print("\n" + ascii_art)
    time.sleep(1)
    input("\n🐠 Press Enter to receive a random affirmation...\n")
    typewriter(rainbow(random.choice(messages)))
    print("\n💚 Program complete. Feel free to rerun any time your serotonin dips.\n")

if __name__ == "__main__":
    main()
