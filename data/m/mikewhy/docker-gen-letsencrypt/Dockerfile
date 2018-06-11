FROM alpine  
  
ENV DOCKER_GEN_VERSION=0.7.0  
RUN apk add --update bash curl \  
&& curl -L \  
https://github.com/jwilder/docker-
gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz \  
| tar -xzv -C /usr/local/bin \  
&& apk add gcc git py-pip py-setuptools python libffi-dev musl-dev openssl
openssl-dev python-dev \  
&& pip install git+git://github.com/zenhack/simp_le.git \  
&& apk del gcc git py-pip libffi-dev musl-dev openssl-dev python-dev  
  
ENV DEBUG=false  
ENV DOCKER_HOST=unix:///var/run/docker.sock  
  
VOLUME /output  
  
COPY ./app /app  
WORKDIR /app  
  
ENTRYPOINT ["/app/entrypoint"]  

