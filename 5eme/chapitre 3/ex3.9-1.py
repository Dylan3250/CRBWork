text = input('Veuillez marquer le message que vous voulez coder.')
text = text.lower()

pattern = 'abcdefghijklmnopqrstuvwxyzabc';

for i in range (len(text)):
    if text[i] == ' ' or text[i] == "'":
        print(text[i],end='')
    else:
        print(pattern[pattern.find(text[i])+3], end='')