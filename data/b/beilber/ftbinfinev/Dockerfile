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
FROM beilber/java8-base  
  
MAINTAINER Brian Eilber <brian.eilber@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get --yes update && \  
apt-get --yes upgrade && \  
apt-get --yes install software-properties-common  
  
RUN apt-get --yes install unzip && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN useradd -M -r minecraft  
  
RUN mkdir /server  
  
RUN wget
http://ftb.cursecdn.com/FTB2/modpacks/FTBInfinity/2_5_0/FTBInfinityServer.zip
-O /server/pack.zip  
  
RUN cd /server && unzip pack.zip && rm pack.zip  
  
RUN sh /server/FTBInstall.sh  
RUN echo "eula=true" > /server/eula.txt  
  
EXPOSE 25565  
EXPOSE 8123  
VOLUME ["/data"]  
COPY server.properties /server/server.properties  
COPY init.sh /etc/init.d/mcserver  
  
RUN chmod +x /etc/init.d/mcserver  
CMD ["/etc/init.d/mcserver","start"]  

