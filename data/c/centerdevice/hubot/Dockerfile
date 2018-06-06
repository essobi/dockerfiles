FROM rheinwerk/hubot:0.1.4  
MAINTAINER Lukas Pustina <lukas.pustina@centerdevice.de>  
  
# Install Additional Software  
USER root  
RUN apt-get update  
RUN apt-get install -y openssh-client pdsh dnsutils  
  
# Cleanup  
RUN apt-get autoremove -y; apt-get clean; rm -rf /var/lib/apt/lists/*; find
/usr/share/locale -mindepth 1 -maxdepth 1 ! -name 'en' ! -name 'de*' | xargs
--no-run-if-empty rm -rf; find /usr/share/doc -depth -type f ! -name copyright
| xargs --no-run-if-empty rm -rf; find /usr/share/doc -empty | xargs --no-run-
if-empty rmdir; rm -rf /usr/share/man /usr/share/groff /usr/share/info
/usr/share/lintian /usr/share/linda /var/cache/man  
  
USER carl  
WORKDIR /carl  
  
# Install Scripts  
RUN npm install --save hubot-bangbang  
RUN npm install --save hubot-centerdevice  
COPY docker/external-scripts.json /carl/  
  

