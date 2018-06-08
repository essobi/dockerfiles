FROM node:6.8  
MAINTAINER Pedro Maia <pedro.maia@ezdelivery.co>  
  
RUN apt-get update \  
&& rm -rf /var/lib/apt/lists/*  
  
#RUN npm install -g slack-cli  
RUN npm install -g slack-webhook-cli  
  
CMD ["slack-hook"]  

