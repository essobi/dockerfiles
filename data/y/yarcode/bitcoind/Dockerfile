FROM alpine:3.7  
MAINTAINER Alexey Samoylov <alexey.samoylov@gmail.com>  
  
ARG BITCOIN_VERSION=0.15.1-r1  
ARG BITCOIN_DATA=/var/lib/bitcoin  
  
# Setting up default environment variables  
ENV BITCOIN_DATA=${BITCOIN_DATA}  
  
RUN echo "@community http://dl-4.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories  
RUN apk add --update --no-cache bash bitcoin@community=${BITCOIN_VERSION}  
  
COPY docker-entrypoint.sh /usr/bin/  
RUN chmod +x /usr/bin/docker-entrypoint.sh  
  
ENTRYPOINT ["/usr/bin/docker-entrypoint.sh"]CMD ["bitcoind"]  

