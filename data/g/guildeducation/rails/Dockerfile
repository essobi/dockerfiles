FROM guildeducation/ruby:2.4.2  
LABEL maintainer "Guild Engineering <engineering@guildeducation.com>"  
  
ENV NODE_VERSION=8.6.0  
ENV YARN_VERSION=1.3.2  
ENV CHROMEDRIVER_VERSION=2.38  
  
RUN node_main_version=`echo 8.6.0| cut -d'.' -f 1` && \  
curl -o nodejs.deb
"https://deb.nodesource.com/node_${node_main_version}.x/pool/main/n/nodejs/nodejs_${NODE_VERSION}-1nodesource1_amd64.deb"
&& \  
dpkg -i nodejs.deb && \  
rm nodejs.deb && \  
apt-get update && apt-get install -y apt-transport-https unzip && \  
curl -o chromedriver.zip
"https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip"
&& \  
unzip chromedriver.zip && mv chromedriver /usr/local/bin && rm
chromedriver.zip && \  
curl -sS https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
\- && \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" | tee
/etc/apt/sources.list.d/chrome.list && \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && apt-get install yarn=${YARN_VERSION}-1 google-chrome-stable
-y && \  
apt-get remove \--purge -y unzip && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
  

