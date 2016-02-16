import os.path
import urllib2
import subprocess
import hashlib

import config

def getServerPatchInfo():
    url = config.patchFileUrl
    serverVersion = 0
    patchBaseUrl = ""

    response = urllib2.urlopen(urllib2.Request(url)).readlines()

    for line in response:
        if "main_version" in line:
            serverVersion = line.replace("main_version=", "").replace("\r", "").replace("\n", "")

        if "main_ftp" in line:
            patchBaseUrl = line.replace("main_ftp=", "").replace("\r", "").replace("\n", "")

        if serverVersion and patchBaseUrl:
            break

    patchBaseUrl = "ftp://" + patchBaseUrl + "/" + serverVersion

    return { "version": serverVersion, "baseUrl": patchBaseUrl }


# def getLocalPatchInfo():
#     #NOTE: not used anymore
#     filePath = config.versionFilePath
#     if os.path.isfile(filePath):
#         # version file found, get patch version
#         f = open(filePath, 'rb')
#         data = f.read()
#         # credit to http://code.activestate.com/recipes/510399-byte-to-hex-and-hex-to-byte-string-conversion/
#         data = ''.join( [ "%02X" % ord( x ) for x in data ] ).strip()
#         f.close()
#
#         # credit to http://stackoverflow.com/questions/209513/convert-hex-string-to-int-in-python
#         version = int(("0x" + data[2] + data[3] + data[0] + data[1]), 0)
#
#     else:
#         version = 0
#
#     return { "version": version }


def getFileInfo(serverPatchInfo):
    baseUrl = serverPatchInfo["baseUrl"]
    serverVersion = int(serverPatchInfo["version"])

    url = config.patchFileListUrl % (str(serverVersion), str(serverVersion))

    result = []

    process = subprocess.Popen([config.curlPath, url], stdout=subprocess.PIPE)
    out = process.communicate()

    response = out[0].rstrip("\n").split("\n")

    #TODO: error handling

    for item in xrange(1, len(response)):
        item = response[item].split(",")
        result.append(
            {
                "filePath": baseUrl + "/" + item[0],
                "size": item[1],
                "md5": item[2]
              }
        )

    return result



def getFileList():
    serverPatchInfo = getServerPatchInfo()
    fileInfo = getFileInfo(serverPatchInfo)

    return fileInfo

#TODO: check md5 of downloaded file to avoid extra downloads