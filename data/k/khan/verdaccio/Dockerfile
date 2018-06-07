FROM node:6.6.0-onbuild  
RUN adduser --disabled-password --gecos "" verdaccio && \  
mkdir -p /verdaccio/storage /verdaccio/conf && \  
chown -R verdaccio.verdaccio /verdaccio  
  
USER verdaccio  
WORKDIR /verdaccio  
  
ADD conf/docker.yaml /verdaccio/conf/config.yaml  
  
EXPOSE 4873  
VOLUME ["/verdaccio"]  
  
CMD ["/usr/src/app/bin/verdaccio", "--config", "/verdaccio/conf/config.yaml"]  

