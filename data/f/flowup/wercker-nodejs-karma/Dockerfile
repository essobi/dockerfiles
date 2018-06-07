FROM ubuntu:xenial  
  
MAINTAINER FlowUp <flowup@flowup.cz>  
  
RUN apt-get update; \  
apt-get install -y git curl sudo zip; \  
curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash - ; \  
curl https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add
\- ; \  
sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable
main" >> /etc/apt/sources.list.d/google-chrome.list' ; \  
apt-get update && apt-get install -y google-chrome-stable nodejs xvfb; \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN npm i -g yarn && yarn global add @angular/cli node-sass  
  
ADD xvfb.sh /etc/init.d/xvfb  
ADD entrypoint.sh /entrypoint.sh  
  
ENV DISPLAY :99.0  
ENV CHROME_BIN /usr/bin/google-chrome  
  
ENTRYPOINT ["/entrypoint.sh"]  

