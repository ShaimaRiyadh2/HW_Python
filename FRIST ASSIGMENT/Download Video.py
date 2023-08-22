import pytube
print("Download video form web by python")
url = input('Enter video url:')
pytube.YouTube(url).streams.get_highest_resolution().download('Desktop')
print("The Download is Done*_*")
