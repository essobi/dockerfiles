FROM node:8.9.3-alpine  
  
LABEL maintainer="We ahead <docker@weahead.se>"  
  
ENV S6_VERSION=1.20.0.0\  
S6_BEHAVIOUR_IF_STAGE2_FAILS=2  
RUN apk --no-cache add curl git su-exec \  
&& apk --no-cache add --virtual build-deps \  
gnupg \  
&& cd /tmp \  
&& curl -OL "https://github.com/just-
containers/s6-overlay/releases/download/v${S6_VERSION}/s6-overlay-
amd64.tar.gz" \  
&& curl -OL "https://github.com/just-
containers/s6-overlay/releases/download/v${S6_VERSION}/s6-overlay-
amd64.tar.gz.sig" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& curl https://keybase.io/justcontainers/key.asc | gpg --import \  
&& gpg --verify s6-overlay-amd64.tar.gz.sig s6-overlay-amd64.tar.gz \  
&& tar -xzf /tmp/s6-overlay-amd64.tar.gz -C / \  
&& rm -rf "$GNUPGHOME" /tmp/* \  
&& apk del build-deps  
  
ENV NODE_ENV=production  
  
WORKDIR /app  
  
COPY root /  
  
EXPOSE 3000  
ENTRYPOINT ["/init"]  
  
ONBUILD COPY app/package.json /app/package.json  
  
ONBUILD RUN chown node:node /app \  
&& su-exec node npm install \  
&& touch /home/node/.fix-npm-clean \  
&& su-exec node npm cache clean --force \  
&& rm /home/node/.fix-npm-clean  
  
ONBUILD COPY app/ /app-tmp  
  
ONBUILD RUN chown node:node /app-tmp \  
&& rm -rf /app-tmp/node_modules \  
&& cp -R /app-tmp/. /app/ \  
&& rm -rf /app-tmp  

