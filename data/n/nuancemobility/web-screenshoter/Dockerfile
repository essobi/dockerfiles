FROM nuancemobility/ubuntu-base:16.10  
MAINTAINER sspcm <mobility-sspcm@nuance.com>  
  
RUN apt-get update -y && \  
apt-get install -y npm phantomjs && \  
ln -s /usr/bin/nodejs /usr/bin/node  
  
ADD src /src  
  
RUN cd /src && npm install  
  
EXPOSE 8080  
ENTRYPOINT [ "nodejs", "/src/index.js" ]  

