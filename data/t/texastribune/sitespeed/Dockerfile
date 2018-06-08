FROM texastribune/base  
MAINTAINER tech@texastribune.org  
  
# This image was 1.656 GB with Java, Chrome and Firefox. It dropped to 632MB  
# when I removed those three items.  
RUN apt-get update  
  
# Node  
RUN add-apt-repository -y ppa:chris-lea/node.js  
RUN apt-get update  
RUN apt-get -yq install apt-utils  
RUN apt-get -yq install nodejs  
  
RUN apt-get -yq install build-essential chrpath git-core libssl-dev
libfontconfig1-dev libxft-dev  
  
#RUN apt-get install -yq openjdk-7-jre curl xsltproc wget unzip  
RUN apt-get install -yq xsltproc wget unzip  
#ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
#sitespeed.io -d 0 -b firefox -u http://www.texastribune.org/  
#RUN apt-get -yq install firefox  
#RUN echo "set -o vi" >> /etc/bash.bashrc  
# frame buffer for Chrome and Firefox:  
#RUN apt-get -yq install xvfb  
#ADD init.xvfb /etc/init.d/xvfb  
#RUN chmod +x /etc/init.d/xvfb  
# TODO: add supervisor to run frame buffer? Or just wrap sitespeed in a script  
# that starts it? (test.sh script for now)  
# Chrome:  
#RUN \  
# wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add - && \  
# echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >
/etc/apt/sources.list.d/google.list && \  
# apt-get update && \  
# apt-get install -y google-chrome-stable && \  
# rm -rf /var/lib/apt/lists/*  
#RUN npm install -g phantomjs chromedriver browsertime  
RUN npm install -g phantomjs  
#RUN npm install sitespeed.io@3.0.0-beta-3 -g  
#RUN npm install sitespeed.io -g  
VOLUME /results  
  
WORKDIR /app  
ADD http://yslow.org/yslow-phantomjs-3.1.8.zip /app/  
RUN unzip yslow-phantomjs-3.1.8.zip  
  
#ENV DISPLAY :1.0  
# TODO: this should be replaced by the docker image under test:  
ADD test.sh /app/  
RUN chmod +x /app/test.sh  
ENTRYPOINT ["/app/test.sh"]  

