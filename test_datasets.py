from datasets import load_dataset

# Test loading a sample dataset
def test_load_dataset():
    print("Testing Hugging Face datasets loading...")
    # Load a small sample dataset
    dataset = load_dataset('ag_news', split='train[:1%]')
    print(f"Loaded dataset with {len(dataset)} examples")
    print("\nSample example:")
    print(dataset[0])

if __name__ == "__main__":
    test_load_dataset()
