sudo apt update
sudo apt install python3-pip python3-venv -y
python3 -m venv ifx
source ifx/bin/activate
pip install requests
pip install holehe
pip install fade
pip install ignorant
pip install python-nmap
pip install cowsay
pip install phonenumbers

python3 ./infonyx.py
