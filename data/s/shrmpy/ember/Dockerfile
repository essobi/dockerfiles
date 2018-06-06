  
# build stage  
FROM alpine AS build-env  
RUN apk update; apk add openssl-dev autoconf automake libtool git \  
build-base gcc abuild binutils cmake linux-headers; \  
git clone https://github.com/facebook/watchman.git /root/watchman; \  
cd /root/watchman; git checkout v4.9.0; ./autogen.sh; ./configure --without-
python; make; make install;  
  
# final stage  
FROM node:alpine  
COPY \--from=build-env /usr/local/bin/watchman /usr/local/bin/watchman  
RUN mkdir -m 777 -p /usr/local/var/run/watchman  
RUN chmod g+s /usr/local/var/run/watchman  
RUN touch /usr/local/var/run/watchman/.not-empty  
RUN mkdir /app  
##RUN apk update; apk add openssl-dev; npm install --production -g ember-cli;
\  
RUN apk update; apk add openssl; npm install --production -g ember-cli; \  
rm -rf /var/cache/apk/*  
WORKDIR /app  
ENTRYPOINT ["/usr/local/lib/node_modules/ember-cli/bin/ember"]  
  

