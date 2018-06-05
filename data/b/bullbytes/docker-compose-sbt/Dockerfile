# Our base image: https://hub.docker.com/_/openjdk/  
# The JRE is used to start SBT which will download compilers, plugins, and
their dependencies  
FROM openjdk:8u131-jre-alpine  
  
MAINTAINER Matthias Braun <matthias@bullbytes.com>  
  
# Install curl, bash (needed by SBT), and py-pip which we use to install
Docker Compose  
RUN apk add --no-cache bash curl py-pip  
  
# Install SBT  
ARG sbtVersion=0.13.15  
ARG sbtHome=/usr/local/sbt  
ENV PATH ${PATH}:${sbtHome}/bin  
  
ARG
sbtArchiveUrl=https://github.com/sbt/sbt/releases/download/v$sbtVersion/sbt-$sbtVersion.tgz  
  
RUN mkdir -p "$sbtHome" && curl -L $sbtArchiveUrl | tar xz --strip-components
1 --directory $sbtHome  
  
# Install Docker Compose using pip which also installs the required glibc.  
# To install without pip, see https://github.com/wernight/docker-compose or
https://github.com/ncrmro/docker-and-compose  
RUN pip install docker-compose  
  
# Install Docker  
ARG docker_channel=edge  
# See this for the most recent version:
https://github.com/moby/moby/blob/master/CHANGELOG.md  
ARG dockerVersion=17.05.0-ce  
  
RUN curl -L
"https://download.docker.com/linux/static/${docker_channel}/x86_64/docker-${dockerVersion}.tgz"
| tar xz --strip-components 1 --directory /usr/local/bin/  
  
# Make Docker in Docker work  
RUN apk add --no-cache \  
btrfs-progs \  
e2fsprogs \  
e2fsprogs-extra \  
iptables \  
xfsprogs \  
xz  
  
# set up subuid/subgid so that "--userns-remap=default" works out-of-the-box  
RUN set -x \  
&& addgroup -S dockremap \  
&& adduser -S -G dockremap dockremap \  
&& echo 'dockremap:165536:65536' >> /etc/subuid \  
&& echo 'dockremap:165536:65536' >> /etc/subgid  
  
ENV DIND_COMMIT 3b5fac462d21ca164b3778647420016315289034  
  
RUN set -ex; \  
apk add --no-cache --virtual .fetch-deps libressl; \  
wget -O /usr/local/bin/dind
"https://raw.githubusercontent.com/docker/docker/${DIND_COMMIT}/hack/dind"; \  
chmod +x /usr/local/bin/dind; \  
apk del .fetch-deps  
  
COPY dockerd-entrypoint.sh /usr/local/bin/  
# Make sure the entrypoint script is executable  
RUN chmod 755 /usr/local/bin/dockerd-entrypoint.sh  
  
VOLUME /var/lib/docker  
EXPOSE 2375  
# Some smoke testing  
RUN ["docker-compose", "version"]  
RUN ["docker", "-v"]  
RUN ["dockerd", "-v"]  
RUN ["sbt", "sbtVersion"]  
  
# Remove py-pip that we used to install Docker-Compose. We can't remove bash
since SBT needs it. Also, Docker Compose requires curl  
RUN apk del py-pip  
  
ENTRYPOINT ["dockerd-entrypoint.sh"]  
CMD []  

