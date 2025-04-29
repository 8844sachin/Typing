import time  
import random 

def typing_test():
    
    sentences = [
        "The quick brown fox jumps over the lazy dog Once upon a time, in a small village there lived a curious young boy named Alex. One sunny afternoon while playing near the old oak tree in his backyard, he found a rusty, old key buried in the dirt. It was shaped oddly with intricate designs carved into its surface. Excited Alex decided to find out what the key opened.",
        "A journey of a thousand miles begins with a single step Determined, Alex decided to look for the chest. He searched the forest, the hills, and every corner of his backyard but found nothing. Disappointed but not ready to give up, he returned to the oak tree, where he had found the key.",
        "To be or not to be, that is the question As he sat down beneath the tree, he noticed something strange—a small, hidden door in the trunk of the oak. His heart raced as he realized the key might fit there. With trembling hands, he inserted the key into the lock and turned it.But something in her heart urged her to approach him.",
        "Python programming is fun and easy to learn Alex smiled and closed the chest. He realized that the true treasure was the journey of discovery, not just the things he found. From that day on, Alex shared his adventure with others, teaching them that sometimes the search itself is the most rewarding part.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts In a bustling city filled with busy people, there lived a young woman named Clara. She worked long hours at a corporate office and often felt lonely amidst the crowd. Her days blurred into one another, and she began to feel that her life lacked any real purpose."
    "A good story encourages us to turn the next page and read more. We want to find out what happens next and what the main characters do and what they say to each other. We may feel excited, sad, afraid, angry or really happy. This is because the experience of reading or listening to a story is much more likely to make us 'feel' that we are part of the story, too. Just like in our 'real' lives, we might love or hate different characters in the story. Perhaps we recognise ourselves or others in some of them. Perhaps we have similar problems."
    "My younger brother is called Fred. Fred's very interested in animals. He talks and asks questions about animals ALL the time! Fred's really interested in parrots and pandas and lions and leopards and rabbits. But Fred's favourite animals live in the sea. He has pictures of whales, dolphins, sharks and octopuses on all the walls of his bedroom."
    ]
    
    test_sentence = random.choice(sentences)
    
    print("Typing Test\n")
    print("Type the following sentence as fast as you can:")
    print(f'"{test_sentence}"\n')
    print("Press Enter when you're ready to start.")
    input() 

   
    start_time = time.time()

    # Step 5: Get the user input
    typed_sentence = input("Start typing: ")

    # Step 6: Record the end time
    end_time = time.time()

    # Step 7: Calculate the time taken to type
    time_taken = end_time - start_time

    # Step 8: Calculate words per minute (WPM)
    words = len(typed_sentence.split())  # Count the number of words
    wpm = (words / time_taken) * 60  # Words per minute formula

    # Step 9: Calculate accuracy and error count
    correct_chars = sum(1 for a, b in zip(typed_sentence, test_sentence) if a == b)
    accuracy = (correct_chars / len(test_sentence)) * 100  # Accuracy in percentage

    # Error count (extra characters typed or missed)
    total_chars = max(len(test_sentence), len(typed_sentence))
    error_count = total_chars - correct_chars

    # Step 10: Display the results
    print(f"\nTest completed!")
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Words per minute: {wpm:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Errors: {error_count}")

# Run the typing test
typing_test()
