def sigma(F, B, E):
    	if B > E:
		return 0
	return F(B) + sigma(F, B+1, E)

def numTrue(P, S):
	if S == []:
		return 0
	elif P(S[0]):
		return 1 + numTrue(P, S[1:len(S)])
	else:
		return numTrue(P, S[1:len(S)])

def numFalse(P, S):
	if S == []:
		return 0
	elif P(S[0]):
		return numFalse(P, S[1:len(S)])
	else:
		return 1 + numFalse(P, S[1:len(S)])

def most(P, S):
	if numTrue(P, S) > numFalse(P, S):
         return True
	else:
		return False