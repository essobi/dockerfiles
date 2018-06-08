FROM node:latest  
  
RUN apt-get update && apt-get install apt-transport-https -y  
RUN curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add
- \  
&& echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main"
> /etc/apt/sources.list.d/google-chrome.list  
RUN apt-get update && apt-get install google-chrome-stable -y  
RUN npm install -g lighthouse  
RUN groupadd -r chrome && useradd -r -g chrome -G audio,video chrome \  
&& mkdir -p /home/chrome/reports && chown -R chrome:chrome /home/chrome  
USER chrome  
WORKDIR /home/chrome/report  
ENTRYPOINT ["lighthouse"]  

