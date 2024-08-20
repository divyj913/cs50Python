def main():
    prompt = input("What's the time ?")
    prompt = convert(prompt)
    
def convert(t):
    if t.endswith('a.m.'):
        t = t.split('a.m.')
        
