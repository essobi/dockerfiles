FROM debian:latest  
MAINTAINER Marco Cyriacks <marco@cyriacks.net>  
  
RUN apt-get update -y && apt-get upgrade -y  
RUN apt-get install -y git build-essential debmake  
RUN apt-get install -y qt5-default qt5-qmake qtbase5-dev-tools libqt5svg5-dev
libqt5webkit5-dev libmarkdown2-dev  
  
# Set correct timezone  
ENV TZ=Europe/Berlin  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  

