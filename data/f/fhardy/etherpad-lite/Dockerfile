# Stable version of etherpad doesn't support npm 2  
FROM alpine:3.6  
MAINTAINER Flavien Hardy <flav.hardy@gmail.com>  
  
ENV ETHERPAD_VERSION 1.6.1  
RUN apk add -U curl unzip nodejs-npm mysql-client bash && \  
curl -SL https://github.com/ether/etherpad-
lite/archive/${ETHERPAD_VERSION}.zip > etherpad.zip && \  
unzip etherpad && \  
rm etherpad.zip && \  
mv etherpad-lite-${ETHERPAD_VERSION} /etherpad-lite && \  
adduser -D etherpad && \  
chown -R etherpad:etherpad /etherpad-lite && \  
rm -rf /var/cache/apk/*  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chown etherpad:etherpad /entrypoint.sh  
  
WORKDIR /etherpad-lite  
USER etherpad  
RUN bin/installDeps.sh && rm /etherpad-lite/settings.json  
  
VOLUME /etherpad-lite/node_modules /etherpad-lite/var  
EXPOSE 9001  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/usr/bin/node","/etherpad-lite/node_modules/ep_etherpad-
lite/node/server.js"]  

