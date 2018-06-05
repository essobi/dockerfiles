FROM node:8-alpine  
  
ENV SERVICE_ROOT /service  
ENV SERVICE_USER service  
ENV YARN_VERSION 1.6.0  
RUN apk add --no-cache bash make gcc g++ binutils jq sudo unzip  
  
RUN apk upgrade --no-cache binutils jq sudo unzip  
  
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
&& rm -rf /usr/local/bin/yarn \  
&& rm -rf /usr/local/bin/yarnpkg \  
&& ln -s /opt/yarn-v$YARN_VERSION/bin/yarn /usr/local/bin/yarn \  
&& ln -s /opt/yarn-v$YARN_VERSION/bin/yarnpkg /usr/local/bin/yarnpkg \  
&& rm yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz \  
&& apk del .build-deps-yarn  
  
ADD https://raw.githubusercontent.com/articulate/docker-consul-template-
bootstrap/master/install.sh /tmp/consul_template_install.sh  
RUN bash /tmp/consul_template_install.sh && rm /tmp/consul_template_install.sh  
  
RUN addgroup $SERVICE_USER && adduser -h $SERVICE_ROOT -G $SERVICE_USER -s
/bin/bash $SERVICE_USER -D  
WORKDIR $SERVICE_ROOT  
  
ADD https://raw.githubusercontent.com/articulate/docker-consul-template-
bootstrap/master/wait-for-it.sh /wait-for-it.sh  
RUN chmod a+rx /wait-for-it.sh  
  
RUN yarn global add node-gyp  
  
ENTRYPOINT ["/entrypoint.sh"]  

