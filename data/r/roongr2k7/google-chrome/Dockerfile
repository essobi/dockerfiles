FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y wget  
  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main"
>> /etc/apt/sources.list.d/google-chrome.list  
RUN apt-get update && apt-get install -y --no-install-recommends google-
chrome-stable  

