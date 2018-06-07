FROM ubuntu:latest  
  
LABEL maintainer="jeremy@icysoft.fr"  
  
## BASE ##  
## ==== ##  
  
RUN apt-get update --fix-missing \  
&& apt-get -qqy upgrade \  
&& apt-get install -qqy sudo curl wget unzip git awscli  
  
## NODEJS 6 ##  
## ======== ##  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - \  
&& sudo apt-get install -qqy nodejs  
  
## CHROME ##  
## ====== ##  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo
apt-key add - && \  
sudo sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list' && \  
sudo apt-get update && \  
sudo apt-get install -qqy google-chrome-stable  
  
## EXEMPLE ##  
## ======= ##  
# RUN mkdir /data  
# WORKDIR /data  
# ENTRYPOINT ["/usr/bin/google-chrome", \  
# "--disable-gpu", \  
# "--headless", \  
# "--no-sandbox", \  
# "--user-data-dir=/data"]

