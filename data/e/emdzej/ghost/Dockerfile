FROM emdzej/node:lts  
  
MAINTAINER Michał Jaskólski <michal@jaskolski.online>  
  
ENV GHOST_HOME /var/www/ghost  
ENV GHOST_CONTENT /var/lib/ghost  
  
RUN addgroup ghost  
RUN adduser -H -h "$GHOST_HOME" -D -G ghost ghost  
  
RUN mkdir -p "$GHOST_HOME"  
RUN mkdir -p "$GHOST_CONTENT"  
  
RUN apk add --no-cache curl ca-certificates su-exec  
  
RUN cd /tmp && curl -s -L https://ghost.org/zip/ghost-latest.zip -o ghost.zip  
  
RUN cd /tmp && unzip -o ghost.zip -d "$GHOST_HOME"  
RUN cd "$GHOST_HOME/content" && mv * "$GHOST_CONTENT"  
  
RUN chown -R ghost:ghost "$GHOST_HOME" && chown -R ghost:ghost
"$GHOST_CONTENT"  
  
RUN rm /tmp/ghost.zip  
  
RUN cd "$GHOST_HOME" && npm install --production \  
&& npm cache clean \  
&& rm -rf /tmp/npm*  
  
COPY config.js "$GHOST_HOME"  
  
VOLUME $GHOST_CONTENT  
  
EXPOSE 2368  
WORKDIR $GHOST_HOME  
  
ENTRYPOINT ["npm"]  
  
CMD ["start", "--production"]  
  

