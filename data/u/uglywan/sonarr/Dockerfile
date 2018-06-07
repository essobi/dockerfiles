FROM ubuntu:trusty  
MAINTAINER Ugly-Wan  
  
# Language set, using US for consistency  
ENV LANG en_US.UTF-8  
RUN locale-gen $LANG  
RUN update-locale LANG=$LANG  
RUN update-locale LANGUAGE=$LANG  
  
# Install time, Sonarr requires you to add their repo  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FDA5DFFC  
RUN echo "deb http://apt.sonarr.tv/ master main" | tee
/etc/apt/sources.list.d/sonarr.list  
RUN apt-get -qy update  
RUN apt-get -qy install nzbdrone  
RUN apt-get -qy upgrade  
  
# Startup script  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
  
EXPOSE 8989  
#Mount points  
VOLUME /mnt/blackhole  
VOLUME /mnt/complete  
VOLUME /mnt/appdata  
  
CMD ["/start.sh"]  

