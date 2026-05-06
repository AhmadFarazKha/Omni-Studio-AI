import os
from tools.story_gen import generate_multilingual_story
from dotenv import load_dotenv

# Load your API Key from the .env file
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

def start_production():
    print("--- OMNI-STUDIO AI ANIMATION PIPELINE ---")
    
    # 1. Get User Input
    topic = input("Enter your story topic: ")
    language = input("Choose language (English/Urdu/Hindi): ")
    
    # 2. Agent Logic: Generate Story
    print(f"\n[Agent] Drafting the story in {language}...")
    story_data = generate_multilingual_story(topic, language, API_KEY)
    
    print("\n--- GENERATED SCRIPT ---")
    print(story_data)
    
    # 3. Next Phase: Character Generation (Placeholder for now)
    print("\n[Agent] Story ready. Proceeding to character design...")

if __name__ == "__main__":
    start_production()