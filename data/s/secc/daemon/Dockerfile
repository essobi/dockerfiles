FROM ubuntu:16.04  
# apt  
RUN apt-get update \  
&& apt-get install -y wget nodejs nodejs-legacy  
  
# install npm + secc, npm install  
RUN mkdir /usr/share/npm \  
&& (wget -qO- https://github.com/npm/npm/archive/master.tar.gz \  
| tar xvfz - -C /usr/share/npm --strip 1) \  
&& mkdir /secc \  
&& (wget -qO- https://github.com/ivere27/secc/archive/master.tar.gz \  
| tar xvfz - -C /secc --strip 1) \  
&& ln -s /usr/share/npm/bin/npm-cli.js /usr/bin/npm \  
&& cd /secc \  
&& npm install  
  
EXPOSE 10508  
ENTRYPOINT exec /usr/bin/nodejs /secc/secc-daemon.js

