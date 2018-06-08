FROM node:8-alpine  
RUN ln -s /opt/yarn-v$YARN_VERSION/ /opt/yarn  
  
FROM jrottenberg/ffmpeg:3.3-alpine  
COPY \--from=0 /usr/local/bin/node /usr/bin/  
COPY \--from=0 /usr/lib/libgcc* /usr/lib/libstdc* /usr/lib/  
  
COPY \--from=0 /opt/yarn/. /opt/yarn  
RUN ln -s /opt/yarn/bin/yarn /usr/local/bin/yarn \  
&& ln -s /opt/yarn/bin/yarnpkg /usr/local/bin/yarnpkg  
  
WORKDIR /app  
COPY . .  
RUN yarn install --production  
  
RUN mkdir /tmp/transcoder_logs  
  
EXPOSE 3000  
ENTRYPOINT [""]  
CMD ["node", "app.js"]

