FROM node:6.11.4-alpine  
  
LABEL Author="Heiko Holland"  
LABEL Name=node-git-repo  
  
ENV GIT_REPO ""  
ENV GIT_BRANCH "master"  
ENV NODE_PM "npm"  
ENV BUILD_IONIC "false"  
ENV NPM_CONFIG_LOGLEVEL "silent"  
ENV ENABLE_REMOTE "false"  
ENV USE_START_SCRIPT "false"  
RUN apk update \  
&& apk add git \  
openssh-client \  
&& rm -rf /var/cache/apk/*  
  
# add fix for node-sass (https://github.com/sass/node-sass/issues/2031)  
ADD https://raw.githubusercontent.com/jubel-
han/dockerfiles/master/common/stack-fix.c /lib/  
RUN set -ex \  
&& apk add --no-cache --virtual .build-deps build-base \  
&& gcc -shared -fPIC /lib/stack-fix.c -o /lib/stack-fix.so \  
&& apk del .build-deps  
ENV LD_PRELOAD /lib/stack-fix.so  
  
RUN apk add --no-cache git \  
openssh-client  
  
RUN npm set progress false  
  
RUN yarn global add npm@5.5.1  
  
RUN npm i -g \  
ionic@3.13.2 \  
cordova@7.1.0 \  
yarn@1.2.1 \  
@hke/remote  
  
VOLUME /repository  
VOLUME /scripts  
VOLUME /app  
  
EXPOSE 3333  
COPY scripts/* /  
  
CMD /run.sh  

