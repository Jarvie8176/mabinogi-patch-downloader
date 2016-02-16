import io
import os
import signal
import atexit
import json
import time
import subprocess

import helper
import config
import test


def saveFileInfo():
    fileInfo = helper.getFileList()
    # fileInfo = test.sampleFileList

    with io.open(config.urlFileName, 'w') as outfile:
        for item in fileInfo:
            outfile.write(unicode(item["filePath"] +"\n"))

    return


def doDownload():
    command = config.downloaderPath + " " + config.downloaderParameters
    print command
    process = subprocess.Popen(command)

    #TODO: ensure process is terminated upon termination of python instance

    out = process.communicate()


if __name__ == "__main__":
    saveFileInfo()
    doDownload()