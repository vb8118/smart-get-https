from pySmartDL import SmartDL

url = "https://testfileorg.netwet.net/testfile.org-1GB-%20Corrupt.zip"
output_file = "1GB-testlargefile.zip"

dl = SmartDL(url, output_file)
dl.start()

