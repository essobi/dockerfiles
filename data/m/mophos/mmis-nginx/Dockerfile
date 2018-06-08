FROM nginx:stable-alpine  
  
LABEL maintainer="Satit Rianpit <rianpit@gmail.com>"  
  
ENV YARN_VERSION 1.7.0  
RUN apk update && apk upgrade && apk add --no-cache git openssh  
  
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/main | tee
/etc/apk/repositories \  
&& echo @testing http://dl-cdn.alpinelinux.org/alpine/edge/testing | tee -a
/etc/apk/repositories \  
&& echo @community http://dl-cdn.alpinelinux.org/alpine/edge/community | tee
-a /etc/apk/repositories \  
&& apk add --update openssl \  
&& apk add --update nodejs \  
&& apk add --update nodejs-npm \  
&& apk add --update mysql-client  
  
RUN apk add --no-cache --virtual .build-deps-yarn curl gnupg tar \  
&& for key in \  
6A010C5166006599AA17F08146C2130DFD2497F5 \  
; do \  
gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" || \  
gpg --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" || \  
gpg --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" ; \  
done \  
&& curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \  
&& curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz.asc" \  
&& gpg --batch --verify yarn-v$YARN_VERSION.tar.gz.asc
yarn-v$YARN_VERSION.tar.gz \  
&& mkdir -p /opt \  
&& tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/ \  
&& ln -s /opt/yarn-v$YARN_VERSION/bin/yarn /usr/local/bin/yarn \  
&& ln -s /opt/yarn-v$YARN_VERSION/bin/yarnpkg /usr/local/bin/yarnpkg \  
&& rm yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz \  
&& apk del .build-deps-yarn  
  
EXPOSE 80  

