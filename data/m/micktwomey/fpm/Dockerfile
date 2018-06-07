FROM ubuntu:16.04  
ARG FPM_VERSION=1.8.0  
ARG DUMB_INIT_VERSION=1.2.0  
COPY scripts/docker-build.sh /tmp/docker-build.sh  
RUN /bin/bash -ex /tmp/docker-build.sh $VERSION  
  
VOLUME /src  
WORKDIR /src  
ENTRYPOINT ["dumb-init", "/usr/local/bin/fpm"]  
CMD ["--help"]  

