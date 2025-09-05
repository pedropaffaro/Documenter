from generator import create_readme

if __name__ == "__main__":
    try:
        if create_readme("example/example.py"):
            print("README.md created successfully.")
        else:
            print("Failed to create README.md.")   
    except Exception as e:
        print(f"Error creating README.md: {str(e)}")
