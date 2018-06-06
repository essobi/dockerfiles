FROM alpine:3.6 as builder  
ARG MAJOR_VERSION=0.9  
ARG MINOR_VERSION=1  
RUN apk add --no-cache gcc g++ mysql-dev ca-certificates openssl wget glib-dev
cmake && \  
mkdir -p /usr/src/mydumper  
WORKDIR /usr/src/  
RUN apk add --no-cache make  
RUN wget
https://launchpad.net/mydumper/${MAJOR_VERSION}/${MAJOR_VERSION}.${MINOR_VERSION}/+download/mydumper-${MAJOR_VERSION}.${MINOR_VERSION}.tar.gz
&& \  
tar xzvf mydumper-${MAJOR_VERSION}.${MINOR_VERSION}.tar.gz -C
/usr/src/mydumper --strip-components 1 && \  
rm mydumper-${MAJOR_VERSION}.${MINOR_VERSION}.tar.gz  
RUN cd mydumper && \  
cmake -DCMAKE_INSTALL_PREFIX=/usr && \  
make -j  
  
FROM alpine:3.6  
RUN apk add --no-cache mariadb-client-libs glib bash  
COPY \--from=builder /usr/src/mydumper/mydumper /usr/bin/  
COPY \--from=builder /usr/src/mydumper/myloader /usr/bin/  
COPY docker-entrypoint.sh /entrypoint  
ENTRYPOINT ["bash","-x","/entrypoint"]  

