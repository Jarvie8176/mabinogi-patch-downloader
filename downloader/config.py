patchFileUrl = "http://patch.mabinogi.jp/patch/patch.txt"
patchFileListUrl = "ftp://download2.nexon.co.jp/mabinogi/patch/%s/%s_full.txt"
curlPath = "./curl.exe"
downloaderPath = "./aria2c.exe"
urlFileName = "./files.txt"
# saveDirName is where the file should be saved in
saveDirName = "download"
downloaderParameters = "--input-file=\"%s\" --max-connection-per-server=16 --max-concurrent-downloads=20 --dir=\"%s\""\
                       % (urlFileName, saveDirName)