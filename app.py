import re
with open ('AI_Hindi_Translation_W10_AI_MOdule_25-English-Plain_eng_hin-postedited.txt', encoding="utf8") as myfile:
    contents = myfile.read()
search_results = re.finditer(r'\(.*?\)', contents)
for item in search_results:
    print( item.group(0))
