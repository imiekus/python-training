answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]
print(answer)

friends = ["Elie", "Tim", "Matt"]
answer2 = [val[::-1].lower() for val in friends]
print(answer2)