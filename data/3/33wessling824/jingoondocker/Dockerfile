FROM mhart/alpine-node:latest  
  
MAINTAINER Achim Weßling <achim.wessling@gmail.com>  
  
LABEL version = 1.0.1 \  
description = "JINGO Wiki running on an Alpine based Docker image"  
  
ENV NODE_ENV production  
ENV GIT_USER user.name  
ENV GIT_MAIL user.name@some.mail  
  
RUN apk update && apk upgrade && \  
apk add --no-cache git && \  
git config --global user.name ${GIT_USER} && git config --global user.email
${GIT_MAIL} && \  
git clone https://github.com/claudioc/jingo.git /app && \  
mkdir /app/data && cd /app/data && git init && \  
cd .. && npm install && \  
mkdir /app/data/conf && ./jingo -s > data/conf/config.yaml && \  
sed -i -e "s|repository: ''|repository: '/app/data'|g" data/conf/config.yaml
&& \  
rm -rf /usr/share/man /tmp/* /var/cache/apk/* \  
/root/.npm /root/.node-gyp /root/.gnupg /usr/lib/node_modules/npm/man \  
/usr/lib/node_modules/npm/doc /usr/lib/node_modules/npm/html
/usr/lib/node_modules/npm/scripts \  
/app/test && \  
npm cache clean --force  
  
WORKDIR /app  
  
VOLUME /app/data  
  
ENTRYPOINT ["./jingo", "-c", "data/conf/config.yaml"]  

