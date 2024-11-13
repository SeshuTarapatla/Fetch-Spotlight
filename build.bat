@echo off

echo Build Windows executable using Nuitka
python -m nuitka --onefile ".\windows-spotlight.py" ^
    --output-filename="Fetch Spotlight" ^
    --windows-icon-from-ico=".\icons\spotlight.ico" ^
    --include-data-files=".\icons\spotlight.ico"="icons\spotlight.ico"

echo Nuitka: Deleting cache directories.
rmdir /S /Q ".\windows-spotlight.build"
rmdir /S /Q ".\windows-spotlight.dist"
rmdir /S /Q ".\windows-spotlight.onefile-build"
