import os
import codecs
import json
import sys

class MySettings(object):
	def __init__(self, settingsfile=None):
		try:
			with codecs.open(settingsfile, encoding="utf-8-sig", mode="r") as f:
				self.__dict__ = json.load(f, encoding="utf-8")
		except IOError as ex:
			self.Message = "Now playing {0}!"
		
		self.Initialized = False

		

	def GetDonationsUrl(self):
		return "https://streamlabs.com/api/v5/donation-goal/data/?token=" + self.DonationToken

	def Reload(self, jsondata):
		self.__dict__ = json.loads(jsondata, encoding="utf-8")
		return

	def Save(self, settingsfile):
		try:
			with codecs.open(settingsfile, encoding="utf-8-sig", mode="w+") as f:
				json.dump(self.__dict__, f, encoding="utf-8")
		except:
			Parent.Log(ScriptName, "Failed to save settings to file.")
		return