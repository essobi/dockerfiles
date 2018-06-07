FROM fabric8/hubot-base:v1.0.0  
  
MAINTAINER fabric8.io <fabric8@googlegroups.com>  
  
USER root  
  
RUN yum install -y jq  
  
# Add modified letschat adapter  
RUN mkdir -p hubot-lets-chat/src  
ADD package.json hubot-lets-chat/  
ADD src hubot-lets-chat/src/  
RUN npm link hubot-lets-chat  
  
RUN npm install -g engine.io-client inherits  
  
RUN chown -R hubot:hubot /home/hubot  
  
USER hubot  
  
RUN yo hubot \--owner="fabric8.io <fabric8@googlegroups.com>"
\--name="fabric8" \--description="Platform manager" \--adapter=lets-chat
--defaults  
  
ADD external-scripts.json /home/hubot/  
ADD start.sh /home/hubot/  
  
ENV HUBOT_LOG_LEVEL debug  
  
CMD /home/hubot/start.sh  

