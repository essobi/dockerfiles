FROM maven:3.5.3-jdk-8-alpine  
  
LABEL maintainer="Piotr Joński <p.jonski@pojo.pl>"  
  
ENV M3_HOME=${MAVEN_HOME}  
ENV HELM_VERSION=v2.8.2  
## install helm, kubectl  
RUN apk add --update ca-certificates openssl curl bash git openssh libintl
gettext \  
&& curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl
-s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl \  
&& mv kubectl /usr/local/bin \  
&& chmod +x /usr/local/bin/kubectl \  
&& curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get >
get_helm.sh \  
&& chmod 700 get_helm.sh \  
&& ./get_helm.sh --version $HELM_VERSION \  
&& helm init --client-only \  
&& helm version --client \  
&& apk add --virtual build_deps \  
&& cp /usr/bin/envsubst /usr/local/bin/envsubst \  
&& rm -rf get_helm.sh  
  
## install grails  
ENV GRAILS_VERSION=2.5.6  
  
RUN wget https://github.com/grails/grails-
core/releases/download/v$GRAILS_VERSION/grails-$GRAILS_VERSION.zip \  
&& unzip grails-$GRAILS_VERSION.zip \  
&& rm -rf grails-$GRAILS_VERSION.zip \  
&& mv grails-$GRAILS_VERSION /usr/lib/jvm/grails  
  
RUN ls -al /usr/lib/jvm/grails  
  
ENV GRAILS_HOME /usr/lib/jvm/grails  
ENV PATH $GRAILS_HOME/bin:$PATH  
  
## install docker https://github.com/docker-
library/docker/blob/master/18.05/Dockerfile  
# set up nsswitch.conf for Go's "netgo" implementation (which Docker
explicitly uses)  
# - https://github.com/docker/docker-
ce/blob/v17.09.0-ce/components/engine/hack/make.sh#L149  
# - https://github.com/golang/go/blob/go1.9.1/src/net/conf.go#L194-L275  
# - docker run --rm debian:stretch grep '^hosts:' /etc/nsswitch.conf  
RUN [ ! -e /etc/nsswitch.conf ] && echo 'hosts: files dns' >
/etc/nsswitch.conf  
  
ENV DOCKER_CHANNEL edge  
ENV DOCKER_VERSION 18.05.0-ce  
  
RUN set -ex; \  
apk add --no-cache --virtual .fetch-deps \  
curl \  
tar \  
; \  
\  
# this "case" statement is generated via "update.sh"  
apkArch="$(apk --print-arch)"; \  
case "$apkArch" in \  
x86_64) dockerArch='x86_64' ;; \  
armhf) dockerArch='armel' ;; \  
aarch64) dockerArch='aarch64' ;; \  
ppc64le) dockerArch='ppc64le' ;; \  
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
  
## cleanup  
RUN rm /var/cache/apk/* \  
&& rm -rf /tmp/* \  
&& rm -rf /var/lib/apt/lists/* \  
&& apk del build_deps  
  
COPY config /root/.kube/config  
  
CMD bash

