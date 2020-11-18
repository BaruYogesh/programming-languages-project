num(0) :- write('The Best Way To Get Started Is To Quit Talking And Begin Doing.').
num(1) :- write('Do not Let Yesterday Take Up Too Much Of Today.').
num(2) :- write('It’s Not Whether You Get Knocked Down, It Is Whether You Get Up.').
num(3) :- write('Failure Will Never Overtake Me If My Determination To Succeed Is Strong Enough.').
num(4) :- write('We May Encounter Many Defeats But We Must Not Be Defeated.').
num(5) :- write('Whether You Think You Can Or Think You Can Not, You Are Right.').
num(6) :- write('The Man Who Has Confidence In Himself Gains The Confidence Of Others.').
num(7) :- write('The Only Limit To Our Realization Of Tomorrow Will Be Our Doubts Of Today.').
num(8) :- write('What You Lack In Talent Can Be Made Up With Desire, Hustle And Giving 110 Percent All The Time.').
num(9) :- write('Do What You Can With All You Have, Wherever You Are.').

enterYourPoints(Num):- 
    NumMod is Num mod 10,
    num(NumMod).