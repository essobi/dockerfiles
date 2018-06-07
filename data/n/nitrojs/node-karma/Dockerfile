FROM ubuntu:trusty  
  
MAINTAINER Jesús Germade <jesus@aplazame.com>  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections; \  
apt-get update; \  
apt-get install -y build-essential; \  
apt-get install -y git curl python; \  
apt-get install -y xvfb firefox; \  
curl -sL https://deb.nodesource.com/setup_6.x | sudo bash -; \  
curl https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add
- ; \  
sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list'; \  
apt-get update && apt-get install -y google-chrome-stable nodejs Xvfb; \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*; \  
npm install phantomjs -g  
  
ADD xvfb.sh /etc/init.d/xvfb  
RUN chmod a+x /etc/init.d/xvfb  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod a+x /entrypoint.sh  
  
ENV DISPLAY :99.0  
ENV CHROME_BIN /usr/bin/google-chrome  
ENV FIREFOX_BIN /usr/bin/firefox  
  
ENTRYPOINT ["/entrypoint.sh"]  

