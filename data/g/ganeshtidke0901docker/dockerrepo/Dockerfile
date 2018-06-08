FROM ubuntu  
MAINTAINER Ganesh Tidke  
  
# Update and install s/w  
RUN apt-get update  
RUN apt-get install -y openjdk-8-jdk  
RUN apt-get install -y git maven  
RUN apt-get install -y xvfb libxi6 libgconf-2-4  
RUN apt-get install wget unzip curl  
  
# Install Chrome  
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list  
RUN apt-get -yqq update  
RUN apt-get -yqq install google-chrome-stable  
RUN rm -rf /var/lib/apt/lists/*  
  
# Clone Git repo and build/execute automation package  
RUN git clone -b master --single-branch
https://github.com/ganeshtidke0901/dockerrepo.git  
WORKDIR dockerrepo-poc

