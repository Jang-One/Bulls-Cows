logo = """ 
                                       _             _  _      
                               ___    | |           | || |     
  ___   ___  __      __ ___   ( _ )   | |__   _   _ | || | ___ 
 / __| / _ \ \ \ /\ / // __|  / _ \/\ | '_ \ | | | || || |/ __|
| (__ | (_) | \ V  V / \__ \ | (_>  < | |_) || |_| || || |\__\ 
 \___| \___/   \_/\_/  |___/  \___/\/ |_.__/  \__,_||_||_||___/
                            
""";
print(logo);

randomNum = getRandomNum();

while True:
    # getInput
    inputNum = [];
    for i in range(4):
        tmp=int(input(i+1+'번째 수를 입력해주세요'));
        inputNum.append(tmp);
    # checkInput
    bulls,cows = checkInput();
    print('bulls :' + bulls);
    print('cows :' + cows);
    if bulls == 4: 
        print('정답입니다!');
        break;




    




