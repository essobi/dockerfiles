FROM alpine:3.3  
ENV COMMAND=build \  
REGISTRY_HOST="docker.io" \  
REGISTRY_USERNAME="qwerty" \  
REGISTRY_PASSWORD="qwerty" \  
IMAGE="namespace/image" \  
TAG="latest"  
RUN apk add --update curl && \  
curl -o docker.tgz
https://get.docker.com/builds/Linux/x86_64/docker-1.11.0.tgz && \  
tar -xzvf docker.tgz && \  
mv docker/docker /usr/local/bin/docker && \  
apk del --purge curl && \  
rm -rf /var/cache/apk/*  
  
COPY ./ /  
  
CMD ["/bin/sh", "/entry.sh"]  

