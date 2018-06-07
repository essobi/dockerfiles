#Using nodejs image of Debian:Wheezy  
FROM node:5.10.1  
  
#Parse an Environment Variable for the directory where WhoBot will be located.  
ENV HUBOT_DIR=/opt/whobot  
  
#Install all of the pre-requisites for Hubot to work and to generate new
instances of itself.  
RUN npm install -g hubot coffee-script yo generator-hubot  
  
##Creates and cd's into the directory where our custom Hubot will go using the
variable we set earlier.  
RUN mkdir -p ${HUBOT_DIR}  
WORKDIR ${HUBOT_DIR}  
##Adds a user (node) that will give hubot permissions without giving it root
access  
RUN useradd -ms /bin/bash node  
RUN chown -R node ${HUBOT_DIR}  
USER node  
  
##Generates a new instance of Hubot named WhoBot.  
RUN yo hubot \--owner="Anton the Bot Wrangler" \--name="Hubot"
\--description="Anton's pet Hubot" \--adapter=slack --defaults --allow-root  
  
##Install's Slack Integration for Hubot.  
RUN npm install hubot-slack --save  
  
##ADD external-scripts.json /opt/hubot/external-scripts.json  
##Receives and adusts the Slack API Token for Hubot to make this Dockerized
Hubot script Universal.  
ENV HUBOT_SLACK_TOKEN=xxxxxxxxxxxxxxxxxxxx  
  
CMD ["./bin/hubot", "--adapter", "slack"]

