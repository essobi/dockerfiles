FROM node:latest  
MAINTAINER Daniel Atkinson <hourd.tasa@gmail.com>  
  
# Install Vim  
RUN apt-get update && apt-get install -y vim  
  
# prepare work directory  
WORKDIR /blog  
  
# add run script  
ADD ./startup.sh /bin/startup  
  
# install hexo  
RUN chmod +x /bin/startup && npm install hexo-cli -g  
  
# replace this with your application's default port  
EXPOSE 4000  
# run hexo server  
CMD ["/bin/startup"]  

