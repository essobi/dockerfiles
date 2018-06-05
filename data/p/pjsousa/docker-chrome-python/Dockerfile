FROM ubuntu  
  
# Add a user for running applications.  
RUN useradd apps  
RUN mkdir -p /home/apps && chown apps:apps /home/apps  
  
USER root  
  
RUN apt-get update; RUN apt-get -y upgrade; apt-get clean  
  
# Overly unecessary requisites  
RUN apt-get install -y build-essential cmake pkg-config\  
libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev\  
libavcodec-dev libavformat-dev libswscale-dev libv4l-dev\  
libxvidcore-dev libx264-dev\  
libgtk-3-dev libx11-dev libboost-python-dev\  
libatlas-base-dev gfortran\  
python2.7-dev python3.5-dev\  
wget zip  
  
# install pip  
RUN wget https://bootstrap.pypa.io/get-pip.py  
RUN python get-pip.py  
  
# Install x11vnc.  
RUN apt-get install -y x11vnc  
  
# Install xvfb.  
RUN apt-get install -y xvfb  
  
# Install fluxbox.  
RUN apt-get install -y fluxbox  
  
# Install wget.  
RUN apt-get install -y wget  
  
# Install wmctrl.  
RUN apt-get install -y wmctrl  
  
# Set the Chrome repo.  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list  
  
# Install Chrome.  
RUN apt-get update && apt-get -y install google-chrome-stable  
  
COPY bootstrap.sh /  
RUN chown apps:apps /bootstrap.sh  
RUN chmod 744 /bootstrap.sh  
  
## instal pip packages  
RUN pip install \  
pandas pandas-datareader\  
matplotlib seaborn plotly\  
scikit-learn scikit-image scipy\  
jupyter\  
h5py\  
tensorflow theano keras\  
pynput pyscreenshot  
  
# missing dependencies for pygtk  
RUN apt-get install -y python-gi python-gi-cairo python3-gi python3-gi-cairo
gir1.2-gtk-3.0  
RUN apt-get install -y gettext fontconfig freetype2-demos expat libpng-dev
zlib1g-dev  
  
CMD '/bootstrap.sh'  
  

