FROM openjdk:8-jdk-alpine  
MAINTAINER Xi Song <songxic@gmail.com>  
  
ENV HOME /home/jenkins  
RUN addgroup -S -g 10000 jenkins  
RUN adduser -S -u 10000 -h $HOME -G jenkins jenkins  
LABEL Description="This is a base image, which provides the Jenkins agent
executable (slave.jar)" Vendor="Jenkins project" Version="3.10"  
  
RUN apk add --no-cache \  
ca-certificates  
  
ENV DOCKER_CHANNEL stable  
ENV DOCKER_VERSION 17.06.2-ce  
# TODO ENV DOCKER_SHA256  
# https://github.com/docker/docker-
ce/blob/5b073ee2cf564edee5adca05eee574142f7627bb/components/packaging/static/hash_files
!!  
# (no SHA file artifacts on download.docker.com yet as of 2017-06-07 though)  
RUN set -ex; \  
# why we use "curl" instead of "wget":  
# + wget -O docker.tgz
https://download.docker.com/linux/static/stable/x86_64/docker-17.03.1-ce.tgz  
# Connecting to download.docker.com (54.230.87.253:443)  
# wget: error getting response: Connection reset by peer  
apk add \--no-cache --virtual .fetch-deps \  
curl \  
tar \  
; \  
\  
# this "case" statement is generated via "update.sh"  
apkArch="$(apk --print-arch)"; \  
case "$apkArch" in \  
x86_64) dockerArch='x86_64' ;; \  
s390x) dockerArch='s390x' ;; \  
*) echo >&2 "error: unsupported architecture ($apkArch)"; exit 1 ;;\  
esac; \  
\  
if ! curl -fL -o docker.tgz
"https://download.docker.com/linux/static/${DOCKER_CHANNEL}/${dockerArch}/docker-${DOCKER_VERSION}.tgz";
then \  
echo >&2 "error: failed to download 'docker-${DOCKER_VERSION}' from
'${DOCKER_CHANNEL}' for '${dockerArch}'"; \  
exit 1; \  
fi; \  
\  
tar --extract \  
\--file docker.tgz \  
\--strip-components 1 \  
\--directory /usr/local/bin/ \  
; \  
rm docker.tgz; \  
\  
apk del .fetch-deps; \  
\  
dockerd -v; \  
docker -v  
  
ARG VERSION=3.10  
ARG AGENT_WORKDIR=/home/jenkins/agent  
  
RUN apk add --update --no-cache curl bash git openssh-client openssl \  
&& curl --create-dirs -sSLo /usr/share/jenkins/slave.jar https://repo.jenkins-
ci.org/public/org/jenkins-ci/main/remoting/${VERSION}/remoting-${VERSION}.jar
\  
&& chmod 755 /usr/share/jenkins \  
&& chmod 644 /usr/share/jenkins/slave.jar \  
&& apk del curl  
USER jenkins  
ENV AGENT_WORKDIR=${AGENT_WORKDIR}  
RUN mkdir /home/jenkins/.jenkins && mkdir -p ${AGENT_WORKDIR}  
  
VOLUME /home/jenkins/.jenkins  
VOLUME ${AGENT_WORKDIR}  
WORKDIR /home/jenkins  
  
COPY jenkins-slave /usr/local/bin/jenkins-slave  
  
ENTRYPOINT ["jenkins-slave"]  

