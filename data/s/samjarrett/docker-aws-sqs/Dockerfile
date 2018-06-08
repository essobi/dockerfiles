FROM python:alpine  
  
ENV DOCKER_VERSION 1.12.3  
RUN set -xe && \  
apk add --no-cache --virtual .build-deps curl tar && \  
apk add --no-cache jq && \  
curl -ksSL
https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz | tar
-C /usr/local/bin --strip-components=1 -zxvf - && \  
pip install awscli && \  
apk del --no-cache .build-deps && \  
true  
  
COPY run.sh /  
  
CMD /run.sh

