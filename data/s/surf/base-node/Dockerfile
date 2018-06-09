# base node-js  
#  
# VERSION 0.0.1  
# BUILD-USING: docker build -t base-node .  
# PUSH-USING: docker tag base-node surf/base-node && docker push surf/base-
node  
FROM surf/base  
MAINTAINER Dan Kinsley <dan@surfbeta.com>  
  
# make sure the package repository is up to date  
RUN apt-get update && apt-get install -y \  
nodejs \  
npm  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
RUN npm install express  
  
CMD ["/bin/bash"]  

