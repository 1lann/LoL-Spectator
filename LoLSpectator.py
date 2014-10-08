#!/usr/bin/python
# coding: utf-8
# ¬

import subprocess
import re
import sys
import os

def spectateGame(rawData):
	spectateMatch = re.compile('(spectator [\w.]*:\d{1,5} \S* \d{8,12} [A-Za-z0-9]*)')
	print(rawData.replace("\n", ""))
	match = spectateMatch.search(rawData.replace("\n", ""))
	if match:
		command = 'cd /Applications/League\ of\ Legends.app/Contents/LoL/RADS/solutions/lol_game_client_sln/releases/*/deploy/LeagueOfLegends.app/Contents/MacOS\nriot_launched=true ./LeagueOfLegends 8394 LoLLauncher "" "{}"'

		devNull = open(os.devnull, 'w')

		try:
			subprocess.Popen(command.format(match.groups()[0]), shell=True, stdout=devNull, stderr=devNull)
		except:
			command = """
			display dialog "There was an error while trying to open the client! Note that your League of Legends application must be stored under /Applications/League of Legends.app" ¬
			with title "LoL Spectator" ¬
			with icon caution ¬
			buttons {"OK"}
			"""
			subprocess.call("osascript -e '{}'".format(command), shell=True)
	else:
		command = """
		display dialog "The spectate data could not be found from that text! The program will now exit." ¬
with title "LoL Spectator" ¬
with icon caution ¬
buttons {"OK"}
		"""
		subprocess.call("osascript -e '{}'".format(command), shell=True)

askDialog = """
display dialog "Enter Any Spectate URI or Command" default answer "" ¬
with title "LoL Spectator"
"""

if len(sys.argv) > 1:
	contents = ""
	try:
		contents = open(sys.argv[1]).read()
	except:
		command = """
		display dialog "Error while reading file!" ¬
	with title "LoL Spectator" ¬
	with icon caution ¬
	buttons {"OK"}
		"""
		subprocess.call("osascript -e '{}'".format(command), shell=True)
	spectateGame(contents)
else:
	response = subprocess.check_output("osascript -e '{}'".format(askDialog), shell=True)
	spectateGame(response)
