import random as rnd
rnd.seed(149)
guess=[""]
o_guess=[""]
w=["R","P","S"]
ord={}
resp={"R":"P","P":"S","S":"R"}
cnt=[0]

def join(lst):
    return "".join(lst)

def markov4(history, play_order):
    if join(history[-4:]) in play_order.keys():
        play_order[join(history[-4:])] += 1
    else:
        play_order[join(history[-4:])] = 1
    possible = [join(history[-3:]) + k for k in w]
    for p in possible:
        if not p in play_order.keys():
            play_order[p] = 0
    predict = max(possible, key=lambda key: play_order[key])
    return predict[-1]


def player(prev_play,opponent_history=[]):
    if prev_play == "" or cnt[0]>69:
      prev_play=rnd.choice(w)
      cnt[0]=0
    hist=opponent_history
    hist.append(prev_play)
    cnt[0]+=1
    if len(hist) >= 4:
        p=resp[markov4(hist,ord)]
        guess[0]=p
    if guess[0]=="":
      guess[0]=rnd.choice(w)
    return guess[0]

