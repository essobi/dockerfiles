FROM node:6-alpine  
  
LABEL maintainer="https://github.com/pluralcafe/barkeep" \  
description="Ambassador bot forked from mbilokonsky/ambassador"  
  
ENV UID=992  
ENV GID=992  
WORKDIR /barkeep  
  
RUN apk -U upgrade \  
&& apk add -t build-dependencies \  
build-base \  
postgresql-dev \  
&& apk add tini \  
ca-certificates \  
tzdata \  
&& update-ca-certificates \  
&& rm -rf /tmp/* /var/cache/apk/* \  
&& addgroup -g ${GID} barkeep \  
&& adduser -h /barkeep -s /bin/sh -D -G barkeep -u ${UID} barkeep  
  
COPY package.json index.js yarn.lock /barkeep/  
  
RUN yarn install \  
&& chown -R barkeep:barkeep /barkeep  
  
USER barkeep  
  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD ["yarn", "start"]  

