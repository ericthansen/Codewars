def get_generation(cells,generations):
    curr=cells
    for i in range{0,generations-1,1}:
        curr=nextGen(cells)
    return curr

def nextGen(cells){

 #if(!Array.isArray(cells) || !cells.length || typeof cells == undefined || cells==[[]]){
 #   return cells;}//end empty/isArray check
  else{ //Big Else  
    ht=cells.length+2;
    wt=cells[0].length+2;
  
var f = new Array();
for (i=0;i<ht;i++) {
 f[i]=new Array();
 for (j=0;j<wt;j++) {
  f[i][j]=0;
 }
}
  nextCells=f;
  #i =0;
  #j = 0;
  
  for (i=0; i < ht; i++){
   for (j=0; j < wt; j++){
    var up=0;
    var down = 0;
    var right=0;
    var left = 0;
    var upleft=0;
    var upright=0;
    var downleft=0;
    var downright=0;
    if (i!=0) {
      up=cells[i-1][j];
      if(j!=0){
        upleft=cells[i-1][j-1];
      }
      if(j!=wt-1){
        upright=cells[i-1][j+1];
      }
    }
    if (i!=ht-1) {
      down=cells[i+1][j];
      if(j!=0){
        downleft=cells[i+1][j-1];
      }
      if(j!=wt-1){
        downright=cells[i+1][j+1];
      }
    }
    if (j!=0) {left=cells[i][j-1];}
    if (j!=wt-1) {right=cells[i][j+1];}
    
    var nbrs=up+down+left+right+upright+upleft+downright+downleft;
    console.log("nbrs is ",nbrs);

    var currgen=cells[i][j];
    console.log("currgen is ",currgen);
    var nextg=0;
    if(currgen==0){//deadcell
      if (nbrs==3){//make live
        nextg=1;
      }
    }//end if deadcell
    else{//livecell
      if(nbrs==2 || nbrs==3) nextg=1;
    }//end livecell else
    nextCells[i][j]=nextg;
    }//end jfor
   }//end ifor
  return nextCells;
 }//end Big Else
}//end Function