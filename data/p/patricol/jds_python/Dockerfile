FROM patricol/python:18.04  
USER root  
  
RUN apt-get update; \  
apt-get install -y \  
python-dev python-xlib python3-tk scrot && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
pip3 install \  
python3-xlib && \  
# above are required by PyAutoGUI, which can only be installed when a display
is set etc.  
pip3 install \  
boto \  
bottlenose \  
gspread \  
openpyxl \  
progressbar33 \  
py2exe \  
Pillow \  
pyperclip \  
twilio \  
xmltodict \  
PyInstaller \  
pysftp \  
pyOpenSSL \  
oauth2client \  
PyJWT \  
ecdsa \  
fuzzywuzzy \  
beautifulsoup4 \  
selenium \  
html2text \  
retrying \  
google-cloud \  
google-api-python-client \  
pefile \  
praw \  
psycopg2 \  
pipdeptree && \  
pip3 install \  
pycrypto && \  
xvfb-run pip install PyAutoGUI  
  
USER user

