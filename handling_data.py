#IN THE COMMENTED CODE BELOW I HANDLED THE DATA AND SORTED IT FOR THE FIRST TIME ASKING IT IS CACHED SO IT IS FASTER



# Calculated the entropies for the first time and cached it so I commented the code
# with open('cache.json', 'r') as f:
#     data = json.load(f)

# for g in guesses:
#     counter = defaultdict(float)

#     for a in s:
#         pattern = feedback(g, a)
#         counter[pattern] += 1

#     total = float(len(s))
#     for key in counter:
#         counter[key] /= total

#     h_g = -sum(val * math.log2(val) for val in counter.values() if val > 0)

#     data["entropies"].append(h_g)

# with open('cache.json', 'w') as f:
#     json.dump(data, f)
    
# with open('cache.json', 'r') as f:
#     data = json.load(f)
# sorted_guesses = [g for g, h in sorted(zip(guesses, data["entropies"]), key=lambda x: x[1], reverse=True)]
# with open('dictionary_5_letter.json','w') as file:
#     json.dump(sorted_guesses,file)
