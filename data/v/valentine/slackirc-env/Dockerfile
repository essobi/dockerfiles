# Copyright 2016 Valentine C  
FROM justcontainers/base-alpine  
  
MAINTAINER Valentine C  
  
# setting user as root to prevent npm from flipping out  
ENV USER=root \  
HOME=/tmp  
  
RUN apk add --update \  
nodejs-lts \  
# dependencies for node-gyp  
python \  
make \  
g++ \  
# dependency for icu  
icu-dev \  
&& npm install -g slack-irc \  
&& apk del make gcc g++ python \  
&& rm -rf /tmp/* /var/cache/apk/* /root/.npm /root/.node-gyp  
  
# terminate and exit if env-check fails  
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS 2  
COPY 00-env-check.sh etc/cont-init.d/00-env-check  
COPY 01-config-env.sh etc/cont-init.d/01-config-env  
  
COPY config.json.sample slack-irc/config.json  
COPY slackirc-run.sh etc/services.d/slack-irc/run  
  
ENTRYPOINT ["/init"]

