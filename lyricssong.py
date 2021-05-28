
print("Welcome to the Music World. U Can Select the Songs Displayed Below......\n")

def fun():
    
    print("Bad boy\nSahore Bahubali\nMaari\nKuch Kuch Hota hai\nPremam Malare\nSalam Rocky Bhai\nChampion\nFast&Furious We own it\nShape Of You\n")
    
while True:
    fun()    
    choice= input("Enter Name of the Song :").lower()
    if choice =="bad boy":
        with open ('badboy.txt','r') as song_lyrics:
            for line in song_lyrics.readlines():
                print(line)

    elif choice =="sahore bahubali":
        with open ('bahu.txt','r') as song_lyrics:
            for line in song_lyrics.readlines():
                print(line)

    elif choice =="champion":
        with open ('champion.txt','r') as song_lyrics:
            for line in song_lyrics.readlines():
                print(line)


    elif choice =="we own it":
        with open ('weownit.txt','r') as song_lyrics:
            for line in song_lyrics.readlines():
                print(line)

    elif choice =="salam rocky bhai":
        with open ('kgf.txt','r') as song_lyrics:
            for line in song_lyrics.readlines():
                print(line)
                
    elif choice =="maari":
        with open ('mari.txt','r') as song_lyrics:
            for line in song_lyrics.readlines():
                print(line)
                
    elif choice =="kuch kuch hota hai":
        with open ('kuch.txt','r') as song_lyrics:
            for line in song_lyrics.readlines():
                print(line)

    elif choice =="shape of you":
        with open ('shapeofu.txt','r') as song_lyrics:
            for line in song_lyrics.readlines():
                print(line)

    elif choice =="malare":
        with open ('premam.txt','r') as song_lyrics:
            for line in song_lyrics.readlines():
                print(line)

    
    else:
        print("Plzzzz Enter a valid song")
##        break
    var = input("Do you want to Continue to Next song.. Press c or Press q to exit: ")
    if var == "c":
        continue
    elif var == "q":
        print("Thank U ..............")
        break
            
