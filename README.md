# Welcome EzADB

EzADB is the easiest tool to run ADB commands, say goodbye to the need of memorizing ADB commands, because now they are as simple to use as a text UI


## System requirements

Actual versions are tested on EndeavourOS (ArchLinux), there is no warranty that it will work on other systems (please report if they are not working correctly)

|Requirements|Required|
|---|---|
|Python|>=3.0|
|OS|Windows, Linux, MacOS |

## Contributing

You can obviously contribute to this project. Just pointing out some bugs and give us feature ideas are already a great help and if you are courageous, you can also try to fix the bugs by yourself


## Installation

No installation is needed, you only need Python installed
    
## (Maybe) Upcoming features

- FastBoot support

- More commands (there will never be enough)

- Giving out more infos about the connection (SCRCPY feature)

- ~~A real interface~~ i suck at making interfaces


## Run Locally

Because it's provided as ready-to-run, you can just clone the repo

```bash
  git clone https://github.com/OmegaStator/EzADB.git
```

Go to the project directory

```bash
  cd EzADB
```
and just run


```bash
  python EzADB.py
```
## Support

For support, please send issues request

## What can you do with this ?

- Start and stop ADB server
- List connected ADB devices
- Install single-file APK and splitted APK apps
- Uninstall packages
- See all packages installed (currently broken, shows only system packages, might be because of my testing device)
- Use [SCRCPY](https://github.com/Genymobile/scrcpy)

## Known issues

- ~~Clearscreen is using the windows shell variant "cls", as a temporary fix, you can change "cls" to "clear" in EzADB.py~~ Fixed since 24/02/25
- ~~25/07/25 : on linux, every command sends error 13 permission denied, system version of android-tools and scrcpy will be required~~ Fixed since 05/11/25

## Licenses

This app is provided with the [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) license, that you can read at https://www.gnu.org/licenses/gpl-3.0.en.html
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)

While this program is under GPLv3 license, this program integrates the full version of [Android SDK Platform tools](https://developer.android.com/tools/releases/platform-tools) (also known as ADB platform tools) and [scrcpy](https://github.com/Genymobile/scrcpy), both of them are under the Apache 2.0 license that you can find [here](https://www.apache.org/licenses/LICENSE-2.0) or at https://www.apache.org/licenses/LICENSE-2.0
