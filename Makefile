install_prerequisites:
	sudo apt update
	sudo apt upgrade -y
	sudo apt-get install stress-ng -y
	sudo apt-get install python3-pip -y
	pip3 install -r requirements.txt
