FROM ubuntu:14.04  
MAINTAINER Bryce Gibson "bryce.gibson@unico.com.au"  
# make sure the package repository is up to date  
RUN apt-get update && apt-get upgrade -y && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && echo
'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | tee
/etc/apt/sources.list.d/mongodb.list && \  
apt-get update && apt-get install -y mongodb-org build-essential git curl zip
inotify-tools python  
  
ENV NODE_VERSION 4.4.0  
RUN curl
https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.gz
-o /tmp/node.tar.gz && ( cd /usr/local && tar xvzf /tmp/node.tar.gz --strip-
components=1 ; )  
  
ENV FONTELLO_VERSION 5.3.0  
RUN git clone \--depth 1 -b "${FONTELLO_VERSION}"
git://github.com/fontello/fontello.git fontello && ( cd fontello && git
submodule update --init && npm install ) && \  
mkdir -p /data/db  
  
ADD ./application.yml /fontello/config/application.yml  
  
WORKDIR /fontello  
  
RUN apt-get install -y wget automake libtool && yes | ./support/ttfautohint-
ubuntu-12.04.sh && \  
apt-get clean autoclean && apt-get autoremove -y && rm -rf
/var/lib/{apt,dpkg,cache,log}/  
  
COPY ./entrypoint.js /usr/local/bin/entrypoint.js  
  
EXPOSE 3000  
CMD [ "node", "/usr/local/bin/entrypoint.js" ]  

