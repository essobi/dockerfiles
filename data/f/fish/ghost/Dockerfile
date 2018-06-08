FROM mhart/alpine-node:4  
MAINTAINER Johannes 'fish' Ziemke <docker@freigeist.org>  
ENV GHOST_VERSION 0.11.7  
ENV NODE_ENV production  
  
EXPOSE 8080  
WORKDIR /usr/lib/ghost  
  
RUN apk --no-cache add --virtual dev curl \  
&& curl -LsSfo ghost.zip
https://github.com/TryGhost/Ghost/releases/download/${GHOST_VERSION}/Ghost-${GHOST_VERSION}.zip
\  
&& unzip ghost.zip \  
&& rm ghost.zip \  
&& npm install --production \  
&& npm cache clean \  
&& apk del dev \  
&& rm -rf /tmp/npm* \  
&& mkdir /var/lib/ghost \  
&& for s in images data apps; do mv content/$s /var/lib/ghost \  
&& ln -s /var/lib/ghost/$s content/; done \  
&& adduser -D -h /var/lib/ghost user \  
&& chown -R user:user /var/lib/ghost content/themes  
# No idea why ghost needs to have write permission to all those things..  
  
COPY config.js /usr/lib/ghost  
  
USER user  
VOLUME /var/lib/ghost  
  
ENTRYPOINT [ "node" ]  
CMD [ "index" ]  

