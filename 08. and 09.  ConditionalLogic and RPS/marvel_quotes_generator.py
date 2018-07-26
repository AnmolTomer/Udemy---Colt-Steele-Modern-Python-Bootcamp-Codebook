print("\nHeyy there! Welcome to Marvel quotes machine.\n")
print("What is your name human ?\n")
user_name = input()
print(f"\nHeyy {user_name}, select corresponding numbers in front of your favorite superhero/villain to get one or two quotes related to them ;) ")
print("\n 1. Captain America\n 2. Iron Man\n 3. Spiderman\n 4. Deadpool\n 5. Hulk\n 6. Thor\n 7. Thanos\n 8. Wolverine\n 9. Gamora\n 10. Groot\n")
char_name = input("Enter your superhero/villain serial no. here: ")

if char_name ==  "1":
    print(f"\nHeyy {user_name}, here are some Captain America quotes:\n")
    print("1. I don’t want to kill anyone. I don’t like bullies; I don’t care where they’re from.")
    print("2. I can do this all day.")
    print("3. Without its ideals — its commitment to the freedom of all men, America is a piece of trash!\n")

elif char_name == "2":
    print(f"\nHeyy {user_name}, here are some Ironman quotes:\n")
    print("1. “I TOLD YOU. I DON’T WANT TO JOIN YOUR SUPER-SECRET BOY BAND.”")
    print("2. WELL, PERFORMANCE ISSUES, IT’S NOT UNCOMMON. ONE OUT OF FIVE…")
    print("3. DOTH MOTHER KNOW YOU WEARETH HER DRAPES.")
    print("4. HAVE YOU EVER TRIED SHAWARMA… I DON’T KNOW WHAT IT IS, BUT I WANNA TRY IT.")
    print("5. IF THERE’S ONE THING I’VE PROVEN IT’S THAT YOU CAN COUNT ON ME TO PLEASURE MYSELF.")
    print("6. GENIUS, BILLIONAIRE, PLAYBOY, PHILANTHROPIST.")
    print("7. YOU KNOW, IT'S MOMENTS LIKE THESE WHEN I REALIZE WHAT A SUPERHERO I AM.\n")

elif char_name == "3":
    print(f"\nHeyy {user_name}, here are some Spiderman quotes:\n")
    print("1. Secrets have a cost, they are not for free.")
    print("2. You have a metal arm? Dude, that is so awesome!\n")


elif char_name == "4":
    print(f"\nHeyy {user_name}, here are some kickass Deadpool quotes:\n")
    print("1. Today was about as much fun as a sandpaper dildo.")
    print("2. You're probably thinking 'Whose balls did I have to fondle to get my very own movie'? I can't tell you his name, but it rhymes with 'pullverine.'")
    print("3. You don’t need to be a superhero to get the girl, the right girl will bring out the hero in you.")
    print("4. WAIT! You may be wondering why the red suit. Well, that's so bad guys don't see me bleed.")
    print("5. Whatever they did to me made me totally indestructible... and completely unfuckable.")
    print("6. Your right leg is Thanksgiving and your left leg is Christmas. Can I come and visit you between the holidays?")
    print("7. I didn't ask to be super, and I'm no hero. But when you find out your worst enemy is after your best girl, the time has come to be a fucking superhero.")
    print("8. Looks *are* everything. You ever heard David Beckham speak? It's like he mouth-sexed a can of helium. Think Ryan Reynolds got this far on his superior acting method?\n")


elif char_name == "5":
    print(f"\nHeyy {user_name}, here are some Hulk quotes:\n")
    print("1. Hulk, SMASH!\n")

elif char_name == "6":
    print(f"\nHeyy {user_name}, here are some Thor quotes:\n")
    print("1. Do I look to be in a gaming mood?")
    print("2. You people are so petty, and tiny.")
    print("3. You’re big. I’ve fought bigger.")
    print("4. You should know that when you betray me, I will kill you.")
    print("5. Fortunately, I am mighty!\n")

elif char_name == "7":
    print(f"\nHeyy {user_name}, here are some Thanos quotes:\n")
    print("1. Fun isn’t something one considers when balancing the universe. But this… does put a smile on my face.")
    print("2. When I’m done, half of humanity will still exist. Perfectly balanced, as all things should be. I hope they remember you.")
    print("3.You’re strong. But I could snap my fingers, and you’d all cease to exist.")
    print("4. I know what it’s like to lose. To feel so desperately that you’re right, yet to fail nonetheless. Dread it. Run from it. Destiny still arrives. Or should I say, I have.")
    print("5. The hardest choices require the strongest wills.\n")

elif char_name == "8":
    print(f"\nHeyy {user_name}, here are some Wolverine quotes:\n")
    print("1. You might remember that 'annoyed' is my natural state.")
    print("2. I'm the best there is at what I do but what I do best isn't very nice.")
    print("3. Sometimes, when you cage the beast, the beast gets angry.")
    print("4. Nature made me a freak. Man made me a weapon. And God made it last too long.\n")

elif char_name == "9":
    print(f"\nHeyy {user_name}, here are some Gamora quotes:\n")
    print("1. I go by many names, Earthian, but I'm sure the one that most know me by is Gamora, the deadliest woman in the whole galaxy.")
    print("2. I am going to die surrounded by the biggest idiots in the galaxy.")
    print("3. Touch me, and the only thing you're gonna feel is a broken jaw.\n")

elif char_name == "10":
    print(f"\nHeyy {user_name}, here are some Groot quotes:\n")
    print("1. I am groot! ^_^")

else:
    print(f"Bad luck {user_name}. To get quotes just enter a number like 1 or 4. Program will exit now. Try running it again if you need a quote. :) \n")