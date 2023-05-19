void main(){

  List<String> temp;
  int panjang = 10;
  int lebar   = 10;

  for(int x = 0; x < panjang; x++){
    temp = [];

    for(int y = 0; y < lebar; y++){
      temp.add("*");
    }

    print(temp.join(" "));
  }
}