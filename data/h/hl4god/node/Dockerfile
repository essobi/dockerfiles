FROM node:9-alpine  
  
LABEL maintainer="Holly <hl4god@gmail.com>"  
  
RUN apk upgrade --update \  
&& apk add --no-cache bash \  
python \  
python-dev \  
py-pip \  
build-base \  
&& npm config set registry https://registry.npm.taobao.org \  
&& rm -rf /var/cache/apk/*  
  
CMD [ "node" ]

