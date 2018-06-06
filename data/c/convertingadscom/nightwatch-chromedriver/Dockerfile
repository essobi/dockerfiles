FROM node:slim  
COPY . /srv  
WORKDIR /srv  
RUN \  
# add chrome  
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add - && \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list && \  
apt-get update -qqy && \  
apt-get -qqy install google-chrome-stable && \  
  
# add npm packages  
npm install -g nightwatch && \  
npm install chromedriver && \  
npm install google-spreadsheet && \  
  
# cleanup before running  
#apt-get remove -y curl gnupg wget unzip && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm /etc/apt/sources.list.d/google-chrome.list && \  
rm -rf /var/lib/apt/lists/* /var/cache/apt/* && \  
npm cache clean --force  

