# Num in list: 20

def isValid(self, s: str) -> bool:
    val = []
    closeToOpen = {")": "(", "]": "[", "}": "{"}

    for i in s:
        if i in closeToOpen:
            if val and val[-1] == closeToOpen[i]:
                val.pop()
            else:
                return False
        else:
            val.append(i)
    return True if not val else False
