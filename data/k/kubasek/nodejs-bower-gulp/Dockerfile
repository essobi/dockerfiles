#  
# Node.js w/ Bower & Gulp Dockerfile  
#  
# https://github.com/kubasek/nodejs-bower-gulp  
#  
# Pull base image.  
FROM node:0.10.46  
  
RUN \  
apt-get update && apt-get upgrade -y && \  
apt-get -y install git && \  
npm install -g npm@1.4.3 && \  
npm install -g nodemon && \  
npm install -g bower && \  
npm install -g gulp && \  
npm install -g grunt-cli && \  
npm install -g browserify && \  
npm install -g mocha&& \  
npm install -g phantomjs && \  
apt-get -y install ruby-full && \  
gem install sass && \  
apt-get clean && \  
rm -rf \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/*  
  
  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD ["bash"]  

