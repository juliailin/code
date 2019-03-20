cue=[1,2,3,5,6,4]
bribes=0
for i in range(len(cue)):
    bribes_i=0
    for j in range(i,len(cue)):
        if cue[i]>cue[j]:
            bribes=bribes+1
            bribes_i=bribes_i+1
            if bribes_i>2:
                print("Too chaotic")
print(bribes)
print('try me')
