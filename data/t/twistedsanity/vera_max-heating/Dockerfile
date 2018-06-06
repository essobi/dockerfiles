# FROM python:3  
FROM phusion/baseimage:latest  
# FROM resin/rpi-raspbian  
MAINTAINER twistedsanity  
  
# Evironment variables to be changed in variables.txt  
# ENV DEBIAN_FRONTEND=noninteractive  
# $WebIP,192.168.0.41  
# $WebPort,4102  
# $MaxIP,192.168.0.36  
# $MaxIP2,192.168.0.37  
# $VeraIP,192.168.0.13  
# $VeraPort,3480  
# $VeraDevice,92  
# $VeraOutsideTempID,112  
# $SingleRadThreshold,78  
# $MultiRadThreshold,60  
# $MultiRadCount,2  
# $AllValveTotal,120  
# $WeatherKey,713951e4ce665b2d2d5d1b7a10b88f63  
# $WeatherCityID,6640068  
#
$WeatherWidget,http://forecast.io/embed/#lat=57.155689&lon=-2.295520&name=Kier
Circle Westhill&units=uk  
  
# Update packages and install software  
RUN \  
apt-get update && \  
apt-get install -y \  
apt-utils \  
python-pip \  
python-dev \  
wget \  
unzip \  
sudo \  
  
# Needed for testing  
nano \  
iputils-ping \  
dnsutils # && \  
# End testing apps  
RUN \  
apt-get clean && rm -rf /tmp/* /var/tmp/* # && \  
RUN \  
pip install psutil # && \  
RUN \  
pip install requests # && \  
RUN \  
pip install RPi.GPIO # && \  
  
RUN \  
# Get and install PiHeating files  
wget https://github.com/twistedsanity/PiHeating/archive/master.zip && \  
unzip master.zip && \  
mkdir /home/pi && \  
mkdir /home/pi/heating && \  
cp -rp PiHeating-master/* /home/pi/heating/ && \  
chmod +x /home/pi/heating/main.py # && \  
RUN \  
sed -i \  
-e 's/WebIP,192.168.0.41/WebIP,$WebIP/' \  
-e 's/WebPort,4102/WebPort,$WebPort/' \  
-e 's/MaxIP,192.168.0.36/MaxIP,$MaxIP/' \  
-e 's/MaxIP2,192.168.0.37/MaxIP2,$MaxIP2/' \  
-e 's/VeraIP,192.168.0.13/VeraIP,$VeraIP/' \  
-e 's/VeraDevice,92/VeraDevice,$VeraDevice/' \  
-e 's/VeraOutsideTempID,112/VeraOutsideTempID,$VeraOutsideTempID/' \  
-e 's/SingleRadThreshold,78/SingleRadThreshold,$SingleRadThreshold/' \  
-e 's/MultiRadThreshold,60/MultiRadThreshold,$MultiRadThreshold/' \  
-e 's/MultiRadCount,2/MultiRadCount,$MultiRadCount/' \  
-e 's/AllValveTotal,120/AllValveTotal,$AllValveTotal/' \  
-e 's/WebIP,192.168.0.41/$WeatherKey/' \  
-e 's/WebIP,192.168.0.41/$WeatherCityID/' \  
-e 's/WebIP,192.168.0.41/$WeatherWidget/' # \  
# /home/pi/heating/variables.txt  
  
# Volumes  
# VOLUME /home/pi  
# Running scripts during container startup  
#CMD [ "python", "/home/pi/heating/main.py" ]  

