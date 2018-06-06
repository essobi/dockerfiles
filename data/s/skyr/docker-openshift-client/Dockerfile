FROM ebits/openshift-client:v1.4.1  
MAINTAINER "Tom Pluess <tom@skyr.ch>"  
RUN apk update && \  
apk add --no-cache \  
bash \  
git \  
curl \  
ca-certificates \  
openssl  
  
ENV DOCKER_BUCKET get.docker.com  
ENV DOCKER_VERSION 17.03.1-ce  
ENV DOCKER_SHA256
820d13b5699b5df63f7032c8517a5f118a44e2be548dd03271a86656a544af55  
  
RUN set -x \  
&& mkdir -p /tmp/docker \  
&& curl -fSL
"https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz" -o
/tmp/docker/docker.tgz \  
&& sha256sum /tmp/docker/docker.tgz | grep $DOCKER_SHA256 \  
&& tar -xzvf /tmp/docker/docker.tgz -C /tmp/docker/ \  
&& mv /tmp/docker/docker/* /usr/local/bin/ \  
&& rm -rf /tmp/docker \  
&& docker -v  
  
ADD run-self-test.sh /opt/run-self-test.sh  

