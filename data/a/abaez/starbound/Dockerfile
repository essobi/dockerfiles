FROM centos  
MAINTAINER [Alejandro Baez](https://twitter.com/a_baez)  
  
# environment for container  
ENV STEAM_USERNAME "anonymous"  
ENV STEAM_PASSWORD ""  
# dependencies  
RUN yum install -y curl tar zip vim  
RUN yum install -y libvorbis libogg libpng  
RUN yum install -y make glibc gcc gcc-c++ make procps freetype openssl  
RUN yum install -y glibc.i686 libstdc++.i686  
  
# mkdir for steam and starbound  
RUN mkdir -p /opt/steamcmd  
RUN mkdir -p /srv/starbound  
  
# get steamcmd  
WORKDIR /opt/steamcmd  
RUN curl -s http://media.steampowered.com/client/steamcmd_linux.tar.gz | tar
xzvf -  
  
# make start script  
ADD ./add/start.sh ./start.sh  
ADD ./add/updater.sh ./updater.sh  
RUN chmod +x ./start.sh ./updater.sh  
  
# Server ports  
EXPOSE 21025  
EXPOSE 21026  
# volume for server  
VOLUME /srv/starbound  
  
CMD ["./start.sh"]  

