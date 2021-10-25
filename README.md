### Simple project that demonstrates the ability to connect telegram and arduino through python.
-----
## About

Hey! My name is ***Darrso*** and I decided to try to make arduino control using telegram bot.

#### ***Frameworks*** used:
1. [Aiogram](https://github.com/aiogram/aiogram "Aiogram")
2. [Pyserial](https://github.com/pyserial/pyserial "Pyserial")

#### ***Arduino***:
1. 7 Wires **MALE TO MALE**
2. 3 resistors
3. Arduino **UNO**

## How it works?
***1. We connect everything to the breadboard***
![image](https://user-images.githubusercontent.com/68957520/138681107-922e97f4-a6a0-424a-a2a3-d15abee2c7cf.png)
![image](https://user-images.githubusercontent.com/68957520/138681174-6e006c63-b9c5-4f26-b622-04f98931b3f5.png)
![image](https://user-images.githubusercontent.com/68957520/138681196-cb3fd9f4-4c01-47d6-84b3-78f5e4abff87.png)
![image](https://user-images.githubusercontent.com/68957520/138681216-7e524c20-6685-4d4e-a10e-4fb132a87f7b.png)

***2. Upload a sketch from the arduino folder to the board***

***3. In the config.py file, insert the bot token, change the com port.***

***4. Start main.py***

***5. Send your bot a message - /start***

***6. The bot receives this message, then you must choose which LED you want to turn on / off.***



https://user-images.githubusercontent.com/68957520/138683036-8d7c99f2-f4d6-46d1-9a96-63665f7944a1.MOV

  
## Plans for the future:

I have another option to implement this work without connecting the arduino to the computer. In the future, I will order an ESP8266 module and modify the program. The result will be on [my github profile](https://github.com/darrso "Darrso").
