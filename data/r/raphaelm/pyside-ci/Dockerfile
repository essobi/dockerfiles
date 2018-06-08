FROM selenium/standalone-chrome:2.45.0  
MAINTAINER Raphael Michel  
USER root  
  
RUN apt-get update && apt-get install -y wget python3 git python3-pip \  
libxml2-dev libxslt1-dev python-dev locales \  
python3-dev build-essential cmake qt4-qmake libqtcore4 libqtwebkit4 \  
python3-pyside.qtcore python3-pyside.qtdeclarative python3-pyside.qtgui
python3-pyside.qtnetwork \  
python3-pyside.qtsvg python3-pyside.qtuitools python3-pyside.qtwebkit
python3-pyside.qtxml \  
x11vnc xvfb libffi-dev libssl-dev xauth libjpeg-dev libfreetype6
libfreetype6-dev zlib1g-dev \  
build-essential python3-dev libssl-dev gettext git curl libfontconfig bzip2 \  
\--no-install-recommends  
  
WORKDIR /  
  
RUN locale-gen  
RUN update-locale LANG=C.UTF-8  
ENV LC_ALL C.UTF-8  
ENV LANG C.UTF-8  
# We want a current pip  
ADD get-pip.py /tmp/get-pip.py  
RUN python3 /tmp/get-pip.py  
RUN pip install virtualenv  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
CMD ["/bin/bash"]  

