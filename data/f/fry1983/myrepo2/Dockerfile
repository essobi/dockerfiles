FROM ubuntu:16.04  
MAINTAINER Fry <Fry1983@mail.com>  
RUN apt-get update  
RUN apt-get install -y wget firefox  
RUN firefox --version  
RUN wget
https://github.com/mozilla/geckodriver/releases/download/v0.19.0/geckodriver-v0.19.0-linux64.tar.gz  
RUN tar -xvzf geckodriver*  
RUN chmod +x geckodriver  
RUN mv geckodriver /bin/  
RUN export PATH=$PATH:/bin/geckodriver  
RUN apt-get install -y python python-pip  
RUN apt-get install -y xvfb xserver-xephyr vnc4server  
RUN pip install selenium requests pyvirtualdisplay

