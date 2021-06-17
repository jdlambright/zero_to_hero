def pig_it(text):
    s = text.split()
    x = []
    f = []
    for word in s:
        b =word[1:] + word[0] + "ay"
        x.append(b)
        f = ' '.join(x)
    if "!" in f or "?" in f:
        return f[:-2]
    else:
        return f

pig_it("Pig latin is cool?")

'''
I was able to do it on test without punctuation with 

def pig_it(text):
    s = text.split()
    x = [word[1:]+word[0]+"ay " for word in s]

    final = "".join(x)
    print(final)
    return final
    
my favorite solution I read was
    
def pig_it(text):
    return ' '.join([x[1:]+x[0]+'ay' if x.isalpha() else x for x in text.split()])
'''