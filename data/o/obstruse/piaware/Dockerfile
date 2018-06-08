FROM resin/armv7hf-debian:jessie  
  
LABEL description="jessie v1.1 deploy with --privileged"  
  
RUN [ "cross-build-start" ]  
  
# Install packages  
RUN apt-get -qq update  
RUN apt-get -qq install --no-install-recommends -y \  
apt-utils \  
wget  
  
RUN wget -q
http://flightaware.com/adsb/piaware/files/packages/pool/piaware/p/piaware-
support/piaware-repository_3.5.3_all.deb  
  
RUN dpkg -i piaware-repository_3.5.3_all.deb  
  
RUN apt-get -qq update  
RUN apt-get -qq install --no-install-recommends -y \  
piaware \  
dump1090-fa  
  
RUN apt-get -qq remove -y --purge \  
apt-utils \  
wget \  
&& apt-get -qq autoremove -y  
RUN rm -rf /var/lib/apt/lists/*  
  
COPY startPiaware.sh /root  
RUN chmod +x /root/startPiaware.sh  
  
RUN mkdir /run/dump1090-fa  
RUN mkdir /run/piaware  
  
CMD /root/startPiaware.sh  
  
# PiAware Skyview web page:  
EXPOSE 8080  
# for connections to other viewing tools, e.g. Virtual Radar:  
# non-MLAT data in Beast format:  
EXPOSE 30005  
# MLAT data in Beast format:  
EXPOSE 30105  
RUN [ "cross-build-end" ]  
  

