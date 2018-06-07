FROM node:6-slim  
  
LABEL maintainer "Charlie McClung <charlie.mcclung@autodesk.com>"  
  
ENV DEHYDRATED_VERSION=0.4.0  
RUN mkdir -p /var/www/dehydrated  
  
RUN curl -L
https://github.com/lukas2511/dehydrated/archive/v$DEHYDRATED_VERSION.tar.gz -o
/tmp/dehydrated.tar.gz  
RUN tar xvzf /tmp/dehydrated.tar.gz -C /tmp  
RUN mv /tmp/dehydrated-$DEHYDRATED_VERSION /etc/dehydrated  
RUN rm -rf /tmp/dehydrated*  
  
ENV SSLR_DIR /sslr  
  
RUN mkdir -p $SSLR_DIR  
  
WORKDIR $SSLR_DIR  
  
COPY dehydrated/config /etc/dehydrated/config  
  
COPY package.json .  
  
RUN npm install  
  
COPY . .  
  
VOLUME [ "/etc/dehydrated" ]  
  
ENTRYPOINT [ "./docker-entrypoint.sh" ]  
  
CMD [ "npm", "start" ]

