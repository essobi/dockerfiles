# Getting node image  
FROM node:9.7.0  
LABEL authors=gauravraosahab  
  
RUN apt-get update && apt-get install -y xvfb  
  
#============================================  
# Google Chrome  
#============================================  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list  
RUN apt-get update  
RUN apt-get install -y google-chrome-stable  
RUN rm /etc/apt/sources.list.d/google-chrome.list  
RUN rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
ENV CHROME_BIN /usr/bin/google-chrome  

