FROM janbaer/alpine:latest  
  
MAINTAINER Jan Baer  
  
USER root  
  
ENV PATH $PATH:/usr/lib/node_modules/bin  
  
RUN npm install -g yarn live-server \  
gulp typescript eslint tslint mocha  
  
USER jan  
  
CMD ["/bin/zsh"]  

