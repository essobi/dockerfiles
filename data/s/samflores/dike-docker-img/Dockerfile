FROM openjdk:jre-alpine  
  
RUN apk update && apk add ca-certificates bash curl  
RUN curl -fsSLo /usr/local/bin/boot https://github.com/boot-clj/boot-
bin/releases/download/latest/boot.sh  
RUN chmod a+x /usr/local/bin/boot  
  
COPY build.boot /root  
  
RUN cd /root && \  
mkdir src resources && \  
BOOT_VERSION=2.6.0 BOOT_AS_ROOT=yes BOOT_CLOJURE_VERSION=1.9.0-alpha12 boot
show -u  

