wins=[[1],[2],[3],[4]]
losses=[[1],[2,2],[1,1,1]]
w='win'
l='loss'
#dic = {[1]: w, [1,1]: l,[2,2]:l}
def decr(game,pile,amt):
	ret=[]
	for i in game:
		ret.append(i)
	ret[pile]-=amt
	if (ret[pile]<=0):
		ret.remove(ret[pile])
	else:
		pass
	return ret
def choose_move(game_state):
	"""Chooses a move to play given a game state"""
	print('gamestate is ',game_state)
	gs=sorted(game_state)
	#print(gs)
	odds=0
	evens=0
	ones=0
	twos=0
	manys=0
	tot=0
	for i in gs:
		tot=tot+i
		if(i<0):
			break#"error, negative pile size"
		else:
			pass
		if (i % 2 ==0):
			evens+=1
		else:
			odds+=1
		if(i==1):
			ones+=1
		elif(i==2):
			twos+=1
		else:
			manys+=1
	piles=len(gs)
	print(evens, odds, ones, twos, manys,tot)
	win=False
	while(win==False):
		for j in gs:
			temp=[]
			for k in gs:
				temp.append(k)
			for l in range(len(gs)):
				for m in range(gs[l]):
					t=decr(temp,l,m)
					if (t in wins):
						win=True
					else:
						choose_move(t)


	return None

print(choose_move([4,2,1,2,3]))
#game=[4,2,1,2,3]
#x=decr(game,1,1)
#print(x)
#print(game)