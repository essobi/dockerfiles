ARG DOCKER_TAG  
FROM brumbrum/php:$DOCKER_TAG  
MAINTAINER Alessandro Lattao <alessandro.lattao@brumbrum.it>  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN \  
apt-get -y --no-install-recommends install curl bzip2 libfontconfig1 && \  
curl -O -J -L
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
&& \  
tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2 && \  
mv phantomjs-2.1.1-linux-x86_64 /usr/local/share && \  
ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs
/usr/local/bin && \  
apt-get purge -y curl bzip2 && \  
apt-get -y autoclean && \  
apt-get -y clean && \  
apt-get -y autoremove  

