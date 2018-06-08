FROM alpine:3.6  
MAINTAINER Michele Adduci <info@micheleadduci.net>  
  
VOLUME ["/project"]  
WORKDIR ["/project"]  
  
RUN apk update && \  
apk upgrade && \  
apk --update add \  
gcc \  
g++ \  
build-base \  
cmake \  
bash \  
libstdc++ && \  
rm -rf /var/cache/apk/*  
  
ADD ./scripts/cmake-build.sh /build.sh  
  
RUN chmod +x /build.sh  
  
ENTRYPOINT exec /build.sh

