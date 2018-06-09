#  
# Dockerfile for telegram2irc-bot.  
#  
FROM alpine  
MAINTAINER stawidy <duyizhaozj321@yahoo.com>  
  
ARG GIT_URL=https://github.com/wfjsw/telegram2irc-bot.git  
ARG SRC_DIR=/telegram2irc-bot  
  
RUN set -x \  
&& apk add --no-cache --virtual .build-deps \  
autoconf \  
build-base \  
git \  
icu-dev \  
python \  
&& apk add --no-cache nodejs \  
&& git clone $GIT_URL \  
&& cd $SRC_DIR \  
&& npm install \  
&& cd .. \  
&& apk del .build-deps \  
&& rm -rf /tmp/*  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
ENV TG_BOT_API_KEY='' \  
TG_GROUP_ID='' \  
IRC_SERVER=irc.freenode.net \  
IRC_CHANNEL='' \  
IRC_NICK=akarin_bot \  
IRC_PORT=6667 \  
IRC_PHOTO=true \  
EX_BOTS=other_bot  
  
WORKDIR /telegram2irc-bot  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["node", "main.js"]  

