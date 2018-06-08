FROM debian:wheezy  
  
MAINTAINER Bruno Binet <bruno.binet@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV NODEJS_VERSION 0.10.35  
RUN apt-get update && apt-get install -yq --no-install-recommends \  
git rlwrap ca-certificates python build-essential  
  
ADD
https://deb.nodesource.com/node/pool/main/n/nodejs/nodejs_${NODEJS_VERSION}-1nodesource1~wheezy1_amd64.deb
/tmp/nodejs.deb  
RUN dpkg -i /tmp/nodejs.deb  
  
RUN npm -g install geddy peerflix  
RUN git clone https://github.com/yify-pop/yify-pop.git  
WORKDIR /yify-pop  
RUN npm install  
RUN npm install moment getport adm-zip opensrt_js child geddy  
RUN apt-get purge -yq git python build-essential && apt-get autoremove -yq \  
&& apt-get clean all  
  
ADD production.js /yify-pop/config/  
  
EXPOSE 4000 8889  
#CMD node yifystart.js  
CMD ["/usr/bin/geddy", "-e", "production"]  

