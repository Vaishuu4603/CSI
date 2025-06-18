import textwrap

text = "Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming."
wrapped_text = textwrap.fill(text, width=50)
print(wrapped_text)
