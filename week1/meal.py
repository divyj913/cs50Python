def main():
    prompt = input("What time is it? ")
    prompt = convert(prompt)
    if 7<= prompt <= 8:
        print("breakfast time")
    elif 12<= prompt <= 13:
        print("Lunch time ")
    elif 18<= prompt <= 19:
        print("Dinner time ")
    else:
        print("eat nothing.")
def convert(t):
    h , m = t.split(":")
    h = float(h)
    m = float(m)
    return h+m/60
main()
