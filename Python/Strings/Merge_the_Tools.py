def merge_the_tools(string, k):

    for i in range(0,len(string),k):
        a=string[i:i+k]
        z=""
        for j in a:
            if j not in z:
                z+=j
        print(z)
