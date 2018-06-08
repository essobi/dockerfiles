FROM debian:7.4  
MAINTAINER sage@sagenite.net  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget  
  
ADD assets/setup/sources.list.d/overviewer.list
/etc/apt/sources.list.d/overviewer.list  
  
RUN wget -O - http://overviewer.org/debian/overviewer.gpg.asc |
DEBIAN_FRONTEND=noninteractive apt-key add -  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y minecraft-overviewer  
  
ADD assets/app /app  
  
CMD ["/usr/bin/nice", "-19", "/usr/bin/overviewer.py", "-c", "/app/config.py"]  

