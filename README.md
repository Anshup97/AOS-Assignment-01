Missile Defense System

## Overview

The Missile Defense System is a user interactive distributed application that models a battlefield with soldiers and a commander.
The User(client) interacts with the Commander (Server) which relays the commands to Soldiers(Clients). 
The system is designed to manage soldier positions, detect incoming missiles, and coordinate soldier actions to minimize casualties.
It also includes a commander election mechanism. After T time, which is the duration of battle, if >50% soldiers are alive, the battle
is won,otherwise not.

## Installation

Follow these steps to set up and run the Missile Defense System:

### Prerequisites

- Python 3.7 or higher
- pip version 9.0.1 or higher

	If necessary, upgrade your version of pip:

		$ python -m pip install --upgrade pip
		
	If you cannot upgrade pip due to a system-owned installation, you can run the example in a virtualenv:

	$ python -m pip install virtualenv
	$ virtualenv venv
	$ source venv/bin/activate
	$ python -m pip install --upgrade pip

- gRPC
	Install gRPC:

		$ python -m pip install grpcio
		
	Or, to install it system wide:

		$ sudo python -m pip install grpcio

- gRPC tools
	Python’s gRPC tools include the protocol buffer compiler protoc and the special 
	plugin for generating server and client code from .proto service definitions.
	
	To install gRPC tools, run:

			$ python -m pip install grpcio-tools

### Download the example

1. Clone the repository to get the example code:

   git clone "https://github.com/Anshup97/AOS-Assignment-01.git"
   cd AOS-Assignemnt-01
   

###Run the Battlefield application

- From the Battlefield directory:

		Run the server:

			$ python Commander.py
			
		From another terminal, run :

			$ python Soldiers.py
		
		Open one more terminal and run :
			
			$ python userinterface.py
			
Congratulations! You’ve just run the application.Now follow the instructions on userinterface.py console screen.

###Group Details:

- Saurav S 
		BITS ID:2023H1120184P
		Email  :h20230184@pilani.bits-pilani.ac.in
		
- Anshuman Panda
		BITS ID:2023H1120183P
		Email  :h20230183@pilani.bits-pilani.ac.in
