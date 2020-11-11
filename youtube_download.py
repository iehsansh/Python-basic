# importing YouTube from pytube
from pytube import YouTube
print("Hi. If you like this little app, lets follow me on Instagram by @iEhsansh!\n\n\n\n")
# asking user to enter link
link = input("Enter the link ")
# showing user that the process has started
print("Downloding...")
# main code to download Video
YouTube(link).streams.first().download()
# showing user that the video has downloaded
print("""
    Video downloaded successfully
    made by: @iehsansh
    www.mattrin.com
    """)