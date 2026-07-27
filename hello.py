# My first Python script in this repo

def greet(name):
    return f"Hi! I'm {Rita}, and this is my developer portfolio."


def list_skills():
    skills = ["Python", "Markdown", "GitHub", "Git workflows"]
    print("My skills:")
    for skill in skills:
        print(f"  - {skill}")


if __name__ == "__main__":
    print(greet("Your Name"))
    list_skills()
