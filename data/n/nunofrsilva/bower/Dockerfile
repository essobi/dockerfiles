FROM node:5.6-slim  
  
MAINTAINER Nuno Silva <nunofrsilva@gmail.com>  
  
RUN npm install -g bower && \  
echo '{ "allow_root": true }' > /root/.bowerrc  
  
WORKDIR /data  
  
ENTRYPOINT [ "bower" ]  

