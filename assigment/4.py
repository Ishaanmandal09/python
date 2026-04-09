name = "ishaan mandal";

letter = '''
dear Ishaan Mandal
you are selected!
2003'''
print(f"Good afternoon  {name} ");


letter = '''
dear <|name|>
you are selected!
<|year|>'''

print(letter.replace("<|name|>", name).replace("<|year|>", "2003"));

name = "Ishaan Mandal";
print(name.find("a"));

print(name.replace(" " ,"_")); 

letter = " evil never die and good always a lie";
print (letter)