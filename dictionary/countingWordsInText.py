def count_word(text):
  text=text.split()
  result={}
  for word in text:
    if word not in result:
      if word.endswith(","):
        word=word[:len(word)-1]
      result[word]=0
    result[word]+=1
  for letter, amount in result.items():
    print("{:<17} : {:>3}".format(letter,amount))


count_word("Some of the signs and symptoms of multisystem inflammatory vasculitis include persistent fever, abdominal pain, gastrointestinal symptoms, including nausea, vomiting and diarrhea, as well as rash and inflammation of arteries of the hear")