from pySmartDL import SmartDL

url = "https://sabnzbd.org/tests/internetspeed/50MB.bin"
output_file = "./1GB-testlargefile.zip"

dl = SmartDL(url, output_file)
dl.start()

