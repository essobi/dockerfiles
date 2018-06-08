FROM ubuntu:14.04  
#Thanks to https://github.com/user419/docker-sickbeard and
https://github.com/GeoffreyPlitt/docker-sickbeard  
MAINTAINER Tim Haak <tim@haak.co.uk>  
  
ENV SICKBEARD_VERSION master  
#ENV SICKBEARD_VERSION build-506  
RUN apt-get -q update &&\  
apt-get -qy --force-yes dist-upgrade  
  
RUN apt-get install -qy --force-yes python-cheetah wget tar ca-certificates
curl git-core  
  
#RUN curl -L https://github.com/midgetspy/Sick-
Beard/tarball/$SICKBEARD_VERSION -o sickbeard.tgz && \  
# tar -xvf sickbeard.tgz -C / &&\  
# mv /midgetspy-Sick-Beard-* /sickbeard/ &&\  
# rm /sickbeard.tgz  
RUN git clone https://github.com/GuillaumeLebeau/Sick-Beard.git /sickbeard  
  
# apt clean  
RUN apt-get clean &&\  
rm -rf /var/lib/apt/lists/* &&\  
rm -rf /tmp/*  
  
EXPOSE 8081  
VOLUME /volumes/config  
VOLUME /volumes/download  
VOLUME /volumes/media  
  
ADD ./start.sh /start.sh  
RUN chmod u+x /start.sh  
  
CMD ["/start.sh"]  

