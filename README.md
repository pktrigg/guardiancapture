# guardiancapture
Toolkit to enable the automated capture of data at sea

ToDo

decide if we can use bash or python

capture on user defined interval, default per day (80*3600*24=6.9Mb/day) which is reasonable
capture to be in a simplae config file with Name, UDP port as parameters
	AIS, 5019
	MarineStar1, 5020
	SBES, 2013
	etc
shell script will read each line of file, and spin up either NC or python script to capture data to disc
shell scriptwill auto start when system boots
crontab will ensure each instance is running (maybe this implies a different script per sensor?
crontab will run every 30 seconds to ensure all scripts are running
files will be autonamed in ascending order sequentially <counter>-<SensorName>-<Year><Month><Day>-<Hour><Minute><Second>.log
files will be in differnt directories per sensor

need a web page sowe can see the files created
web page to be based on python

