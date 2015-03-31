#=======================================================================
# Answers Python Library. 
# Copyright Calvin Hartwell 2015. 
# Distributed under the MIT License.
# (See accompanying file LICENSE or copy at http://opensource.org/licenses/MIT)
#=======================================================================

import subprocess 	# Used for for running subprocesses (shell execution) and reading output
import json 		# Used for reading JSON (answers files)
import os			# Used for working with files/loading answers file
import select		# Used to pull data out of the file descriptors (reading process output)
import pty			# Used for terminal utils, openpty to communicate with subprocesses

# Answers Library (Answers Class)
class Answers(object):
	# Can execute commands with or without a list of answers
	def __init__(self, executable=None, answersRaw=None):
		self._executable = executable
		self._answersRaw = answersRaw
		self._answers = None
		self._logFileHandle = None
		self.defaultAnswer = "y"
		self.postAnswerCommand = "\r"
		self.logName = "answers.log"
		self.timeoutInSeconds = 1
		self.maxReadWriteSize = 2048
		self.debugMode = False 
		self.logMode = False
		self.postAnswerMode = True 
		self.defaultAnswerMode = False
		self.hideExceptionsMode = True

	# Attemps to load answers JSON file
	def _LoadAnswers(self):
		# Check if file exists first
		if os.path.isfile(self._answersRaw) == True:
			answersFile = open(self._answersRaw)
			self._answers = json.load(answersFile)
		else: # Try to load it as raw JSON
			self._answers = json.loads(self._answersRaw)	
		
		self._DebugPrint ("Answers Loaded: %s" % self._answers)

	# Attempts to Log To File 
	def _LogToFile(self, message):
		try:
			if self._logFileHandle is None:
				self._logFileHandle = open(self.logName, "w")
				self._logFileHandle.write(message + "\n")
		except Exception as ex:
			if self.debugMode:
				print(message)
			if not self.hideExceptionsMode:
				raise ex

	# Print Wrapper which can be used to print and log output
	def _DebugPrint(self, message):
		if self.debugMode:
			print(message)
		if self.logMode:
			self._LogToFile(message)

	# Execute Subprocess with answers file
	def _ExecProcessWithAnswers(self):
		try:
			# Master and slave file descriptors for low level output
			writeMFD, writeSFD = pty.openpty()
			readMFD, readSFD = pty.openpty()

			self.process = subprocess.Popen( self._executable,
										stdout=readSFD,
										#stderr=readSFD, 
										stdin=writeSFD,
										universal_newlines=True, shell=True)

			while True:
				# Read data from process using file descriptor and select
				rlist, _, _, = select.select([readMFD], [], [], self.timeoutInSeconds)

				if rlist:
					data = os.read(readMFD, self.maxReadWriteSize)
					self._DebugPrint("Subprocess: %s" % data.strip())
					answerFound = False
					for answer in self._answers['answers']:
						if answer['question'] in data:
							answerFound=True
							if self.postAnswerMode:
								os.write(writeMFD, answer['answer'] + self.postAnswerCommand)
							else:
								os.write(writeMFD, answer['answer'])	
							self._DebugPrint("Answer: %s" % answer['answer'])
					if self.defaultAnswerMode and not answerFound:
						if self.postAnswerMode:
							os.write(writeMFD, self.defaultAnswer + self.postAnswerCommand)
						else:
							os.write(writeMFD, self.defaultAnswer)			
					if not data:
							self._DebugPrint("Subprocess received EOF command -- exiting.")
							break
				elif self.process.poll() is not None:
					self._DebugPrint("Subprocess has ended -- exiting.")
					break

		except KeyboardInterrupt as ex:
				self._DebugPrint("Caught Ctrl+C (force close application) -- exiting.")
				if not self.hideExceptionsMode:
					raise ex
		except Exception as ex:
				self._DebugPrint("Unhandled Exception: %s" % ex)
				if not self.hideExceptionsMode:
					raise ex
		finally:
			 	self._DebugPrint("Cleaning up...")
				os.close(writeSFD)
				os.close(writeMFD)
				os.close(readSFD)
				os.close(readMFD)
				if self.process.poll() is None:
					self.process.kill()

	# Execute Subprocess without answers file
	def _ExecProcess(self):
		try:
			# Master and slave file descriptors for low level output
			readMFD, readSFD = pty.openpty()

			self.process = subprocess.Popen( self._executable,
										stdout=readSFD, 
										#stderr=readSFD,
										universal_newlines=True, shell=True)

			while True:
				# Read data from process using file descriptor and select
				rlist, _, _, = select.select([readMFD], [], [], self.timeoutInSeconds)

				if rlist:
					data = os.read(readMFD, self.maxReadWriteSize)
					self._DebugPrint("Subprocess: %s" % data.strip())				
					if not data:
							self._DebugPrint("Subprocess received EOF command -- exiting.")
							break
				elif self.process.poll() is not None:
					self._DebugPrint("Subprocess has ended -- exiting.")
					break

		except KeyboardInterrupt as ex:
				self._DebugPrint("Caught Ctrl+C (force close application) -- exiting.")
				if not self.hideExceptionsMode:
					raise ex
		except Exception as ex:
				self._DebugPrint("Unhandled Exception: %s" % ex)
				if not self.hideExceptionsMode:
					raise ex
		finally:
			 	self._DebugPrint("Cleaning up...")
				os.close(readSFD)
				os.close(readMFD)
				if self.process.poll() is None:
					self.process.kill()

	# Run automation
	def Execute(self):
		try:
			if self._executable is not None:
				if self._answersRaw is None:
					self._ExecProcess()
				else:
					self._LoadAnswers()
					self._ExecProcessWithAnswers()
		except Exception as ex:
			if self.debugMode:
				self._DebugPrint(ex)
			if self.hideExceptionsMode:
				raise ex

