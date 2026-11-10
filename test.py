line = "ksdfj;;;;kjdg ;;; sdf"

def clear_povtor(line):
    newlist = []
    for i in range(len(line)):
        if line[i] == ';' and newlist and newlist[-1] == ';':
            continue
        newlist.append(line[i])
    return "".join(newlist)

print(clear_povtor(line)) 
