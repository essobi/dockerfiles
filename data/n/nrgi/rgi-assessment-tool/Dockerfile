FROM centos:centos7  
MAINTAINER Chris Perry, cperry@resourcegovernance.org  
  
# Enable EPEL for Node.js  
RUN rpm -Uvh https://rpm.nodesource.com/pub_4.x/el/7/x86_64/nodesource-
release-el7-1.noarch.rpm  
  
# Upgrade system  
RUN yum -y clean all  
RUN yum -y distro-sync  
RUN yum -y update  
RUN yum -y upgrade  
  
# Install Node.js, npm, and git  
RUN yum install -y git nodejs npm  
  
# Install dependancies  
RUN yum install -y bzip2 fontconfig freetype libfontconfig.so.1
libfreetype.so.6 libstdc++.so.6 tar.x86_64 urw-fonts wget  
RUN npm install -g bower forever  
  
# Build src  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install --production  
RUN mkdir -p /src && cp -a /tmp/node_modules /src  
RUN rm -R /tmp/node_modules  
COPY . /src  
RUN cd /src && bower install --allow-root  
  
RUN node -v  
RUN npm -v  
  
EXPOSE 80  
  
CMD ["/src/node_modules/forever/bin/forever","/src/server.js"]  
  
  
  
  
  
  
## Enable EPEL for Node.js  
#RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm  
#  
## Install Node.js, npm, git and bower\  
##RUN yum -y install npm  
#RUN yum -y install git \  
# \  
# \  
# \  
# \  
# \  
# \  
# \  
# \  
#  
##RUN yum install -y git \  
#  
#  
#RUN npm install -g bower  
#  
##Install Phantom JS  
#RUN wget
http://phantomjs.googlecode.com/files/phantomjs-1.8.1-linux-x86_64.tar.bz2 -O
/usr/local/share/phantomjs-1.8.1-linux-x86_64.tar.bz2 && ls /usr/local/share  
#RUN tar jxvf /usr/local/share/phantomjs-1.8.1-linux-x86_64.tar.bz2 -C
/usr/local/share  
#RUN ln -s /usr/local/share/phantomjs-1.8.1-linux-x86_64/bin/phantomjs
/usr/local/share/phantomjs  
#RUN ln -s /usr/local/share/phantomjs-1.8.1-linux-x86_64/bin/phantomjs
/usr/local/bin/phantomjs  
#RUN ln -s /usr/local/share/phantomjs-1.8.1-linux-x86_64/bin/phantomjs
/usr/bin/phantomjs  
#  
## Build src  
#ADD package.json /tmp/package.json  
#RUN cd /tmp && npm install --production  
#RUN mkdir -p /src && cp -a /tmp/node_modules /src  
#RUN rm -R /tmp/node_modules  
#COPY . /src  
#RUN cd /src && bower install --allow-root  
#  
#  
#EXPOSE 80  
#  
#CMD ["/src/node_modules/forever/bin/forever","/src/server.js"]  
##CMD ["node", "/src/server.js"]  
  
  
  
#FROM centos:centos7  
#MAINTAINER Chris Perry, cperry@resourcegovernance.org  
#  
## Node version  
#ENV NODE_VERSION 4.0.0  
#  
## Upgrading system  
#RUN yum -y clean all  
#RUN yum -y distro-sync  
#RUN yum -y update  
#RUN yum -y upgrade  
  
## Installing node.js  
#RUN yum install -y wget tar make gcc-c++ openssl openssl-devel  
#RUN cd /tmp && wget
http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION.tar.gz && tar xzf
node-v$NODE_VERSION.tar.gz && cd node-v$NODE_VERSION && ./configure && make &&
make install  
#  
## Install depndancies  
#RUN yum install -y tar.x86_64 bzip2 fontconfig freetype libfreetype.so.6
libfontconfig.so.1 libstdc++.so.6 urw-fonts  
#RUN npm install -g bower forever  
#  
##Install Phantom JS  
#RUN wget
http://phantomjs.googlecode.com/files/phantomjs-1.8.1-linux-x86_64.tar.bz2 -O
/usr/local/share/phantomjs-1.8.1-linux-x86_64.tar.bz2 && ls /usr/local/share  
#RUN tar jxvf /usr/local/share/phantomjs-1.8.1-linux-x86_64.tar.bz2 -C
/usr/local/share  
#RUN ln -s /usr/local/share/phantomjs-1.8.1-linux-x86_64/bin/phantomjs
/usr/local/share/phantomjs  
#RUN ln -s /usr/local/share/phantomjs-1.8.1-linux-x86_64/bin/phantomjs
/usr/local/bin/phantomjs  
#RUN ln -s /usr/local/share/phantomjs-1.8.1-linux-x86_64/bin/phantomjs
/usr/bin/phantomjs  
#  
## Build src  
#ADD package.json /tmp/package.json  
#RUN cd /tmp && npm install --production  
#RUN mkdir -p /src && cp -a /tmp/node_modules /src  
#RUN rm -R /tmp/node_modules  
#COPY . /src  
#RUN cd /src && bower install --allow-root  
#  
#EXPOSE 80  
#  
#CMD ["/src/node_modules/forever/bin/forever","/src/server.js"]  
##CMD ["node", "/src/server.js"]  

