FROM ubuntu:14.04  
MAINTAINER Fry <Fry1983@mail.com>  
RUN apt-get update  
RUN apt-get purge firefox  
RUN apt-cache showpkg firefox  
RUN apt-get install -y wget libfreetype6 libfontconfig1 libxrender1 libXext6
libXdamage1 libXfixes-dev libXcomposite-dev libasound-dev libdbus-glib-1-dev
libgtk2.0-0 libxt6  
RUN apt-get install -y python python-pip  
RUN apt-get install -y xvfb xserver-xephyr vnc4server  
RUN pip install selenium==2.48.0 requests pyvirtualdisplay  
RUN wget https://ftp.mozilla.org/pub/firefox/releases/45.0/linux-x86_64/en-
US/firefox-45.0.tar.bz2  
RUN tar -xjf firefox-45.0.tar.bz2  
RUN mv firefox /opt/firefox45  
RUN ln -s /opt/firefox45/firefox /usr/bin/firefox  
RUN ls /opt/firefox45  
RUN firefox --version

