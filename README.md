# Pyxel GPi Framework

A basic framework for simple games meant for the [RetroFlag GPi Case](http://retroflag.com/GPi-CASE.html) using [Pyxel!](https://github.com/kitao/pyxel)

## Description

A basic framework for the Pyxel game development suite that attempts to make creating games specifically for the GPi easier.

The GPi is a Gameboy-like handheld console with a D-pad, four front-facing buttons (not including Start and Select) as well as two buttons on the back of the handheld.

In order to best fit the screensize and make use of all of the buttons without having to redo all of the necessary underlying code for each game, I wish to create a framework that performs those base functions.

Please note that this is supposed to have what would be required in almost every instance of game development, other things, like sound, graphics, 3D, and tile logic will either be included in separate libraries or must be created by the developer using this framwork.

## Features 

* Preset for the screen size: 256x240 (No aspect ratio, just using all the pixels it can)
* Has built-in handlers for the button presses and creates easy-to-use events
* Has scaffolding for handling "stages" and adding/removing "actors" (inspired by pixi.js)

## How it works

Imports the base Pyxel and creates an App class with predefined settings, making development for the GPi easier!

## Requirements

Pyxel must be installed to use this framework.

## License

This project was created by Derek McCammond and is licensed under the [MIT license.](https://en.wikipedia.org/wiki/MIT_License)