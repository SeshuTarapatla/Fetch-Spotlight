# Fetch-Spotlight
A python project that can fetch your current Windows Spotlight wallpaper into your library.

## What it does
Creates a new folder "Windows Spotlight" in your Pictures library & copied your current Spotlight wallpaper into that folder.

File naming format : **"Windows-Spotlight-{Current_date}_{index}.jpg"**  
Index: Starts at 01 (and gets incremented if there is different wallpaper at same date).
  
## Build for windows
It is converted into Windows Executable using Python 3.12 and a library called Nuitka.

## Refs
1. Nuitka: https://github.com/Nuitka/Nuitka