FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG en_US.UTF-8  
RUN echo "deb http://ppa.launchpad.net/maxmind/ppa/ubuntu trusty main" >
/etc/apt/sources.list.d/maxmind.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys "DE742AFA" \  
&& apt-get update \  
&& apt-get install -y geoipupdate \  
&& apt-get -qy autoremove \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
COPY init.sh /  
  
VOLUME /data  
  
CMD [ "/init.sh" ]  

