FROM openjdk:8-jdk-alpine AS builder  
LABEL maintainer "amaya <mail@sapphire.in.net>"  
  
RUN apk --no-cache add gc-dev clang musl-dev libc-dev build-base git  
RUN apk add libunwind-dev -U -X http://nl.alpinelinux.org/alpine/edge/main  
RUN git clone \--depth=1 -b 2018-03-01 https://github.com/google/re2.git && \  
cd re2 && \  
CXX=clang++ make && \  
make install  
  
ENV SBT_VERSION="1.1.0"  
ENV SBT_HOME="/usr/local/sbt"  
ENV PATH="${PATH}:${SBT_HOME}/bin"  
RUN mkdir -p ${SBT_HOME} && \  
apk add --no-cache bash wget bc && \  
wget
"https://github.com/sbt/sbt/releases/download/v${SBT_VERSION}/sbt-${SBT_VERSION}.tgz"
-O - \  
| tar xz -C ${SBT_HOME} \--strip-components=1 && \  
sbt about  
  
FROM alpine:3.7  
LABEL maintainer "amaya <mail@sapphire.in.net>"  
  
RUN apk add --no-cache libatomic_ops  
  
COPY \--from=builder \  
/usr/lib/libunwind.so.8 \  
/usr/lib/libunwind-x86_64.so.8 \  
/usr/lib/libgc.so.1 \  
/usr/lib/libstdc++.so.6 \  
/usr/lib/libgcc_s.so.1 \  
/usr/lib/  
COPY \--from=builder \  
/usr/local/lib/libre2.so.0 \  
/usr/local/lib/  
  

