import time

print('--'*50)
print()
print("==========   Mad Lib Story 📔    ========== ")
time.sleep(0.5)
print()
def story():
    noun1 = input("Enter noun (person/creature)👩🐕‍🦺: ")
    noun2 = input("Enter an object: ")
    place = input("Enter a place🌄: ")
    verb1 = input("Enter a verb(base form)🚵‍♀️: ")
    verb2 = input("Enter verb2 +ing🚵‍♀️: ")
    adverb1 = input("Enter an adverb: ")
    adverb2 = input("Enter adverb2: ")
    adjective1 = input("Enter an adjective 1: ")
    adjective2 = input("Enter an adjective 2: ")
    adjective3 = input("Enter an adjective 3: ")

    time.sleep(0.5)
    print()
    print("=============   Here's your Mad Lib Story 📔😁    ============= ")

    time.sleep(1)
    print()
    text = f"""
One {adjective1} afternoon🌇, {noun1} and I went to {place} to {verb1}.
There's a {adjective2} {noun2} at {place}, {noun1} was {adverb1} curious to see how it works.
So he went {verb2} to the {adjective2} {noun2}, and came back after a few minutes {adverb2}, looking {adjective3}.
I was in awe😪.
"""
    print(text)

if __name__ == '__main__':
    story()
print('--'*50)
