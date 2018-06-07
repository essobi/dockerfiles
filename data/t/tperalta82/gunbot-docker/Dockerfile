FROM debian:latest  
  
ADD gunthy-linuxx64 /gunbot/  
RUN chmod +x /gunbot/*  
RUN apt-get -y update  
RUN apt-get -y upgrade  
#CLEANUP  
RUN apt-get clean -y && \  
apt-get autoclean -y && \  
apt-get autoremove -y && \  
rm -rf /usr/share/locale/* && \  
rm -rf /var/cache/debconf/*-old && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /usr/share/doc/*  
RUN mkdir /gunbot/configs  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]

