FROM openjdk:8-jre  
  
MAINTAINER ValentinDeville <contact@valentin-deville.eu>  
  
# Create directory and start JD2 for the initial update and creation of config
files.  
RUN mkdir -p /opt/JDownloader/ && \  
wget -O /opt/JDownloader/JDownloader.jar --progress=bar:force
http://installer.jdownloader.org/JDownloader.jar && \  
java -Djava.awt.headless=true -jar /opt/JDownloader/JDownloader.jar  
  
COPY startJD2.sh /opt/JDownloader/  
RUN chmod +x /opt/JDownloader/startJD2.sh  
  
# Run this when the container is started  
CMD /opt/JDownloader/startJD2.sh  

