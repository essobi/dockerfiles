FROM ubuntu:16.04  
  
# COPY sources.list /etc/apt/sources.list  
RUN apt-get update && apt-get install -y npm ruby-compass git  
  
# RUN ln -s /usr/bin/nodejs /usr/bin/node \  
# && npm config -g set registry https://registry.npm.taobao.org \  
# && npm install -g grunt-cli bower yo generator-karma generator-angular  
RUN ln -s /usr/bin/nodejs /usr/bin/node \  
&& npm install -g grunt-cli bower yo generator-karma generator-angular  
  
RUN useradd -m -s /bin/bash www  
  
USER www  
WORKDIR /project  
CMD grunt serve  
EXPOSE 9000  

