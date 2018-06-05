FROM alpine:3.7 AS build  
  
ENV BONNIE_VERSION=1.97.3 \  
STRESS_VERSION=1.0.4 \  
SHELL=/bin/bash  
  
WORKDIR /tmp  
  
# Dependencies  
RUN \  
apk add --no-cache bash g++ make perl wget openssl  
  
# Bonnie++  
RUN \  
wget https://www.coker.com.au/bonnie++/bonnie++-${BONNIE_VERSION}.tgz && \  
tar xvf bonnie++-${BONNIE_VERSION}.tgz && cd bonnie++-${BONNIE_VERSION}/ && \  
mkdir -p bonnie &&\  
./configure --prefix=/tmp/bonnie && make && make install  
  
# Stress  
RUN \  
wget
https://people.seas.harvard.edu/~apw/stress/stress-${STRESS_VERSION}.tar.gz &&
\  
tar xvf stress-${STRESS_VERSION}.tar.gz && cd stress-${STRESS_VERSION} && \  
mkdir -p stress &&\  
./configure --prefix=/tmp/stress && make && make install  
  
#---  
FROM alpine:3.7  
WORKDIR /usr/local  
  
RUN \  
apk add --no-cache g++  
  
COPY \--from=build /tmp/bonnie/bin/* /usr/local/bin/  
COPY \--from=build /tmp/bonnie/sbin/* /usr/local/sbin/  
COPY \--from=build /tmp/stress/bin/* /usr/local/bin/  
  
#CMD ["/app/listener"]  
ARG BUILD_DATE  
ARG BUILD_VCS_REF  
ARG BUILD_VERSION  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="https://github.com/mgvazquez/docker-stress.git" \  
org.label-schema.vcs-ref=$BUILD_VCS_REF \  
org.label-schema.version=$BUILD_VERSION \  
com.microscaling.license=MIT

