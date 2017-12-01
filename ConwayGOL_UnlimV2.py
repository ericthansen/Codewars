class gCell(self,vitality):
  self.alive=vitality
  self.nextAlive=True
  self.n=None
  self.ne=None
  self.e=None
  self.se=None
  self.s=None
  self.sw=None
  self.w=None
  self.nw=None
  self.nbrs=[n,ne,e,se,s,sw,w,nw]

  def isLive():
    return self.alive

  def predict():
    count=0
    for i in nbrs:
      if(i==None):
        pass
      else:
        count+=i.isLive()
    if count<2:
      return 'die'
    elif count>3:
      return 'die'
    else:#ß
      return 'live'





class GOL(self,inp):
