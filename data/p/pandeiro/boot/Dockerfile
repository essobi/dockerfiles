FROM java:openjdk-8u111-jre-alpine  
MAINTAINER Murphy McMahon <pandeiro.docker@gmail.com>  
  
# Get Boot  
RUN apk --update upgrade && \  
apk add bash curl ca-certificates && \  
update-ca-certificates && \  
rm -rf /var/cache/apk/*  
  
RUN curl -L -o /usr/bin/boot \  
https://github.com/boot-clj/boot-bin/releases/download/latest/boot.sh \  
&& chmod +x /usr/bin/boot  
  
# Config Boot to run as root and use maven cache  
ENV BOOT_AS_ROOT yes  
ENV BOOT_LOCAL_REPO /m2  
ENV BOOT_HOME /.boot  
ENV BOOT_VERSION 2.7.1  
ENV BOOT_EMIT_TARGET no  
  
# Run `boot` a first time and cache everything in /m2  
RUN mkdir /m2  
RUN boot -vv && boot repl --server  
  
# Mount applications in /app  
RUN mkdir /app  
WORKDIR /app  
  
ENTRYPOINT ["boot"]  
  
#  
# Usage:  
#  
# docker run -v $(pwd):/app -v ~/.m2/repository:/m2 -v ~/.boot:/.boot
pandeiro/boot run  
#  

