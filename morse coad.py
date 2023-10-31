morse_code=['.-','-...','-.-.','-..','.','..-.','--.',
            '....','..','.---','-.-','.-..','--','-.',
            '---','.--.','--.-','.-.','...','-','..-',
            '...-','.--','-..-','-.--','--..','.----',
            '..---','...--','....-','.....','-....',
            '--...','---..','----.','-----','/']
alnum=list("abcdefghijklmnopqrstuvwxyz1234567890 ")
while True:
    start=input("to continue press enter\n\t[to close press #]")
    if start!= '':
        print("\n unvalied syntex \t try again\n")
        continue
    else:break
while True:
    words=[]
    data=list(input("enter to code or decord :\n\t\t\t"))
    for i in data:
        if i in alnum:
            words.append(i)
        else:pass
    if data[0] in alnum:
        for i in words :
            print(morse_code[alnum.index(i)],end=' ')     
    if data[0]in ['.','-']:
        code,data='',data
        if data[-1]!=" ":
            data.append(" ")
        for i in data:
            if i==' ':
                print(alnum[morse_code.index(code)],end='')
                code=''
            else: code+=i
    if data[0]=='#':
        print("\n\t\t\t\t\tthanks for using")
        break
    print()
