#Smart Playlist Intelligence System
n=int(input("Enter Number of songs: "))
songs=[0]*n
for i in range(n):
    songs[i]=int(input("Enter duration: "))

invalid=False
for s in songs:
    if s<=0:
        invalid=True
        break
        
if invalid:
    print("Invalid Playlist")
else:
    Total_Duration=sum(songs)
    cnt_song=len(songs)

    repeat=False
    for s in songs:
        if songs.count(s)>1:
            repeat=True
            break
    if Total_Duration<300:
        c="Too Short Playlist"
        r="Add more songs"
    elif Total_Duration>3600:
        c="Too Long Playlist"
        r="Remove Some Songs"
    elif repeat:
        c="Repetitive Playlist"
        r="Add Vareity"
    elif max(songs)-min(songs)<=300:
        c="Balanced Playlist"
        r="Good Listening session"
    else:
        c="Irregular Playlist"
        r="Make sure that duration vary reasonably"
    
    print("Total Duration: ",Total_Duration,"seconds")
    print("songs: ",cnt_song)
    print("Category: ",c)
    print("Recommendation: ",r)

