def decodeMorse(morseCode):
	morseCode=morseCode.strip()
	# ToDo: Accept dots, dashes and spaces, return human-readable message
	#in codewars, MORSE_CODE[] is a preloaded dictionary
	MORSE_CODE = {'.-': 'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E', '..-.':'F', '--.':'G', '....':'H',
	 '..':'I', '.---':'J', '-.-':'K', '.-..':'L', '--':'M', '-.':'N', '---':'O', '.--.':'P', '--.-':'Q', 
	 '.-.':'R', '...':'S', '-':'T', '..-':'U', '...-':'V', '.--':'W', '-..-':'X', '-.--':'Y', '--..':'Z', 
	 '.----':'1', '..---':'2', '...--':'3', '....-':'4', '.....':'5', '-....':'6', '--...':'7', '---..':'8', 
	 '----.':'9', '-----':'0',
	 '· -- · -- · --':'.', '-- --· · -- --':',', '· · -- --· ·':'?', '-- -- -- · · ·':':', '-- · -- · -- ·':';', 
	 '-- · · · · --':'-', '...--..--':'$', '· -- -- · -- ·':'@', '· -- · -- ·':'Stop', '· -- · · ·':'Wait','· -- ·':'Received' }
	#print(MORSE_CODE['...'])

	curLetter=''
		#currentAlNum Letter
	cur=''
		#currentMorseBit
	prev=''
		#PrevMorseBit
	prePrev=''
		#before previous morse bit
	out=[]
		#appendable array of alNum letters&spaces
	#if(morseCode[0]==' '):
	#	print("ERROR")
	for a in (morseCode):
		if(a==' '):
			if(prev==' '):
				if(prePrev==' '):
					out.append(' ')
					prePrev=prev
					prev=a
					curLetter=''
				else:
					#curLetter=a
					prePrev=prev
					prev=a
			else:
				prePrev=prev
				prev=a
				#print(curLetter)
				out.append(MORSE_CODE[curLetter])
				curLetter=''
		else:
			curLetter=curLetter+a
			preprev=prev
			prev=a
	out.append(MORSE_CODE[curLetter])#bc final letter wouldn't get appended bc no trailing space
	sp=""
	out=sp.join(out)
	return out
#print(decodeMorse('.... . -.--   .--- ..- -.. .'))
#print(decodeMorse('    .... . -.--   .--- ..- -.. .     '))

def decodeBits(bits):
	# ToDo: Accept 0's and 1's, return dots, dashes and spaces
	bits=bits.strip().strip('0')
	#first, find send frequency
	minRun=len(bits) #this will be the "send frequency" - i.e the shortest length of 1s or 0s
	curRun=len(bits)
	#firstRun=0
	prev=''
	for b in bits:
		if(b==prev):
			curRun=curRun+1
		else:
			if(minRun>curRun):
				minRun=curRun
			curRun=1
		prev=b
	bitz=bits.split(7*'0'*minRun)

	#print('minrun is ',minRun)
	#print('bitz is ', bitz)
	fin=''
	for w in bitz:
		currw=w.split(3*'0'*minRun)
		#print('currw is ',currw)
		cw=''
		for u in currw:
			currl=u.split(1*'0'*minRun)
			#print('currl is ',currl)
			cl=''
#			ddd=''
			for dd in currl:
				if(dd=='1'*minRun):
					cl=cl+'.'
				else:
					cl=cl+'-'
			#cl=decodeMorse(cl)
			#print('cl is ',cl)
			cw=cw+' '+cl
			#print('cw is ',cw)
		cw=cw.strip()
		fin=fin+'   '+cw
		#print('fin is ', fin)
	fin=fin.strip()
	#print('fin is ',fin)
	return fin
	#sp=' '
	#return sp.join(fin.strip())
#	bitz2=sp.join(bitz)
#	print('bitz2 is ', bitz2)

#	return bits.replace('111', '-').replace('000', ' ').replace('1', '.').replace('0', '')
#print(decodeBits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'))
print(decodeMorse(decodeBits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')))