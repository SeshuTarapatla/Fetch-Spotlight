# Fetch-Spotlight
A python project that can fetch your current Windows Spotlight wallpaper into your library.

## What it does
Creates a new folder called "Windows Spotlight" in your Pictures library & copies your current Spotlight wallpaper into that folder.

File naming format : **"Windows-Spotlight-{Current_date}_{index}.jpg"**  
Index: Starts at 01 (and gets incremented if there is different wallpaper at same date).
  
## Build for windows
It is converted into Windows Executable using Python 3.12 and a library called Nuitka.

## Executable from release (Latest: [v1.0.0](https://github.com/SeshuTarapatla/Fetch-Spotlight/releases/tag/v1.0.0))
Windows Executable for the same source code:
* Download EXE and execute.
* It just opens a console and immediately closes once the process is complete.
* You can check your Wallpaper in Pictures > Windows Spotlight folder 📂.

‼️ If you face any issues with Antivirus - Please add it to the exclusions list.  
And if you want to see the logs. Open any terminal > Drag and drop the EXE to the terminal > Execute  

## Refs
1. Nuitka: https://github.com/Nuitka/Nuitka