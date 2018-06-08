FROM ubuntu:latest  
MAINTAINER celeron1ghz <celeron1ghz@gmail.com>  
  
WORKDIR /root  
COPY package.json /root/  
COPY run.sh /root/  
  
RUN apt-get update \  
&& apt-get -y install curl \  
&& curl -sL https://deb.nodesource.com/setup_7.x | bash - \  
&& apt-get -y install --no-install-recommends \  
nodejs \  
build-essential unzip git \  
xvfb x11-xkb-utils xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic
x11-apps clang \  
libssl-dev libdbus-1-dev libgtk2.0-dev libnotify-dev \  
libxss1 \  
libgnome-keyring-dev libgconf2-dev libasound2-dev libcap-dev libcups2-dev
libxtst-dev libnss3-dev gcc-multilib g++-multilib \  
&& apt-get clean \  
&& apt-get -y remove build-essential \  
libssl-dev libdbus-1-dev libgtk2.0-dev libnotify-dev \  
libgnome-keyring-dev libgconf2-dev libasound2-dev libcap-dev libcups2-dev
libxtst-dev libnss3-dev gcc-multilib g++-multilib \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /root/.electron \  
&& npm install  

