FROM node:8.9.3-slim  
  
# Change node uid to our own uid  
# Note that you MUST build this image where you use it  
# Install wanted packages  
RUN apt-get update && apt-get install -yyq \  
git python python-dev python-pip python-virtualenv sudo \  
&& apt-get clean \  
&& npm install -g node-gyp bower@1.8.2 gulp@3.9.1 \  
&& npm cache clean -f \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /data  
  
CMD ["bash"]  

