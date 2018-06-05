FROM node:4-slim  
  
MAINTAINER Lukas Pustina <lukas.pustina@gmail.com>  
  
RUN npm install -g coffee-script yo generator-hubot  
RUN adduser --home /carl carl  
  
USER carl  
WORKDIR /carl  
  
ENV HUBOT_NAME "Carl"  
ENV HUBOT_OWNER "Lukas Pustina <lukas.pustina@gmail.com>"  
ENV HUBOT_DESCRIPTION "Your friendly Ops Minion"  
ENV HUBOT_SLACK_VERSON="3.4.2"  
RUN yo hubot --name="$HUBOT_NAME" \--owner="$HUBOT_OWNER"
\--description="$HUBOT_DESCRIPTION" \--adapter=slack@${HUBOT_SLACK_VERSON}
\--defaults  
  
# Install Scripts  
RUN npm install --save hubot-diagnostics  
RUN npm install --save hubot-auth@1.3.0  
RUN npm install --save hubot-http-status  
RUN npm install --save hubot-seen  
RUN npm install --save hubot-calculator  
RUN npm install --save hubot-grafana  
RUN npm install --save hubot-bosun  
COPY docker/external-scripts.json /carl/  
  
ENTRYPOINT ["/bin/sh", "-c", "cd ~; ./bin/hubot -a slack;"]  
  

