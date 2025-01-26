# Open files with English terms and Turkish terms
with open("english_glossary.txt", "r", encoding="utf-8") as en_file, open("turkish_glossary.txt", "r", encoding="utf-8") as tr_file:
    english_glossary = en_file.read().splitlines()
    turkish_glossary = tr_file.read().splitlines()

# Translation process
js_result = []
for i in range(len(english_glossary)):
    en_gloss = english_glossary[i]
    tr_gloss = turkish_glossary[i]
    js_result.append(f'.replace("{en_gloss}", "{tr_gloss}")')

# Print the translation code to another file javascript code
with open("js_result.txt", "w", encoding="utf-8") as ceviri_file:
    ceviri_file.write("//Copy and paste under 'var tr_Translation = en_Words' in the ‘Web Site Glossary Translation.html’ file\n")
    ceviri_file.write("\n".join(js_result))