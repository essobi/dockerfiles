FROM jenkins  
MAINTAINER Jerry Chen  
  
# Prep Jenkins Directories  
USER root  
RUN mkdir /var/log/jenkins  
RUN mkdir /var/cache/jenkins  
RUN chown -R jenkins:jenkins /var/log/jenkins  
RUN chown -R jenkins:jenkins /var/cache/jenkins  
  
RUN apt-get update && apt-get install -y nodejs-legacy npm build-essential
chrpath libssl-dev libxft-dev libfreetype6 libfreetype6-dev libfontconfig1
libfontconfig1-dev  
RUN wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2  
RUN tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2  
RUN mv phantomjs-2.1.1-linux-x86_64 /usr/local/share  
RUN ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs
/usr/local/bin  
RUN rm -rf /var/lib/apt/lists/*  
RUN npm install -g grunt-cli karma-cli  
  
USER jenkins  

