FROM comptel/docker-alpine-base:v36.1  
ARG LIBRESSL_VERSION=2.7  
ARG LIBRDKAFKA_VERSION=0.11.4-r1  
  
RUN apk add libressl${LIBRESSL_VERSION}-libcrypto
libressl${LIBRESSL_VERSION}-libssl --update-cache --repository
http://nl.alpinelinux.org/alpine/edge/main && \  
apk add librdkafka=${LIBRDKAFKA_VERSION} \--update-cache --repository
http://nl.alpinelinux.org/alpine/edge/community  

