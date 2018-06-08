FROM alpine:3.3  
MAINTAINER Florian Maier <contact@marsmenschen.com>  
  
ENV GIT_URL git://github.com/marsmensch/vanitygen.git  
ENV REFRESHED_AT 2016-05-09  
ENV DPROJECT vanitygen  
  
# install dependencies  
RUN apk add --update --no-cache git libqrencode openssl-dev bash pcre-dev
gegl-dev build-base  
  
# create code directory  
RUN mkdir -p /opt/code/; cd /opt/code; git clone ${GIT_URL} ${DPROJECT} && \  
cd ${DPROJECT} && make && make install && rm -rf /opt/code/  
  
# no parameters display help  
ENTRYPOINT ["/usr/local/bin/vanitygen"]  
CMD ["--help"]

