FROM docker:git  
  
RUN apk --no-cache add jq openssl  
  
ENV DOCKER_DRIVER=overlay  
  
ENV DOCKER_COMPOSE_VERSION=1.11.2\  
GLIBC=2.23-r3  
  
# See: https://github.com/docker/compose/blob/master/Dockerfile.run  
RUN set -x \  
&& wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub \  
&& wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/$GLIBC/glibc-$GLIBC.apk \  
&& apk add --no-cache glibc-$GLIBC.apk \  
&& rm glibc-$GLIBC.apk \  
&& ln -s /lib/libz.so.1 /usr/glibc-compat/lib/ \  
&& ln -s /lib/libc.musl-x86_64.so.1 /usr/glibc-compat/lib \  
&& wget -q -O /usr/local/bin/docker-compose
"https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-
compose-$(uname -s)-$(uname -m)" \  
&& chmod +x /usr/local/bin/docker-compose \  
&& docker-compose -v  
  
ENV RANCHER_CLI_VERSION 0.6.3  
  
RUN set -x \  
&& wget -q -O-
"https://github.com/rancher/cli/releases/download/v${RANCHER_CLI_VERSION}/rancher-
linux-amd64-v${RANCHER_CLI_VERSION}.tar.xz" | tar -C / -xJ \  
&& mv /rancher-v${RANCHER_CLI_VERSION}/rancher /usr/local/bin/ \  
&& rm -rf /rancher-v${RANCHER_CLI_VERSION} \  
&& rancher -v  
  

