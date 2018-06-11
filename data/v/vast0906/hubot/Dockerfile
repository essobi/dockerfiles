FROM node:6.2.0  
ENV TZ=Asia/Shanghai  
ENV BOT_NAME "007"  
ENV BOT_OWNER "vast"  
ENV BOT_DESC "none"  
ENV HUBOT_BEARYCHAT_TOKENS ""  
ENV HUBOT_BEARYCHAT_MODE "rtm"  
USER root  
RUN npm install -g hubot coffee-script yo generator-hubot && useradd -ms
/bin/bash hubot  
##node  
USER hubot  
WORKDIR /home/hubot  
RUN yo hubot --owner="$BOT_OWNER" \--name="$BOT_NAME"
\--description="$BOT_DESC" \--defaults \  
&& npm install hubot-bearychat --save \  
&& npm install hubot-script-shellcmd --save \  
&& cp -R node_modules/hubot-script-shellcmd/bash/ ./ \  
&& sed -i '2a\ "hubot-script-shellcmd",' ./external-scripts.json  
ENTRYPOINT ["/bin/sh", "-c", "./bin/hubot -a bearychat;"]  

