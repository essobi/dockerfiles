FROM goldeneggg/hubot  
  
MAINTAINER goldeneggg  
  
# install hubot-irc  
WORKDIR /root/mybot  
RUN npm install hubot-irc --save && npm install  
  
# set hubot irc environment  
# HUBOT_IRC_SERVER and HUBOT_IRC_ROOMS must be indicated by `docker run -e
...`  
ENV HUBOT_IRC_NICK hubot  
ENV HUBOT_IRC_UNFLOOD true  
  
# HTTP Listener listen port 9980  
ENV PORT 9980  
EXPOSE 9980  
# run redis-server and hubot("-a irc")  
EXPOSE 6379  
RUN /etc/init.d/redis-server start  
ENTRYPOINT ["bin/hubot", "-a", "irc"]  
CMD ["--name", "myhubot"]  

