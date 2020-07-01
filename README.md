Please do not judge me on sloppy coding and bad practices...
This tool was created in a short period of time and was just made to do a specific task
I wanted to sit and clean it up a bit, organize some functions in a better way
Define other methods, etc etc... Just general cleaning up and maintenance but I did not have any time to do it :)

Feel free to modify, organize and clean it up as you like but do leave comments and log messages explaining what you did

Also, all and any types of in code comments are appreciated and andy kind and form of criticizm is acceptable
I would really appreciate some constructive feedback and comments
Thanks!

+++++++++++++++++++INSTRUCTIONS+++++++++++++++++++++++++++++

Requirements:
		Python3.8(Version used while coding and testing the tool)
		Scapy

Setup Steps and Explanation:

Since I had to modify scapy source code to make IP spoofing faster 
I am also sending you the modified scapy file which you will have to 
substitute instead of the original scapy

In order to do this, go into you python3 scapy folder
(for my pc the location is: " /home/proximo/.local/lib/python3.6/site-packages/scapy")
you rename the python file called "sendrecv.py" to something else (eg. oldSendrecv.py , just to have the original version) then you take the sendrecv.py from this github and put it in the folder

The outcome should be that spoofed IP addresses are random, target ports are random and the size is random and everything changes with every iteration

"Sudo python3 ./udpflooder -src rand -p 999999 -s 999999 10.0.0.2"
*Six nines is value for random port and size*

