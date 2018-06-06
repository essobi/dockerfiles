FROM selenium/node-base:2.53.1  
MAINTAINER Selenium <selenium-developers@googlegroups.com>  
  
USER root  
  
#===========  
# PhantomJS  
#===========  
ENV PHANTOMJS_VERSION 2.1.1  
RUN apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install \  
bzip2 \  
ca-certificates \  
libfontconfig1 \  
&& rm -rf /var/lib/apt/lists/* \  
&& wget --no-verbose -O /tmp/phantomjs.tar.bz2
https://bitbucket.org/rocketboy/phantomjs_bin/downloads/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2 \  
&& tar -C /opt -xjf /tmp/phantomjs.tar.bz2 \  
&& rm /tmp/phantomjs.tar.bz2 \  
&& ln -fs /opt/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/bin/phantomjs
/usr/bin/phantomjs  
  
#====================================  
# PhantomJS Launch Script Modication  
#====================================  
COPY entry_point.sh /opt/bin/entry_point.sh  
RUN chmod +x /opt/bin/entry_point.sh  
  
USER seluser  

