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
    num(NumMod),
    Num < 10 -> write('Pick up the pace, you can do this. ');
    Num < 20 -> write('Good job. You are on the right track. ');
    Num < 30 -> write('Keep it up. ');
    Num < 40 -> write('It is almost Friday. You got this. '); 
    Num < 50 -> write('Now you are getting there. '); 
    Num < 60 -> write('You are doing great. ');
    Num < 70 -> write('Awesome job. ');
    Num < 80 -> write('You are the best! ');
    Num < 90 -> write('Is this a new record? ');
    write('Wow! Exceptional job this week! ').