#
-----------------------------------------------------------------------------  
# docker-agskies2  
#  
# A dockerized minecraft server for the Agrarian Skies 2  
#  
# Needs work, comments and serious polish  
#  
# Authors: Brian Eilber  
# Updated: March 27th, 2016  
# Require: Docker (http://www.docker.io/)  
#
-----------------------------------------------------------------------------  
FROM ubuntu:14.04  
MAINTAINER Brian Eilber <brian.eilber@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get --yes update && \  
apt-get --yes upgrade && \  
apt-get --yes install software-properties-common  
  
RUN sudo apt-add-repository --yes ppa:webupd8team/java && apt-get --yes update  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
apt-get --yes install curl oracle-java7-installer unzip && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir /server  
RUN wget http://addons-
origin.cursecdn.com/files/2241/72/AS2%201.1.5%20Server%20Files.zip -O
/server/pack.zip  
RUN wget http://addons-origin.cursecdn.com/files/2234/903/SMP%20Template.zip
-O /server/map.zip  
RUN cd /server && unzip pack.zip && rm pack.zip  
RUN cd /server && unzip map.zip && rm map.zip && mv "SMP Template" world  
  
RUN echo "eula=true" > /server/eula.txt  
  
EXPOSE 25565  
EXPOSE 8123  
VOLUME ["/data"]  
  
COPY start.sh /server/start.sh  
  
RUN chmod +x /server/start.sh  
  
CMD ["/server/start.sh"]  

