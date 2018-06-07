FROM ubuntu:14.04  
RUN apt-get update  
RUN apt-get -y install expect redis-server nodejs npm  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
RUN npm install -g yo generator-hubot coffee-script  
ADD install_hubot /usr/local/bin/install_hubot  
RUN chmod +x /usr/local/bin/install_hubot  
RUN /usr/local/bin/install_hubot  
RUN npm install .  
RUN npm install hubot-hipchat  
RUN chmod 755 bin/hubot  
  
RUN apt-get -y install supervisor  
RUN mkdir -p /var/log/supervisor  
  
ADD hubot-scripts.json hubot-scripts.json  
ADD ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
CMD supervisord -n  
  

