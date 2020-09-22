# c2_handler
twitter c2 handler for teaching purposes

Have managed to convert it to an exe in a way it bypasses AV and runs on a fully patched win10 machine.

It will poll the twitter account @TheRealFrankFo1 every 30s, could add some jitter here but have not currently had the need.

When a tweet has the hashtag #WouldYouKindly the text following it will be parsed and will execute a command.

Command = do some maths
Action = the calculator will open on the host, do several calculations and display a hidden message :)

Command = play me a song
Action = will play the bundled audio.mp3 on the host, this is something I would never give up.

![Image of Yaktocat](https://github.com/The1WhoPrtNocks/c2_handler/blob/master/calc.PNG)
