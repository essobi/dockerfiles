FROM ubuntu:14.04  
MAINTAINER thuchede  
  
RUN apt-get update && apt-get -y install curl python-dev python-pip python-
opencv python-wxgtk2.8 && pip install dronekit-sitl MAVProxy  
  
RUN curl -sL https://deb.nodesource.com/setup_5.x | sudo bash -  
RUN apt-get install -y nodejs  
RUN cp /usr/share/zoneinfo/Europe/Paris /etc/localtime  
  
WORKDIR /app  
ADD . /app  
RUN npm install && npm install -g forever  
EXPOSE 3000  
# launch should be done using : -e NODE_ENV=XXX  
ENTRYPOINT [ "forever", "." ]  

