FROM node:latest  
MAINTAINER Ben Edmunds  
  
#Defaults Environment variables..will be overridden from docker run  
ENV HUBOT_SLACK_TOKEN xoxb-86458599122-dJtxMjdQgl7W22OcRIpalsSz  
ENV HUBOT_NAME chatbot  
ENV HUBOT_OWNER none  
ENV HUBOT_DESCRIPTION Hubot  
ENV EXTERNAL_SCRIPTS "hubot-help,hubot-pugme"  
ENV ADAPTER slack  
  
#ENV in case of hipchat  
ENV HUBOT_HIPCHAT_JID=123_456@chat.hipchat.com  
ENV HUBOT_HIPCHAT_PASSWORD=password  
ENV HUBOT_HIPCHAT_ROOMS=testroom  
  
#ENV for irc  
ENV HUBOT_IRC_SERVER=irc.freenode.net  
ENV HUBOT_IRC_ROOMS="#myhubot-irc"  
ENV HUBOT_IRC_NICK="myhubot"  
#HUBOT_IRC_USERNAME optional  
#HUBOT_IRC_PASSWORD optional  
#ENV for campfire  
ENV HUBOT_CAMPFIRE_ACCOUNT=test3068  
ENV HUBOT_CAMPFIRE_TOKEN=8c2f2aa475243aa009e3fdf8b0dfd596abd16965  
ENV HUBOT_CAMPFIRE_ROOMS=625159  
RUN useradd hubot -m  
  
RUN npm cache clean  
RUN npm install -g n  
RUN n stable  
RUN curl -L https://npmjs.org/install.sh | sh  
  
RUN npm install -g hubot coffee-script yo generator-hubot && npm cache clear  
  
RUN cd $(npm root -g)/npm && npm install fs-extra && sed -i -e s/graceful-
fs/fs-extra/ -e s/fs.rename/fs.move/ ./lib/utils/rename.js  
  
USER hubot  
  
WORKDIR /home/hubot  
  
RUN yo hubot --owner="${HUBOT_OWNER}" \--name="${HUBOT_NAME}"
\--description="${HUBOT_DESCRIPTION}" \--defaults && sed -i /redis-brain/d
./external-scripts.json && npm install hubot-scripts && npm install mysql &&
npm install hubot-slack --save && npm install hubot-hipchat --save && npm
install hubot-irc  
  
VOLUME ["/home/hubot/scripts"]  
  
CMD node -e "console.log(JSON.stringify('$EXTERNAL_SCRIPTS'.split(',')))" >
external-scripts.json && \  
npm install $(node -e "console.log('$EXTERNAL_SCRIPTS'.split(',').join(' '))")
&& \  
bin/hubot -n $HUBOT_NAME \--adapter $ADAPTER  

