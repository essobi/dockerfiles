FROM ubuntu:16.04  
MAINTAINER HandcraftedBits <opensource@handcraftedbits.com>  
  
VOLUME /opt/container/screenshots  
  
RUN apt-get update && \  
apt-get install -y apt-transport-https software-properties-common && \  
add-apt-repository multiverse && \  
apt-get update && \  
echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select
true | debconf-set-selections && \  
echo ttf-mscorefonts-installer msttcorefonts/present-mscorefonts-eula note |
debconf-set-selections && \  
apt-get install -y curl libasound2 libgconf-2-4 libgtk2.0-0 libnss3 libxss1
libxtst6 ttf-mscorefonts-installer \  
xvfb && \  
  
curl -sL https://deb.nodesource.com/setup_7.x | bash - && \  
apt-get install -y nodejs && \  
  
npm install -g netshot && \  
  
apt-get purge -y apt-transport-https software-properties-common && \  
apt-get autoremove -y && \  
apt-get clean -y  
  
COPY data /  
  
EXPOSE 8000  
  
CMD [ "/bin/bash", "/opt/container/script/run-netshot.sh" ]

