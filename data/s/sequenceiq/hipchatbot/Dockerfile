FROM dockerfile/nodejs  
  
RUN apt-get update  
  
RUN apt-get -y install wget python-dev g++ make libexpat1-dev libicu-dev
redis-server  
  
RUN npm install --global coffee-script hubot@v2.6.4  
RUN hubot --create /opt/hubot  
WORKDIR /opt/hubot  
ADD hubot-scripts.json /opt/hubot/hubot-scripts.json  
ADD scripts/ /opt/hubot/scripts/  
RUN npm install  
RUN npm install --save hubot-hipchat  
  
CMD redis-server /etc/redis/redis.conf && bin/hubot --adapter hipchat  

