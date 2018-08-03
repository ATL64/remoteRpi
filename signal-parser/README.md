This script will execute the signals recorded in a session, i.e. all the 
output from pilight-debug when trying to capture signals.

If this output should look something like


Raw code:

1755 78 273 117 234 117 234 117 234 117 195 117 234 117 234 117 234 117 234 117 

--[RESULTS]--

time:		Tue Jul 17 14:55:34 2018
hardware:	433gpio
pulse:		4
rawlen:		376
pulselen:	475

Raw code:

47 235 94 188 94 235 94 235 141 235 94 235 94 235 94 235 94 235 94 235 94 235 94 
 
--[RESULTS]--

time:		Tue Jul 17 14:55:35 2018
hardware:	433gpio
pulse:		12
rawlen:		139
pulselen:	222

Raw code:

220 110 220 88 198 110 176 88 198 88 198 44 220 110 176 88 176 88 176 88 176 110 176
 
--[RESULTS]--


with longer series of numbers which I shortened for readibility, 
and any number of signals detected.

To run the script, first save the above output to a text file and then use the path as argument:

`python3 signal-parser.py /Users/frosterchosky/Documents/Things/useful_commands`




