from code_parser import analyse_code
import os

def create_readme(filename):
    try:
        funcs, classes = analyse_code(filename)

        os.makedirs("out", exist_ok=True)
        path = os.path.join("out", "README.md")

        with open(path, "w") as file:
            file.write("# Documentation\n\n")
            if funcs:
                file.write("## Functions\n\n")
                for func in funcs:
                    file.write(f"- {func}\n")
            if classes:
                file.write("\n## Classes\n\n")
                for class_ in classes:
                    file.write(f"- {class_}\n")

        return True
    
    except Exception as e:
        print(f"Error creating README.md: {str(e)}")
        return False
