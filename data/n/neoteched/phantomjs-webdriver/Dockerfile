FROM ubuntu:16.04  
MAINTAINER Achim Rohn <achim@rohn.eu>  
  
ENV phantomjs_version 2.1.1  
RUN apt-get update && apt-get -y install fontconfig wget bzip2 \  
fonts-wqy-microhei && \  
wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${phantomjs_version}-linux-x86_64.tar.bz2
&& cd / && \  
tar xjf phantomjs-${phantomjs_version}-linux-x86_64.tar.bz2 &&\  
mv phantomjs-${phantomjs_version}-linux-x86_64/bin/phantomjs /usr/bin &&\  
useradd -m phantomjs &&\  
apt-get purge -y wget bzip2 &&\  
rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*
/phantomjs-${phantomjs_version}-linux-x86_64.tar.bz2  
USER phantomjs  
  
EXPOSE 8910  
ENTRYPOINT ["phantomjs", "--webdriver", "8910"]  

