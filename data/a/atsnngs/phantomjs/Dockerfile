FROM ubuntu:14.04  
MAINTAINER Atsushi Nagase<a@ngs.io>  
  
ENV PHANTOM_JS phantomjs-2.1.1-linux-x86_64  
  
RUN apt-get update -y && \  
apt-get -y --no-install-recommends install \  
build-essential \  
chrpath \  
libssl-dev \  
libxft-dev \  
libfreetype6 \  
libfreetype6-dev \  
libfontconfig1 \  
libfontconfig1-dev  
  
ADD https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2
/var/src/  
RUN cd /var/src && tar -C /usr/local \--strip 1 -xjf $PHANTOM_JS.tar.bz2 && rm
$PHANTOM_JS.tar.bz2  
ENTRYPOINT ["/usr/local/bin/phantomjs"]  
  

