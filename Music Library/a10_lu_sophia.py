# Sophia Lu, sjlu@usc.edu
# ITP 115, Spring 2021
# Assignment 10
# Description:
# This program simulates a user's music library

# import
import MusicLibraryHelper
import random

def displayMenu():
    print()
    print("Welcome to Your Music Library")
    print("Options:")
    print("\t1) Display library")
    print("\t2) Display all artists")
    print("\t3) Add an album")
    print("\t4) Delete an album")
    print("\t5) Delete an artist")
    print("\t6) Search library")
    print("\t7) Generate a random playlist")
    print("\t8) Make your own playlist")
    print("\t9) Exit")


def displayLibrary(musicLibDictionary):
    # get list of all keys/artists
    artists = list(musicLibDictionary.keys())
    for artist in artists:
        print("Artist:", artist)
        print("Albums:")
        # for loop for each album
        for album in musicLibDictionary[artist]:
            print("\t-", album)

def displayArtists(musicLibDictionary):
    print("Displaying all artists:")
    artists = list(musicLibDictionary.keys())
    for artist in artists:
        print("\t-", artist)

def addAlbum(musicLibDictionary):
    artist = input("Enter artist: ").title()
    album = input("Enter album: ").title()
    # creating list with all artist names
    artists = list(musicLibDictionary.keys())
    # check to see if artist is already in dictionary
    if artist in artists:
        if album not in musicLibDictionary[artist]:
            musicLibDictionary[artist].append(album)
    # if not in dictionary, create new pairing
    else:
        musicLibDictionary[artist] = [album]

# function: deleteAlbum
# return value of Boolean
def deleteAlbum(musicLibDictionary):
    artist = input("Enter artist: ").title()
    album = input("Enter album: ").title()
    artists = list(musicLibDictionary.keys())
    # artist and album must both be in dictionary
    if artist in artists and album in musicLibDictionary[artist]:
        success = True
        musicLibDictionary[artist].remove(album)
        # if there are no more albums in artist's list, delete artist
        if len(musicLibDictionary[artist]) == 0:
            del musicLibDictionary[artist]
    else:
        success = False
    # return value
    return success

def deleteArtist(musicLibDictionary):
    artist = input("Enter artist: ").title()
    artists = list(musicLibDictionary.keys())
    # check if artist is in dictionary first
    if artist in artists:
        success = True
        del musicLibDictionary[artist]
    else:
        success = False
    return success

def searchLibrary(musicLibDictionary):
    value = input("Please enter a search term: ")

    # artists
    print("Artists containing '" + value + "'")
    artists = list(musicLibDictionary.keys())
    # count to keep track of whether there are albums/artists with the search term
    artistCount = 0
    # for loop for checking and printing artists with search term
    for artist in artists:
        if value.title() in artist:
            print("\t-", artist)
            artistCount = 1
    if artistCount == 0:
        print("\tNo Results")

    # albums
    print("Albums containing '" + value + "'")
    # turn albums into one list
    allAlbums = []
    for artist in artists:
        albumList = musicLibDictionary[artist]
        for item in albumList:
            allAlbums.append(item)
    # count to keep track
    albumCount = 0
    # for loop for checking and printing albums with search term
    for album in allAlbums:
        if value.title() in album:
            print("\t-", album)
            albumCount = 1
    if albumCount == 0:
        print("\tNo Results")

def generateRandomPlaylist(musicLibDictionary):
    print("Here is your random playlist:")
    artists = list(musicLibDictionary.keys())
    for artist in artists:
        albumsList = musicLibDictionary[artist]
        numAlbums = len(albumsList)
        # picking random album
        pick = random.randrange(numAlbums)
        # appending album to playlist
        song = albumsList[pick]
        # nicely printing out playlist
        print("\t-" + song + " by " + artist)

def generateCustomPlaylist(musicLibDictionary):
    # empty string for playlist
    playlist = []
    # making list of all current artists
    artists = list(musicLibDictionary.keys())
    # condition for while loop
    repeat = "y"
    while repeat == "y":
        # for printing playlist
        print("Your playlist so far:")
        if len(playlist) > 0:
            for item in playlist:
               print("-", item)
        print("----")

        # loop through artist options
        for artist in artists:
            print(str(artists.index(artist)) + ") " + artist)
        # user input for choosing artist
        artistIndex = input("Select an artist from the list by entering its number: ")
        # error checking
        while artistIndex.isdigit() is False or int(artistIndex) not in range(0, len(artists)):
            print("*Error, please try again")
            artistIndex = input("Select an artist from the list by entering its number: ")
        artistIndex = int(artistIndex)
        chosenArtist = artists[int(artistIndex)]
        chosenArtist = musicLibDictionary[chosenArtist]

        # loop through artist's albums
        for album in chosenArtist:
            print(str(chosenArtist.index(album)) + ") " + album)
        # user input for choosing album
        albumIndex = input("Select an album from the list by entering its number: ")
        # error checking
        while albumIndex.isdigit() is False or int(albumIndex) not in range(0, len(chosenArtist)):
            print("*Error, please try again")
            albumIndex = input("Select an album from the list by entering its number: ")
        albumIndex = int(albumIndex)
        chosenAlbum = chosenArtist[albumIndex]
        # add album and artist to playlist
        albumArtistStr = chosenAlbum + " by " + artists[artistIndex]
        playlist.append(albumArtistStr)

        # asking if they would like to continue
        repeat = input("Would you like to continue building your playlist (y/n)? ")
        # error checking
        while repeat != "y" and repeat != "n":
            print("Invalid input.")
            repeat = input("Would you like to continue building your playlist (y/n)? ")
    # exit while loop output
    print("Your completed playlist:")
    for item in playlist:
        print("-", item)

def main():
    library = MusicLibraryHelper.loadLibrary("musicLibrary.dat")
    selection = 0
    while selection != 9:
        displayMenu()
        selection = input("> ")
        # error checking to make sure correct input
        while selection.isdigit() is False or int(selection) not in range(1, 10):
            print("Invalid option")
            selection = input("> ")
        # make sure selection is int
        selection = int(selection)
        print()
        if selection == 1:
            displayLibrary(library)
        if selection == 2:
            displayArtists(library)
        if selection == 3:
            addAlbum(library)

        if selection == 4:
            success = deleteAlbum(library)
            if success == True:
                print("Delete album success!")
            else:
                print("Delete album failed.")

        if selection == 5:
            success = deleteArtist(library)
            if success == True:
                print("Delete artist success!")
            else:
                print("Delete artist failed.")

        if selection == 6:
            searchLibrary(library)
        if selection == 7:
            generateRandomPlaylist(library)
        if selection == 8:
            generateCustomPlaylist(library)
        if selection == 9:
            MusicLibraryHelper.saveLibrary("musicLibrary.dat", library)
            print("Saving music library . . .")
            print("Goodbye!")

# calling main
main()