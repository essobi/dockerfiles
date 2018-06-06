FROM alpine:latest  
  
ENV DEBUG=false \  
DOCKER_GEN_VERSION=0.7.4 \  
DOCKER_HOST=unix:///var/run/docker.sock  
  
# Install packages required by the image  
RUN apk add --update \  
ca-certificates \  
bash \  
curl && \  
mkdir -p /usr/local/share/ca-certificates/ && \  
rm /var/cache/apk/* && \  
mkdir /app  
  
# Install docker-gen  
RUN curl -L https://github.com/jwilder/docker-
gen/releases/download/${DOCKER_GEN_VERSION}/docker-gen-linux-
amd64-${DOCKER_GEN_VERSION}.tar.gz \  
| tar -C /usr/local/bin -xz  
  
ADD entrypoint.sh /app/entrypoint.sh  
ADD pdns.tmpl /app/pdns.tmpl  
ADD pdns.sh /app/pdns.sh  
  
WORKDIR /app  
  
ENTRYPOINT [ "/app/entrypoint.sh" ]  
  

