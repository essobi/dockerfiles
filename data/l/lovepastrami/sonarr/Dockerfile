FROM ubuntu  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FDA5DFFC  
RUN echo "deb http://apt.sonarr.tv/ master main" | tee
/etc/apt/sources.list.d/sonarr.list  
RUN apt-get update && apt-get install -y nzbdrone  
RUN apt-get autoremove -y && apt-get clean -y  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 8989  
CMD mono /opt/NzbDrone/NzbDrone.exe  

