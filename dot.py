def correct_sentence(text):
    text = text[0].upper() + text[1:] if text else ""
    if not text.endswith('.'):
        text += '.'
    return text
assert correct_sentence("greetings, friends")
assert correct_sentence("Greetings. Friends")
assert correct_sentence("Greetings, friends.")
assert correct_sentence("greetings, friends.")

print('ОК')
