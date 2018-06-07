FROM nerelohw/docker-ubuntu:16.04  
  
#https://github.com/ONLYOFFICE/Docker-
DocumentServer/blob/release/v5.1.0/Dockerfile  
#https://github.com/ONLYOFFICE/Docker-DocumentServer/tree/hotfix/v5.1.1  
  
ENV LANG=en_US.UTF-8 LANGUAGE=en_US:en LC_ALL=en_US.UTF-8
DEBIAN_FRONTEND=noninteractive  
  
RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d \  
&& apt-get -y update \  
&& apt-get install -yq curl apt-transport-https ca-certificates sudo make wget
locales \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys CB2DE8E5 \  
&& locale-gen en_US.UTF-8 \  
&& curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - \  
&& apt-get -y update && apt-get install -y nodejs \  
&& npm install -g grunt-cli json  
  
RUN apt-get -y update && \  
apt-get -yq install \  
adduser \  
bomstrip \  
htop \  
libasound2 \  
libboost-regex-dev \  
libcairo2 \  
libcurl3 \  
libgconf2-4 \  
libgtkglext1 \  
libnspr4 \  
libnss3 \  
libnss3-nssdb \  
libstdc++6 \  
libxml2 \  
libxss1 \  
libxtst6 \  
nano \  
net-tools \  
netcat \  
pwgen \  
software-properties-common \  
xvfb \  
zlib1g \  
postgresql-client \  
openssh-client \  
git && \  
rm -rf /var/lib/apt/lists/*  

