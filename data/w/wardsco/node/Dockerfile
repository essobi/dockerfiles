FROM node:8.0.0-alpine  
  
WORKDIR /usr/src/app/  
RUN apk --no-cache add --virtual .build-deps \  
build-base \  
openssl-dev \  
libffi-dev \  
zlib-dev \  
python2  
  
ONBUILD ARG BUILD_DEPS=  
ONBUILD ARG BYPASS_PIP_INSTALL_ERRORS=  
  
ONBUILD RUN echo $BUILD_DEPS | xargs -r apk --no-cache add --virtual .build-
deps  
ONBUILD COPY . .  
# HACK: Copy current directory. Need optional COPY feature from Docker  
# ONBUILD COPY package.json .  
# ONBUILD COPY yarn.lock .  
ONBUILD RUN test -f yarn.lock && yarn install || npm install  
ONBUILD RUN apk del .build-deps  

