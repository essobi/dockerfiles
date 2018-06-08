FROM node:6  
MAINTAINER Push Innovation <devops@pushinnovation.com>  
  
#packages  
RUN apt-get update && apt-get install -y git openssh-client tar curl python
make g++ python-pip python-dev  
  
#docker  
RUN VER="17.03.0-ce" \  
&& curl -L -o /tmp/docker-$VER.tgz
https://get.docker.com/builds/Linux/x86_64/docker-$VER.tgz \  
&& tar -xz -C /tmp -f /tmp/docker-$VER.tgz \  
&& mv /tmp/docker/* /usr/bin \  
&& rm /tmp/docker-$VER.tgz  
  
#dockerize  
ENV DOCKERIZE_VERSION v0.5.0  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
#aws  
RUN pip install --upgrade awscli  
  
# npm  
RUN rm -rf /usr/local/lib/node_modules/npm \  
&& mkdir /usr/local/lib/node_modules/npm \  
&& curl -sL https://github.com/npm/npm/archive/v5.4.0.tar.gz | tar xz -C
/usr/local/lib/node_modules/npm --strip-components=1 \  
&& npm --version  
  
#yarn  
ENV YARN_VERSION 1.6.0  
RUN set -ex \  
&& for key in \  
6A010C5166006599AA17F08146C2130DFD2497F5 \  
; do \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \  
done \  
&& curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \  
&& curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz.asc" \  
&& gpg --batch --verify yarn-v$YARN_VERSION.tar.gz.asc
yarn-v$YARN_VERSION.tar.gz \  
&& rm -rf /opt/yarn /usr/local/bin/yarn /usr/local/bin/yarnpkg \  
&& mkdir -p /opt/yarn \  
&& tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/yarn --strip-components=1 \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarn \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarnpkg \  
&& rm yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz  
  
#add github public host key so we can push  
RUN git config --global user.email "devops@pushinnovation.com" \  
&& git config --global user.name "CircleCi" \  
&& mkdir ~/.ssh \  
&& ssh-keyscan -t rsa github.com > ~/.ssh/known_hosts  
  
EXPOSE 3000  

