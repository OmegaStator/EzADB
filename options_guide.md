# Adding the options
To add the options, add the options in one line with spaces seperating the options

Example :

    --option1 --option2 --option3


# SCRCPY
Theses options will let you modify the behaviour of SCRCPY function, here are a lot of options you can use


## OTG mode
-     --otg
        
    Launch scrcpy in OTG mode, useful if your device doesn't have ADB.

    Warning ! This will need a USB connection
    -     --keyboard=disabled
        Disables the keyboard when in OTG mode
    -     --mouse=disabled
        Disables the mouse in OTG mode
    -     -G / --gamepad=aoa
        Enables gamepads in OTG mode

## Audio and Video settings
-     --no-audio
    disables automatic audio routing to the computer (only used in android 11 SDK30 or higher, older androids don't support audio routing)

-     --no-video
    Disables video output, useful if you just want to control your device without having the screen

-     --audio-source=mic
    Instead of redirecting the system audio, will redirect the microphone audio (requires android 11/SDK 30 or higher)

-     --audio-source=playback
    Alternative method to recieve the audio on your device (requires android 13/SDK 33 to work)

-     --audio-dup
    Uses --audio-source=playback to keep the sound output on your device while SCRCPY is connected (like audio-source=playback, this needs android 13/SDK 33 to work)
    Warning : some apps are opt-out of this feature, so the audio won't be outputted

-     --audio-codec=
    - opus
    - aac
    - flac
    - raw

-     --audio-codec=opus --audio-encoder='com.example.encoder'
    Can be used if you have multiple audio encoders on your device and you want to select a specific one

-     --audio-bitrate=64K
    Lets you change the bitrate of the audio (lower=better performance, higher=better quality)

-     --audio-buffer=50
    Changes the value of the target audio buffer (lower=less lag, higher=smoother)

-     --video-buffer=50
    Same as the audio buffer feature, but for the video

## Recording

-     --record=filename
    Record the output and save it with the file name, the output container will depend on the file type you wrote
    - .mp4
    - .m4a
    - .aac
    - .mkv
    - .mka
    - .opus
    - .flac
    - .wav

-     --no-playback
    disable audio while recording

-     --time-limit=20
    Limits recording time (with time in seconds, this can also be used in normal screen mirroring)

## Virtual display

-     --new-display
    Will output the video of a virtual display instead of the main android one. Without one of the following options, the screen settings will be the same as your actual screen
    -     =1920x1080
        Sets resolution of the virtual display at what you indicate (here, 1920 by 1080) and the DPI of your main screen
    -     =/240
        Sets DPI at what you indicate (here, 240DPI) and the screen resolution of your main screen
    -     =1920x1080/240
        Mix of the two options explained above, sets a resolution and a DPI

-     --start-app=com.example.package
    Will start a specific app when the virtual screen is connected

-     --no-vd-system-decorations
    Will disable the UI on this screen, without the command --start-app, no render will be done. Reccomanded to use it if your device has a broken UI on the virtual display

-     --no-vd-destroy-content
    By default, when a virtual display is disconnected, all the apps that were running are closed, to prevent this, use this option

## General
-     --stay-awake / -w
    Prevents the device from going into sleep mode, only works if the device is connected through ADB by USB, resets when SCRCPY is disconnected

-     --screen-off-timeout=300
    changes the sleep timeout. Like --stay-awake, default value will be restored when disconnected

-     --turn-screen-off / -S
    will turn the screen off, but will not disable the video output

-     -Sw
    Combines the two commands above to use your device without the fear that it goes into sleep but shuts your screen off

-     --show-touches / -t
    Show a point where you click, useful when you control android using your android

-     --power-off-on-close
    When you will disconnect, the screen will be shut down

-     --no-power-on
    Disables the power On upon connect behaiviour