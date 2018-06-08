# Full list of versions available here:
https://registry.hub.docker.com/_/node/tags/manage/\n' +  
FROM node:4  
# Add repository files to container  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/
stable main" >> /etc/apt/sources.list.d/google-chrome.list'  
  
#Start: Packages  
RUN apt-get update -y && apt-get install -y redis-server build-essential  
RUN apt-get install -y google-chrome-stable curl wget xvfb  
#End

