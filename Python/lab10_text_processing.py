#Text Processing Tool
print("       TEXT PROCESSING TOOL")
sentence = input("Enter a sentence: ")

print("--- Processing Results ---")

position = int(input("Enter position for indexing: "))

if 0 <= position < len(sentence):
    print(f"Character at position {position} : '{sentence[position]}'")
else:
    print("Invalid position!")
start = int(input("Enter start index for slicing : "))
end = int(input("Enter end index for slicing   : "))

print(f"Sliced string [{start}:{end}] : '{sentence[start:end]}'")
print(f"Uppercase                  : {sentence.upper()}")
print(f"Lowercase                  : {sentence.lower()}")

word = input("Enter word to replace       : ")
replacement = input("Enter replacement word      : ")

new_sentence = sentence.replace(word, replacement)
print(f"After replace               : {new_sentence}")
print(f"Length of sentence          : {len(sentence)}")
print("Analysis Complete!")
