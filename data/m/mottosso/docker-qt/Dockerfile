FROM ubuntu:16.04  
# Needed to install pyside2-tools without issues  
ENV DEBIAN_FRONTEND noninteractive  
  
# Expose shiboken to apt-get  
RUN echo deb http://us.archive.ubuntu.com/ubuntu xenial main universe >>
/etc/apt/sources.list  
  
RUN apt-get update && \  
apt-get install -y \  
software-properties-common && \  
add-apt-repository -y ppa:thopiekar/pyside-git && \  
apt-get update && apt-get install -y \  
nano \  
python3 \  
python3-dev \  
python3-pip \  
python3-pyqt4 \  
python3-pyqt5 \  
python3-pyside \  
python3-pyside2 \  
pyside2-tools \  
libshiboken2-dev \  
xvfb  
  
# Nose is the Python test-runner  
RUN pip3 install nose nosepipe  
  
# Enable additional output from Launcher  
ENV QT_VERBOSE true  
ENV QT_TESTING true  
  
# Xvfb  
ENV DISPLAY :99  

