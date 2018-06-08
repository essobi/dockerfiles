FROM php:7.1-fpm  
MAINTAINER Andrew Kirkpatrick <development@andrew-kirkpatrick.com>  
  
# Install Node.js  
RUN apt-get update && \  
apt-get install -y curl build-essential && \  
curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
apt-get install -y nodejs  
  
# Install ZombieJS  
RUN npm install -g zombie && \  
export NODE_MODULES=/usr/lib/node_modules  
  
# Install PhantomJS  
RUN curl -OL
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
&& \  
tar -xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2 && \  
mv phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs && \  
apt-get install -y libfontconfig  
  
# Run GhostDriver  
CMD ["phantomjs", "--webdriver=8643"]  

