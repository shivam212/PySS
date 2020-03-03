from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import glob
import subprocess
import time
gauth = GoogleAuth()
# gauth.LocalWebserverAuth()
# print(s)
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")

# gauth.SaveCredentialsFile()
drive = GoogleDrive(gauth)
while 1:
	subprocess.call(
	    ["/usr/bin/open", "-W", "-n", "-a", "/Applications/Utilities/Screenshot.app"]
	    )
	print("if satisified type 1 else 0")
	n = int(input());
	if n:
		break
time.sleep(1)
s=glob.glob("*.png")

file1 = drive.CreateFile()
file1.SetContentFile(s[0])
file1.Upload()
print("The link is ---> ")

permission = file1.InsertPermission({
                        'type': 'anyone',
                        'value': 'anyone',
                        'role': 'reader'})

print(file1['alternateLink'])

os.remove(s[0])

