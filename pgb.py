import random
ppcchoice=["Papel", "Gunting", "Bato"]
userchoice=["Papel","Gunting","Bato"]
#userChoice=none

def function():
	userWinCtr=0
	pcWinCtr=0;
	while pcWinCtr <3 and userWinCtr <3:

		print("Bato bato pik!")
		print("Game options:")
		print("(P)apel")
		print("(G)unting")
		print("(B)ato")

		enterChoice= input("Enter your choice: ")
		p=0
		g=1
		b=2

		if enterChoice.lower() == 'p':
			tempUserChoice=userchoice[p]
			print(userchoice[p])
		elif enterChoice.lower() == 'g':
			tempUserChoice=userchoice[g]
			print(userchoice[g])
		elif enterChoice.lower() == 'b':
			tempUserChoice=userchoice[b]
			print(userchoice[b])
		else:
			print("Invalid input! Please choose from the game options!")
			continue;
		
		pcchoice=random.randint(0, 2)
		print("Pc choice is: ",ppcchoice[pcchoice])
		if ppcchoice[pcchoice] == tempUserChoice:
			print("Draw!")
		elif ppcchoice[pcchoice] == "Gunting":
			if tempUserChoice == "Bato":
				print("Player wins!")
				userWinCtr=userWinCtr+1
			else:
				print("Computer wins!")
				pcWinCtr=pcWinCtr+1
		elif ppcchoice[pcchoice] == "Bato":
			if tempUserChoice == "Papel":
				print("Player wins!")
				userWinCtr=userWinCtr+1
			else:
				print("Computer wins")
				pcWinCtr=pcWinCtr+1
		elif ppcchoice[pcchoice] == "Papel":
			if tempUserChoice == "Gunting":
				print("Player wins!")
				userWinCtr=userWinCtr+1
			else:
				print("Computer wins")
				pcWinCtr=pcWinCtr+1
		else:
			print("Invalid")

		print("User win: ",userWinCtr)
		print("Pc win: ",pcWinCtr)



function()

print("GAME OVER!")