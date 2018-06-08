FROM node:6  
MAINTAINER Pedro Maia <pedro.maia@ezdelivery.co>  
  
RUN apt-get update \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN npm install -g pusher-cli  
  
CMD ["pusher-cli"]  

