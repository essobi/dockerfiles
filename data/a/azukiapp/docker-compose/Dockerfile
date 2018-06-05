FROM docker  
  
ENV GLIBC 2.23-r3  
  
# Install dependencies  
# Based: https://github.com/docker/compose/issues/3465  
RUN set -xe && \  
apk update && apk add --no-cache \  
bash \  
git \  
curl \  
openssl \  
openssh \  
ca-certificates \  
&& \  
wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub && \  
wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/$GLIBC/glibc-$GLIBC.apk && \  
apk add --no-cache glibc-$GLIBC.apk && rm glibc-$GLIBC.apk && \  
ln -s /lib/libz.so.1 /usr/glibc-compat/lib/ && \  
ln -s /lib/libc.musl-x86_64.so.1 /usr/glibc-compat/lib  
# Install docker-compose  
ENV DOCKER_COMPOSE_VERSION 1.18.0  
  
RUN set -xe \  
&& curl -L
https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-
compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose \  
&& docker-compose --version  
  
CMD ["bash"]  

