FROM hongkongkiwi/node-watchman  
LABEL maintainer "Andy Savage"  
  
ENV NPM_CONFIG_LOGLEVEL error  
ENV TZ 'Asia/Hong_Kong'  
ENV NODE_ENV 'development'  
ENV WATCHMAN_VERSION '4.9.0'  
ENV WATCHMAN_REPO 'https://github.com/facebook/watchman.git'  
ENV SEND_EXISTING_FILES_ON_BOOT 'true'  
VOLUME ["/data", "/config"]  
  
WORKDIR /app  
  
RUN mkdir -p /var/cache/apk/ \  
&& apk update \  
&& apk add --no-cache \  
git file nano  
  
COPY . /app  
  
RUN npm install && \  
apk del --purge \  
git file nano \  
&& rm -rf /var/cache/apk/  
  
ENTRYPOINT [ "/sbin/tini", "--" ]  
CMD [ "npm", "start" ]  

