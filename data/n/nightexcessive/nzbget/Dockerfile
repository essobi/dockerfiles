FROM phusion/baseimage:latest  
MAINTAINER Michael Johnson <michael@johnson.computer>  
  
RUN add-apt-repository -y ppa:modriscoll/nzbget && apt-get update \  
&& apt-get install -y nzbget unrar p7zip-full && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY start.sh /root/start.sh  
  
CMD /root/start.sh  
  
VOLUME /config /downloads  
  
EXPOSE 6789  

