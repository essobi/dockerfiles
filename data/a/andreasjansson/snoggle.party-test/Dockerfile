FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y \  
python-pip \  
xvfb \  
ipython \  
xvfb \  
libxss1 \  
libappindicator1 \  
libindicator7 \  
unzip \  
wget \  
python-nose \  
python-ipdb  
  
RUN pip install \  
flask \  
flask-socketio \  
eventlet \  
pyvirtualdisplay \  
selenium \  
unittest2  
  
RUN wget https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb  
  
RUN dpkg -i --force-depends google-chrome-stable_current_amd64.deb || \  
apt-get install -y -f  
  
RUN wget -N
http://chromedriver.storage.googleapis.com/2.26/chromedriver_linux64.zip  
RUN unzip chromedriver_linux64.zip  
  
RUN mv -f chromedriver /usr/local/share/chromedriver  
RUN ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver  
RUN ln -s /usr/local/share/chromedriver /usr/bin/chromedriver  
  
WORKDIR /opt/snoggle/test  

