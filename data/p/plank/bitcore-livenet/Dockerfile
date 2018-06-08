#################################################################  
# Bitcore distribution with supervisord & node-gyp installed. Location
dockerfiles/bitcore-regtest  
# Build command:  
# $ docker build -t plank/bitcore-regtest -f plank/bitcore-regtest .  
# Push to docker.io/hub.docker.com  
# $ docker push plank/bitcore-regtest  
#################################################################  
FROM plank/bitcore-base:latest  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY bitcore-node.json /root/.bitcore/bitcore-node.json  
  
EXPOSE 8333 8332 3001  
CMD ["/usr/bin/supervisord"]  

