FROM node:slim  
MAINTAINER toughiq@gmail.com  
  
# update system, install git and remove apt files afterwards  
RUN apt-get update \  
&& apt-get install -y git \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# fetch source code  
RUN git clone https://github.com/cprerovsky/rest-quest.git  
  
# change to code directory  
WORKDIR /rest-quest  
  
# change BASE_URL param in client.js to work with docker  
RUN sed -i 's/localhost/rqserver/' client.js  
  
# install node packages  
RUN npm install --ignore-scripts  
  
# set server start as default  
CMD ["node","server.js"]  
  

