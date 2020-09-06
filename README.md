# Gifcreator
A program to create gifs from images or videos

## Getting Started
Make sure you are using python >= 3.6:
```
python --version
```
Install python dependencies:
```
pip install -r requirements.txt
```
Install gifsicle:

With Homebrew `brew install gifsicle`

With MacPorts `sudo port install gifsicle`


Converting images to a gif requires all images to be in the same directory and be in order (the first image/frame of your gif should be first when ordering images by name).

## Gifcreator Command Line
To run the command line interface:
```
python creategif_cl.py
```
The program will ask for your input to several questions - the specifics on how to answer and format will be in the prompt.

The program will output your gif with name and location specified by you.

## Gifcreator GUI - WORK IN PROGRESS