authorized_users=set(["alice","bob","frank","grace"])
login_attempts=["alice", "bob", "eve", "alice", "mallory", "frank", "eve"]
def identify_intruders(login,authorized):
    l=[]
    for i in login:
        if i not in authorized:
            l.append(i)
    return set(l)

print(identify_intruders(login_attempts,authorized_users))