# Build: docker build -t guiselenium .  
# Launch: docker run -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix
--hostname=$HOSTNAME -v $HOME/.Xauthority:/root/.Xauthority -it guiselenium  
# Author: Sprinteiro dev  
#  
# Use case: Docker in Practice. Page 156, 88  
#  
# From Ubuntu 14.04 base image, install Firefox and Python plus utility tools  
# in order to run a user experience on Docker Hub with Mozilla Firefox  
FROM ubuntu:14.04  
RUN apt-get update  
RUN apt-get install -y curl unzip  
RUN apt-get install -y firefox  
RUN apt-get install -y libcanberra-gtk3-module  
RUN apt-get install -y python2.7 python-pip  
RUN pip install selenium  
  
# Download Mozilla GeckoDriver for Linux 64 bits, unpack it in image in
/opt/geckodriver  
RUN mkdir -p /opt/geckodriver \  
&& curl
https://github.com/mozilla/geckodriver/releases/download/v0.11.1/geckodriver-v0.11.1-linux64.tar.gz
> geckodriver.tar.gz  
ADD geckodriver.tar.gz /opt/geckodriver/  
  
# If Mozilla GeckDriver not possible, comment out lines below to extract zip
file into image in /opt/geckodriver  
# RUN mkdir -p /opt/geckodriver  
# Local import if not downloaded from the Internet  
# COPY geckodriver.tar.gz /opt/geckodriver/  
# RUN cd /opt/geckodriver && tar xvf geckodriver.tar.gz  
ADD browsegitseleniumtest1.py /browsegitseleniumtest1.py  
ADD dockerhub.py /dockerhub.py  
COPY launchtest.sh /launchtest.sh  
  
# Skip prompt for any confirmation: https://lincolnloop.com/blog/automated-no-
prompt-deployment-pip/  
ENV PIP_NO_INPUT 1  
ENV PATH $PATH:/opt/geckodriver  
  
# Shell to execute python script with Selenium test case  
CMD ["sh","-c",". /launchtest.sh"]  

