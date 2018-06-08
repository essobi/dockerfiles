FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
# setup and install mono (key: D3D831EF)  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys D3D831EF \  
&& echo "deb http://download.mono-project.com/repo/debian wheezy main" >
/etc/apt/sources.list.d/mono.list \  
&& apt-get -q update \  
&& apt-get -y install libmono-cil-dev \  
libcurl3 \  
mediainfo \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
# copy startup script  
COPY assets/startup.sh /opt/startup.sh  
  
# expose radarr tcp port  
EXPOSE 7878/tcp  
  
# kick off radarr  
ENTRYPOINT [ "/bin/bash", "/opt/startup.sh" ]  

