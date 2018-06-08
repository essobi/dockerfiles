#################################################################  
# Bitcore distribution with supervisord & node-gyp installed. Location
dockerfiles/bitcore-regtest  
# Build command:  
# $ docker build -t plank/bitcore-regtest -f plank/bitcore-regtest .  
# Push to docker.io/hub.docker.com  
# $ docker push plank/bitcore-regtest  
#################################################################  
FROM plank/node:latest  
MAINTAINER rajesh@getplank.com  
  
# Create app directory. Make sure /logs/plank and /data/bitcore are mounted
during run. Else, they will be created locally.  
RUN mkdir -p /usr/src/app /logs/bitcore /bitcore /root/.bitcore  
RUN cd /usr/src/app && \  
git clone https://github.com/bitpay/bitcore-node.git  
WORKDIR /usr/src/app/bitcore-node  
  
# install dependencies  
RUN npm install && \  
./bin/install && \  
make -C ./libbitcoind clean && \  
rm -fr cache/*  
  
RUN npm install insight-api && \  
npm install insight-ui  
  
CMD ["/bin/bash"]  

