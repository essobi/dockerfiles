FROM ubuntu:14.04  
# Install node.js and npm  
RUN apt-get -qq update && \  
apt-get install -y nodejs && \  
apt-get install -y npm && \  
ln -s /usr/bin/nodejs /usr/bin/node  
  
# Install grunt-cli  
RUN npm install -g grunt-cli  
  
# Install local packages  
ADD https://github.com/twbs/bootstrap/raw/v3.2.0/package.json package.json  
RUN npm install  
  
# For PhantomJS  
RUN apt-get install -y libfreetype6 libfontconfig  
  
# Install Jekyll  
RUN apt-get install -y rubygems-integration ruby-dev && \  
gem install jekyll  

