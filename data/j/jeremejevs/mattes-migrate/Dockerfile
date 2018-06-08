FROM frolvlad/alpine-glibc  
  
ENV VERSION 3.0.1  
RUN \  
set -xe; \  
apk add --no-cache openssl ca-certificates; \  
wget
https://github.com/mattes/migrate/releases/download/v$VERSION/migrate.linux-
amd64.tar.gz; \  
tar xzf migrate.linux-amd64.tar.gz  
  
FROM frolvlad/alpine-glibc  
  
COPY \--from=0 migrate.linux-amd64 /usr/local/bin/migrate  
WORKDIR /migrations  
ENTRYPOINT ["migrate"]  

