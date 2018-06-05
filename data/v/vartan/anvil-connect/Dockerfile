FROM mhart/alpine-node:5.1.0  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN addgroup -S connect && adduser -S -G connect connect  
  
# grab gosu for easy step-down from root  
RUN apk add --update ca-certificates curl gnupg && \  
gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 && \  
ARCH=`uname -m`; if [ $ARCH == "x86_64" ]; then export ARCH="amd64"; else
export ARCH="i386"; fi && \  
curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.6/gosu-$ARCH" && \  
curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.6/gosu-$ARCH.asc" && \  
gpg --verify /usr/local/bin/gosu.asc && \  
rm /usr/local/bin/gosu.asc && \  
chmod +x /usr/local/bin/gosu && \  
apk del ca-certificates curl gnupg && \  
rm -rf /var/cache/apk/*  
  
ENV ANVIL_CONNECT_VERSION 0.1.58  
ENV NODE_ENV production  
  
COPY runner /usr/src/anvil-connect  
  
RUN apk add --update ca-certificates git python make g++ gcc openssl && \  
npm install -g /usr/src/anvil-connect && \  
rm -r /usr/src/anvil-connect && \  
rm -rf /root/.npm && \  
apk del ca-certificates git python make g++ gcc && \  
rm -rf /var/cache/apk/*  
  
ENV NODE_PATH /usr/lib/node_modules/docker-anvil-connect/node_modules  
  
RUN mkdir /connect && \  
mkdir /connect/keys && \  
mkdir /connect/secrets && \  
chown -R connect:connect /connect  
VOLUME /connect/keys  
VOLUME /connect/secrets  
WORKDIR /connect  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 3000  
CMD [ "anvil-connect" ]  

