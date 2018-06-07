FROM node:9.0.0  
WORKDIR /app  
  
# Install some dependencies  
RUN apt-get update -y  
RUN apt-get install -qqy \  
dirmngr \  
wget \  
git \  
curl \  
apt-utils  
  
# Install Java  
#RUN apt-get install -y default-jre  
# Install Chrome  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/
stable main" >> /etc/apt/sources.list.d/google-chrome.list'  
RUN apt-get update  
RUN apt-get install -y google-chrome-stable  
  
# install yarn  
RUN npm install -g yarn  
  

