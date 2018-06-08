#  
# Ghost Dockerfile  
#  
# https://github.com/dockerfile/ghost  
#  
  
# Pull base image.  
#FROM dockerfile/nodejs  
FROM node:boron-alpine  
  
SHELL ["/bin/sh", "-c"]  
  
#  
# Ghost install zip url  
# [ ]  
#ENV GHOSTURL
https://api.hgrg.info/github/repos/TryGhost/Ghost/releases/latest/zip  
#Replace local url with new check-service  
#ENV GHOSTURL http://gh-check.herokuapp.com/api/v1/lastreleaseurl  
ENV GHOSTURL https://kamino.hgrg.info/api/v1/lastreleaseurl  
  
#########################################  
### Set Ghost environment variables.  
#########################################  
# NODE_ENV: [production / development* ] *default  
ENV NODE_ENV production  
  
### Server listen options  
#ENV server__host 0.0.0.0  
#ENV server__port 2368  
  
### URL is just for production  
#ENV url http://my-ghost-blog.com  
  
### DATABASE settings  
## - SQLITE3  
ENV database__client sqlite3  
ENV database__connection__filename /ghost/content/data/ghost.sqlite3.db  
#ENV database__useNullAsDefault true  
#ENV database__debug false  
## - MySQL  
#ENV database__client mysql  
#ENV database__connection__host  
#ENV database__connection__user  
#ENV database__connection__password  
#ENV database__connection__database  
#ENV database__useNullAsDefault true  
#ENV database__debug false  
  
### Auth  
# Auth.type: [ghost / password]  
ENV auth__type password  
  
ENV paths__contentPath="/ghost/content/"  
### Logging  
##  
ENV logging__level error  
ENV logging__rotation__enabled false  
#ENV logging__transports ["stdout"]  
#ENV logging__path /ghost/content/logs  
  
# Define mountable directories.  
VOLUME ["/data", "/ghost-override"]  
  
# Install Ghost  
RUN \  
addgroup -S ghost && adduser -S -g ghost ghost -h /ghost && \  
apk update && apk add wget unzip git sed && \  
cd /tmp && \  
wget -O ghost-latest.zip ${GHOSTURL:-https://ghost.org/zip/ghost-latest.zip}
&& \  
unzip ghost-latest.zip -d /ghost && \  
rm -f ghost-latest.zip && \  
cd /ghost && \  
yarn install --prod && yarn global add knex-migrator && \  
knex-migrator init && knex-migrator-migrate && \  
# sed 's/127.0.0.1/0.0.0.0/' /ghost/config.example.js > /ghost/config.js && \  
# sed "s/127.0.0.1/0.0.0.0/;s/'2368'/process.env.PORT || '2368'/"
/ghost/config.example.js > /ghost/config.js && \  
### Dirty-dirty hack to let openshift boot the image..  
echo '{"logging": {"transports": ["stdout"]}}' > /ghost/config.production.json
&& \  
apk del zip unzip git wget sed && \  
# yarn global remove knex-migrator && \  
yarn cache clean && \  
rm -rf /tmp/npm* && \  
chown -R ghost:ghost /ghost  
#chown -R ghost:ghost /data /ghost /ghost-override  
  
# Add files.  
ADD start.bash /ghost-start  
  
# Define working directory.  
WORKDIR /ghost  
  
# Define default command.  
#CMD ["bash", "/ghost-start"]  
#CMD ["sh", "-c", "chown -R ghost:ghost /ghost"]  
  
USER ghost  
CMD ["sh", "-c", "knex-migrator-migrate --init"]  
CMD ["sh", "-c", "NODE_ENV=${NODE_ENV:-production} server__port=${PORT:-2368}
server__host=${server__host:-0.0.0.0} url=${url:-http://localhost:2368} node
index"]  
  
# Expose ports.  
EXPOSE 2368  

