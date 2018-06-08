FROM node:latest  
MAINTAINER Patrice FERLET <metal3d@gmail.com>  
  
# to be able to use --user, node need to write  
# data to $HOME, but using root will break that possibility, so  
# use /project instead  
ENV HOME /project  
WORKDIR /project  
EXPOSE 9000 35729  
RUN set -ex;\  
apt-get update && apt-get install -y ruby-compass; \  
npm install -g grunt-cli bower yo generator-karma generator-angular wiredep;  
  
CMD ["grunt", "serve"]  
  

