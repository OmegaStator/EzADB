No more command lines for ADB
# Welcome EzADB

EzADB is the easiest tool to run ADB commands, say goodbye to the need of memorizing ADB commands, because now they are as simple to use as a command-line interface




## System requirements

While this has been tested only on windows for the moment, this app supports windows, linux and macOS. You will also need python (obviously)


## Contributing

You can obviously contribute to this project. Just pointing out some bugs and give us feature ideas are already a great help and if you are courageous, you can also try to fix the bugs by yourself


## Installation

no installation is needed, you only need Python with the Subprocess and Platform module installed
    
## Roadmap

- FastBoot support

- More commands (there will never be enough)

- Giving out more infos about the connection (SCRCPY feature)

- A real interface


## Run Locally

Because it's provided as ready-to-run, you can just clone the repo

```bash
  git clone https://github.com/omegastator/ezadb
```

Go to the project directory

```bash
  cd EzADB
```
and just run


```bash
  EzADB.py
```
## Support

For support, please send issues request, if they are not bug related, please contact me at xblade720.gamer@proton.me

## What can you do with this ?

- Start and stop ADB server
- List connected ADB devices
- Install single-Apk and splitted-apk apps
- Uninstall packages
- See all packages installed (currently broken, shows only system packages, might be because of my testing device)
- Use [SCRCPY](https://github.com/Genymobile/scrcpy)
## Known issues

- adb_package_list can only list system packages (migth be because of my test device)
- ~~Clearscreen is using the windows shell variant "cls", as a temporary fix, you can change "cls" to "clear" in EzADB.py~~ fixed since 24/02/25

## Licenses

This app is provided with the [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) license, that you can read at https://www.gnu.org/licenses/gpl-3.0.en.html
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)

While this program is under GPLv3 license, this program integrates the full version of [Android SDK Platform tools](https://developer.android.com/tools/releases/platform-tools) (also known as ADB platform tools) and [scrcpy](https://github.com/Genymobile/scrcpy), both of them are under the Apache 2.0 license that you can find [here](https://www.apache.org/licenses/LICENSE-2.0) or at https://www.apache.org/licenses/LICENSE-2.0
