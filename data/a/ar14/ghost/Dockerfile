FROM alpine:3.4  
MAINTAINER aria@fallah.us  
  
ENV GHOST_USER ghost  
ENV GHOST_SOURCE /usr/src/app  
ENV GHOST_CONTENT /var/lib/ghost  
ENV GHOST_VERSION 0.8.0  
WORKDIR $GHOST_SOURCE  
  
RUN addgroup "$GHOST_USER" \  
&& adduser -D -h /home/"$GHOST_USER" -G "$GHOST_USER" "$GHOST_USER"  
  
RUN mkdir -p "$GHOST_SOURCE" \  
&& mkdir -p "$GHOST_CONTENT" \  
&& chown -R "$GHOST_USER":"$GHOST_USER" "$GHOST_CONTENT"  
  
RUN apk update \  
&& apk --no-cache add bash su-exec tar tini nodejs-lts \  
&& apk --no-cache add --virtual devs gcc make python wget unzip ca-
certificates \  
&& wget -O ghost.zip "https://ghost.org/archives/ghost-${GHOST_VERSION}.zip" \  
&& unzip ghost.zip \  
&& npm install --production \  
&& rm ghost.zip \  
&& apk del devs \  
&& npm cache clean \  
&& rm -rf /tmp/npm*  
  
COPY ./config.js $GHOST_SOURCE  
COPY ./entrypoint.sh /  
  
VOLUME $GHOST_CONTENT  
EXPOSE 2368  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["npm", "start"]  

