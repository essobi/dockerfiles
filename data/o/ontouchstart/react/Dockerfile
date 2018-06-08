FROM ontouchstart/node:0.10.36  
MAINTAINER Sam Liu <ontouchstart@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y git  
ADD . /react  
RUN cd /react && npm install -g grunt-cli && npm install && grunt build  

