void main(){
  
  List<int> temp;
  int tinggi  = 4;
  int lebar   = 6;

  for(int x = 0; x < tinggi; x++){
    temp = [];

    for(int y = 1; y <= lebar; y++){
      temp.add(y);
    }

    print(temp.join(" "));
  }
}