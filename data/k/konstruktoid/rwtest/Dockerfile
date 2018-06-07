FROM alpine:3.2  
ENV VERSION 1.10.2  
WORKDIR /usr/bin  
  
RUN apk update && \  
apk upgrade && \  
apk --update add bash coreutils curl openssl && \  
curl -sS https://get.docker.com/builds/Linux/x86_64/docker-$VERSION >
docker-$VERSION && \  
curl -sS https://get.docker.com/builds/Linux/x86_64/docker-$VERSION.sha256 >
docker-$VERSION.sha256 && \  
sha256sum -c docker-$VERSION.sha256 && \  
ln -s docker-$VERSION docker && \  
chmod u+x docker-$VERSION && \  
apk del curl && \  
rm -rf /var/cache/apk/*  
  
COPY ./rw-test.sh /rw-test.sh  
  
ENTRYPOINT ["/bin/bash", "/rw-test.sh"]  

