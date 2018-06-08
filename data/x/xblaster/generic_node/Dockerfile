# Pull base image.  
FROM node:6  
MAINTAINER xblaster@lo2k.net  
  
RUN cd $(npm root -g)/npm \  
&& npm install fs-extra \  
&& sed -i -e s/graceful-fs/fs-extra/ -e s/fs\\.move/fs.rename/
./lib/utils/rename.js  
  
# OLD line for NPM install && npm install -g npm@"$NPM_VERSION" \  
# OLD && rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc \  
RUN apt-get update && apt-get install -y\  
ruby-dev\  
rubygems\  
build-essential \  
git  
  
RUN gem install compass && npm install -g bower && npm install -g grunt-cli  
  
RUN npm install -g jspm  
  

