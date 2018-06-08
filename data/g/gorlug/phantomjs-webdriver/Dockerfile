FROM ubuntu:16.04  
MAINTAINER Achim Rohn <achim@rohn.eu>  
  
ENV phantomjs_version 2.1.1  
RUN apt-get update && apt-get -y install fontconfig wget bzip2  
RUN wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${phantomjs_version}-linux-x86_64.tar.bz2  
RUN tar xjf phantomjs-${phantomjs_version}-linux-x86_64.tar.bz2  
RUN mv /phantomjs-${phantomjs_version}-linux-x86_64/bin/phantomjs /usr/bin  
RUN useradd -m phantomjs  
USER phantomjs  
  
EXPOSE 8910  
ENTRYPOINT ["phantomjs", "--webdriver", "8910"]  

