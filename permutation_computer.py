
def main():
    print()


def compute(p1="123432,hsh2121", p2="73asa"):
    # multiplies two permutation and returns a list of disjoint permutations
    p1l = p1.split(",")
    p2l = p2.split(",")
    letters = []
    for i in p1l+p2l:
        if i not in letters:
            letters.append(i)
    p3 = []
    for l in letters:
        if p3!=[]:
            for i in p3:
                if l in i:
                    break
            # if the letter has not been seen before generate the cycle it is in
            nxt = None
            while nxt != l:
                if not nxt:
                    nxt = l
                nxt = f(nxt)

        else:
            p3.append(l)



def to_trans():
    # converts to a list of transpositions

def to_trans2():
    # converts to a list of transpositions but using pensil method




