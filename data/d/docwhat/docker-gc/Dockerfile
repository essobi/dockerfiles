FROM busybox  
MAINTAINER Christian Höltje <docwhat@gerf.org>  
  
ENV DOCKER_GC_VERSION 1.0.7  
ENV COLUMNS 80  
ADD ["https://github.com/docwhat/docker-
gc/releases/download/${DOCKER_GC_VERSION}/docker-gc_linux_amd64", "/docker-
gc"]  
RUN ["chmod", "0755", "/docker-gc"]  
  
ENTRYPOINT ["/docker-gc"]  

