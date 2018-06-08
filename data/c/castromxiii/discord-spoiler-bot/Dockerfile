FROM node:8-alpine  
  
RUN apk update \  
&& apk upgrade \  
&& apk add alpine-sdk git python curl cairo-dev jpeg-dev pango-dev giflib-dev
\  
&& rm -f /usr/local/bin/yarn \  
&& curl -o- -L https://yarnpkg.com/install.sh | sh \  
&& chmod +x ~/.yarn/bin/yarn \  
&& ln -s ~/.yarn/bin/yarn /usr/local/bin/yarn \  
&& git clone https://github.com/ClaytonAstrom/discord-spoiler-bot.git \  
&& cd ./discord-spoiler-bot \  
&& yarn install  
  
ENTRYPOINT node /discord-spoiler-bot/index.js

