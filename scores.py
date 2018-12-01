school = [{"school_class": "4a", "scores": [3, 4, 4, 5, 2]}, 
        {"school_class": "4b", "scores": [5, 5, 4, 5, 3]}, 
        {"school_class": "4c", "scores": [3, 3, 4, 5, 3]}]

total_scores = []
for item in school:
    total_scores.extend(item["scores"])
print(sum(total_scores)/len(total_scores))

for item in school:
    print(sum(item["scores"])/len(item["scores"]))


