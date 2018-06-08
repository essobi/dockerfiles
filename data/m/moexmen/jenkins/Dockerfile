FROM jenkins/jenkins:lts-alpine  
  
ENV TZ Asia/Singapore  
ENV GLIBC 2.27-r0  
ENV DOCKER_VERSION 17.12.0  
ENV DOCKER_COMPOSE 1.19.0  
ENV GIT_LFS_VERSION 2.3.4  
  
USER root  
  
RUN \  
apk add --no-cache openssl tzdata rsync \  
&& ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
\  
&& curl -L -o docker-latest.tgz
https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}-ce.tgz
\  
&& tar -xvf docker-latest.tgz \  
&& mv docker/* /usr/bin \  
&& rm -rf docker docker-latest.tgz \  
&& wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub \  
&& wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/$GLIBC/glibc-$GLIBC.apk \  
&& apk add --no-cache glibc-$GLIBC.apk && rm glibc-$GLIBC.apk \  
&& ln -s /lib/libz.so.1 /usr/glibc-compat/lib/ \  
&& ln -s /lib/libc.musl-x86_64.so.1 /usr/glibc-compat/lib \  
&& curl -L
https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE}/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose \  
&& curl -L -o git-lfs.tar.gz https://github.com/git-lfs/git-
lfs/releases/download/v${GIT_LFS_VERSION}/git-lfs-linux-
amd64-${GIT_LFS_VERSION}.tar.gz \  
&& tar -xvzf git-lfs.tar.gz \  
&& ./git-lfs-${GIT_LFS_VERSION}/install.sh \  
&& rm -rf git-lfs.tar.gz git-lfs-${GIT_LFS_VERSION} \  
  
USER jenkins  

