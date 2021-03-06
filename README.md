Baker
=====

[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)

## About
With this tool you can convert one or multiple videos and pack them into MKV containers with subtitles, audio tracks and fonts. It is made with anime series in mind to adapt 10-bits rips for convenient storage and playing on weak devices, lacking power with no hardware acceleration for 10-bit videos present as of today.

### Key features
* convert 10-bit video to 8-bit with adjusted settings using 8-bit x264 encoder
* pack video with external subtitles, audio tracks, fonts using mkvmerge
* process series of files
* CLI and GUI versions

## Prerequisites
To use code "as is" your system has to meet some requirements:

* OS: Windows
* Python 3 (developed with 3.4)
* PyQt 4.11

## Build
To build an executable with supplied scripts you'll need additionally:

* PyInstaller - just run it with provided spec-files as only parameter.

You can also use built executables from releases, everything needed is supplied with them.

## Configuration
Basic settings are supplied through config-file in JSON format:

* `open_path` - default path which is opened in folder select prompt
* `tools_location` - folder where x264.exe and mkvmerge.exe are stored or will be downloaded by GUI-version
* `x264` - any performance parameters for x264.exe (see it's documentation)

## Usage

### GUI
1. run main&#46;py with Python or Baker.exe straight
2. choose folder witch contains video file(s) and subfolder(s) with additions
3. pick desired actions on the main Windows
4. press "Bake!" button
5. wait for it to complete (progress bar for files and overall are provided)

### CLI
Run baker&#46;py with Python or BakerCore.exe providing necessary parameters and wait for completion.

#### Parameters
* `-p <absolute path>` - absolute path to a folder with video files
* `-a <folder name>` (optional) - name of the subfolder inside main folder (provided with -p flag) containing desired audio-tracks
* `-s <folder name>` (optional) - name of the subfolder inside main folder (provided with -p flag) containing desired subtitles
* `-f <number>` - file number to proceed from
* `-t <number>` - file number to proceed last
* `-P <x264 mode name>` (optional) - x264 presets (ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow, placebo).
If supplied - overwrites all parameters set in config file.
More info can be found here: https://trac.ffmpeg.org/wiki/Encode/H.264#a2.Chooseapreset
* `-c` (optional) - file needs to be encoded (converted)
* `-v` (optional) - toggles output from x264 and mkvmerge

## Troubleshooting
Add `-d` parameter to script/executable to get debug output to console and/or file.