FROM node:8  
ENV NPM_CONFIG_LOGLEVEL warn  
  
RUN apt-get update  
RUN apt-get install -y \  
unzip \  
;  
RUN apt-get update -qq -y \  
&& apt-get install -qq -y apt-transport-https unzip \  
&& curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
\  
&& echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main
#Google-Chrome" > /etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update -qq -y \  
&& apt-get install -qq -y --no-install-recommends google-chrome-stable \  
&& curl -s https://chromedriver.storage.googleapis.com/"$(curl -s
https://chromedriver.storage.googleapis.com/LATEST_RELEASE)"/chromedriver_linux64.zip
-o /tmp/chromedriver_linux64.zip \  
&& unzip -d /usr/bin /tmp/chromedriver_linux64.zip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["/mnt"]  
WORKDIR /mnt  

