import time
import random
import os

def typing_test():
    sentences = [
        "The quick brown fox jumps over the lazy dog. Once upon a time, in a small village, there lived a curious young boy named Alex. One sunny afternoon, while playing near the old oak tree in his backyard, he found a rusty old key buried in the dirt.",
        "A journey of a thousand miles begins with a single step. Determined, Alex searched the forest, the hills, and every corner of his backyard but found nothing. Disappointed but hopeful, he returned to the oak tree where he had found the key.",
        "To be or not to be, that is the question. As he sat beneath the tree, he noticed something strange—a small hidden door in the trunk. His heart raced as he realized the key might fit. With trembling hands, he inserted the key and turned it.",
        "Python programming is fun and easy to learn. Alex smiled and closed the chest. He realized the true treasure was the journey, not just the discovery. From that day on, he shared his story, inspiring others to find adventure in curiosity.",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. In a bustling city filled with busy people, there lived a young woman named Clara. She often felt lonely and wondered about the true meaning of her days.",
        "A good story encourages us to turn the next page. We want to know what happens next and what the characters say. We may feel excited, sad, or afraid. Reading a story can feel so real that we love or hate characters like people in real life.",
        "My younger brother is called Fred. He's very interested in animals—especially sea creatures. He has posters of whales, dolphins, sharks, and octopuses all over his room. Fred talks about them all the time!"
    ]

    test_sentence = random.choice(sentences)

    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*60)
    print("🎯  Welcome to the Typing Speed Test!  🎯")
    print("="*60)
    print("\nType the following sentence as quickly and accurately as you can:\n")
    print(f"📝  \"{test_sentence}\"\n")
    input("Press Enter when you're ready to begin...")

    start_time = time.time()
    typed_sentence = input("\n💬 Start typing: ")
    end_time = time.time()

    time_taken = end_time - start_time
    words = len(typed_sentence.split())
    wpm = (words / time_taken) * 60 if time_taken > 0 else 0

    correct_chars = sum(1 for a, b in zip(typed_sentence, test_sentence) if a == b)
    accuracy = (correct_chars / len(test_sentence)) * 100
    total_chars = max(len(test_sentence), len(typed_sentence))
    error_count = total_chars - correct_chars

    print("\n⏱️  Test Completed!")
    print("-" * 40)
    print(f"⌚ Time Taken      : {time_taken:.2f} seconds")
    print(f"🚀 Words Per Minute: {wpm:.2f} WPM")
    print(f"🎯 Accuracy        : {accuracy:.2f}%")
    print(f"❌ Errors          : {error_count}")
    print("="*60)
    print("👏 Great job! Keep practicing to improve your speed and accuracy.\n")

typing_test()
