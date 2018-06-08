FROM qnib/d-node  
  
RUN apt-get update \  
&& apt-get install -y git  
#### Inspired by  
# https://github.com/RocketChat/hubot-rocketchat/blob/master/Dockerfile  
RUN npm install -g coffee-script yo generator-hubot && \  
useradd hubot -m  
  
#ADD hubot-graphme.tar /home/hubot/node_modules/  
#RUN chown -R hubot: /home/hubot/node_modules  
USER hubot  
  
WORKDIR /home/hubot  
  
ENV DEV=false \  
BOT_NAME="bot" \  
BOT_OWNER="Christian Kniep <christian@qnib.org>" \  
BOT_DESC="Hubot with rocketbot adapter"  
ENV EXTERNAL_SCRIPTS=hubot-diagnostics,hubot-help,hubot-google-images,hubot-
google-translate,hubot-maps,hubot-rules,hubot-grafana,hubot-shipit,hubot-
graphme,hubot-business-cat,hubot-tell  
  
RUN yo hubot --owner="$BOT_OWNER" \--name="$BOT_NAME"
\--description="$BOT_DESC" \--defaults && \  
sed -i /heroku/d ./external-scripts.json && \  
sed -i /redis-brain/d ./external-scripts.json && \  
npm install hubot-rocketchat  
  
RUN node -e "console.log(JSON.stringify('$EXTERNAL_SCRIPTS'.split(',')))" >
external-scripts.json && \  
npm install $(node -e "console.log('$EXTERNAL_SCRIPTS'.split(',').join(' '))")
&& \  
if $DEV; then coffee -c /home/hubot/node_modules/hubot-
rocketchat/src/*.coffee; fi  
ADD etc/supervisord.d/hubot.ini /etc/supervisord.d/  
ADD opt/qnib/hubot/bin/start.sh /opt/qnib/hubot/bin/  
CMD /opt/qnib/hubot/bin/start.sh 30  
ADD hubot-graphme/src/graph-me.coffee /home/hubot/node_modules/hubot-
graphme/src/graph-me.coffee  
USER root  
RUN chown -R hubot: /home/hubot/node_modules/hubot-graphme  
#WORKDIR /root/  
USER hubot  
#RUN sed -i -e 's;Configuration.*;#{url}/render?#{query.join("\&")}";'
/home/hubot/node_modules/hubot-graphme/src/graph-me.coffee  
### When supervisord takes over...  

