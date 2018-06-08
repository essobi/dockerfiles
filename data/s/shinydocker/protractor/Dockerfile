FROM shinydocker/node:builder-1.2.0  
# From https://github.com/emmenko/docker-nodejs-karma/blob/master/Dockerfile  
RUN apt-get update; \  
apt-get install -y git curl bzip2; \  
curl -sL https://deb.nodesource.com/setup_0.12 | bash -; \  
curl https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - ; \  
sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list'; \  
apt-get update && apt-get install -y google-chrome-stable nodejs Xvfb; \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD xvfb.sh /etc/init.d/xvfb  
#ADD entrypoint.sh /entrypoint.sh  
  
ENV DISPLAY :99.0  
ENV CHROME_BIN /usr/bin/google-chrome  
  
  
# From https://github.com/jciolek/docker-protractor-
headless/blob/master/Dockerfile  
#WORKDIR /tmp  
RUN npm install -g protractor mocha jasmine && \  
webdriver-manager update && \  
apt-get update && \  
apt-get install -y xvfb wget openjdk-7-jre && \  
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
&& \  
dpkg --unpack google-chrome-stable_current_amd64.deb && \  
apt-get install -f -y && \  
apt-get clean && \  
rm google-chrome-stable_current_amd64.deb && \  
mkdir /protractor  
#ADD protractor.sh /protractor.sh  
#WORKDIR /protractor  

