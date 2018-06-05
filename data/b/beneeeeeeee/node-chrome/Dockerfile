# use 'node' as base image  
FROM node:9.11.1  
# Install apt-transport-https  
RUN apt-get update \  
&& apt-get install -y apt-transport-https  
  
# Add Chrome key & sources  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main"
> /etc/apt/sources.list.d/google-chrome.list  
  
# Install Chrome  
RUN apt-get update \  
&& apt-get install -y google-chrome-stable=67.0.3396.62-1  

