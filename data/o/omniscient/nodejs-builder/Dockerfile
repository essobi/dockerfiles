# Dockerfile  
# The FROM directive sets the Base Image for subsequent instructions  
FROM omniscient/nodejs  
  
RUN apt-get update && apt-get install -y wget locales && \  
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add \- && \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >
/etc/apt/sources.list.d/google.list && \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && \  
apt-get install -y google-chrome-beta yarn && \  
apt-get autoremove && \  
apt-get clean && \  
export CHROME_BIN=google-chrome-beta  
  
RUN yarn global add github:gulpjs/gulp#4.0 && \  
yarn global add lerna && \  
yarn global add typescript && \  
yarn global add tape && \  
yarn global add aurelia-cli && \  
yarn cache clean  
  

