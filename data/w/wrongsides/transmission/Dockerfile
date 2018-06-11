FROM wrongsides/baseimage  
  
# Install Dependencies  
RUN add-apt-repository "deb http://ppa.launchpad.net/transmissionbt/ppa/ubuntu
trusty main"  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 365C5CA1  
RUN apt-get update -q &&\  
apt-get install -qy --force-yes transmission-daemon  
  
# Exports and Volumes  
VOLUME ["/config"]  
VOLUME ["/downloads"]  
EXPOSE 9091  
EXPOSE 54321  
# Add a standard config.json  
ADD settings.json /tmp/  
  
# Add config.sh to execute during container startup  
RUN mkdir -p /etc/my_init.d  
ADD config.sh /etc/my_init.d/config.sh  
RUN chmod +x /etc/my_init.d/config.sh  
  
# Add transmission to runit  
RUN mkdir /etc/service/transmission  
ADD transmission.sh /etc/service/transmission/run  
RUN chmod +x /etc/service/transmission/run  

