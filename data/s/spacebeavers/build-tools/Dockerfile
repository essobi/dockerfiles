FROM alpine:3.3  
MAINTAINER Chris Saunders <slapheadted@gmail.com>  
MAINTAINER Mike Buckley <mikebuckley.canada@gmail.com>  
  
##  
## To use this image for your developer workflow:  
##  
## docker run -it -p 3000:3000 -v $(pwd):/code spacebeavers/build-tools:latest  
##  
## docker run -it -p 3000:3000 -v $(pwd):/code spacebeavers/build-tools:latest
polymer:seed element-name  
##  
# TODO: Pin the following package versions.  
RUN apk add git --update  
RUN apk add nodejs --update  
  
RUN npm install -g yo  
RUN npm install -g generator-polymer  
  
# Credit to cthulhu666. https://github.com/cthulhu666/docker-yeoman  
# Add a yeoman user because yeoman doesn't like being root  
RUN adduser -D -g "" yeoman && \  
echo "yeoman ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
# set HOME so 'npm install' and 'bower install' don't write to /  
ENV HOME /home/yeoman  
  
RUN mkdir /code && chown yeoman:yeoman code  
  
WORKDIR /code  
  
USER yeoman  
  
ENTRYPOINT ["/usr/bin/yo"]  

