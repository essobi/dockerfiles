FROM node:8  
LABEL maintainer="Koen Gremmelprez" version="0.1.0"  
  
# Install AWS CLI.  
RUN apt-get update && \  
apt-get install -y python-dev groff && \  
curl -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
pip install awscli  
  
# Install the latest stable NPM  
RUN npm install npm@latest -g  
  
# Install required libraries for pa11y-CI  
RUN apt-get install -y gconf-service libasound2 libatk1.0-0 libc6 libcairo2
libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-
pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0
libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1
libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1
libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3
lsb-release xdg-utils wget  
  
# Add user for Puppeteer so we don't need --no-sandbox.  
RUN groupadd -r pptruser && useradd -r -g pptruser -G audio,video pptruser \  
&& mkdir -p /home/pptruser/Downloads \  
&& chown -R pptruser:pptruser /home/pptruser  
  
# Enable cloudfront preview in aws CLI  
RUN aws configure set preview.cloudfront true  

