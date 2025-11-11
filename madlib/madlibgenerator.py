"""Mad Libs Story Generator

This script collects words from the user and generates a silly story
using those words. The story is printed to the terminal and saved
to a text file.
"""


class WordBank:
    """A class to store words for use in the Mad Libs story."""
    
    def __init__(self, noun, verb, adjective, place, emotion, animal, celebrity, object_):
        """Initialize the WordBank with the provided words.
        
        Args:
            noun: A person, place, or thing
            verb: An action word
            adjective: A descriptive word
            place: A location
            emotion: A feeling
            animal: An animal name
            celebrity: A famous person's name
            object_: An object or thing
        """
        self.noun = noun
        self.verb = verb
        self.adjective = adjective
        self.place = place
        self.emotion = emotion
        self.animal = animal
        self.celebrity = celebrity
        self.object = object_


def collect_words() -> WordBank:
    """Collect words from the user interactively.
    
    Returns:
        A WordBank object populated with user input.
    """
    print("\n🎭 Welcome to the Mad Libs Story Generator! 🎭\n")
    print("Please provide the following words:")
    
    noun = input("Enter a noun: ").strip()
    verb = input("Enter a verb (action word): ").strip()
    adjective = input("Enter an adjective (descriptive word): ").strip()
    place = input("Enter a place: ").strip()
    emotion = input("Enter an emotion (feeling): ").strip()
    animal = input("Enter an animal: ").strip()
    celebrity = input("Enter a celebrity or famous person: ").strip()
    object_ = input("Enter an object: ").strip()
    
    return WordBank(noun, verb, adjective, place, emotion, animal, celebrity, object_)


def generate_story(word_bank: WordBank) -> str:
    """Generate a silly story using the words from the WordBank.
    
    Args:
        word_bank: A WordBank object containing all the words.
        
    Returns:
        A string containing the complete story.
    """
    story = f"""
╔═══════════════════════════════════════════════════════════════╗
║                    THE WILD ADVENTURE                         ║
╚═══════════════════════════════════════════════════════════════╝

One day, a {word_bank.adjective} {word_bank.noun} decided to {word_bank.verb} 
in the magical land of {word_bank.place}. 

The {word_bank.noun} was feeling {word_bank.emotion}, so they decided to 
seek help from their best friend, a talking {word_bank.animal}. 

Together, they journeyed through forests, crossed rivers, and eventually 
ran into the famous {word_bank.celebrity}, who was also looking for a 
mysterious {word_bank.object}.

"I will help you find it!" said the {word_bank.celebrity}, striking a heroic pose.

The three friends spent the whole day searching, laughing, and causing 
mayhem wherever they went. Finally, they discovered the {word_bank.object} 
hidden behind a giant {word_bank.adjective} rock.

With their quest complete, the {word_bank.noun}, the {word_bank.animal}, 
and {word_bank.celebrity} became the best of friends forever, and they 
all lived happily ever after in {word_bank.place}.

                            THE END

═══════════════════════════════════════════════════════════════════
"""
    return story


def save_story(story: str, filename: str = "madlib_story.txt") -> None:
    """Save the story to a text file.
    
    Args:
        story: The story text to save.
        filename: The name of the file to save to (default: madlib_story.txt).
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(story)
    print(f"✓ Story saved to {filename}\n")


def main():
    """Main function to run the Mad Libs generator."""
    # Collect words from user
    word_bank = collect_words()
    
    # Generate the story
    story = generate_story(word_bank)
    
    # Print the story to terminal
    print(story)
    
    # Save the story to a file
    save_story(story)


if __name__ == "__main__":
    main()
