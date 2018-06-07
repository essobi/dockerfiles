FROM alpine:latest  
MAINTAINER Christopher Emerson <christopher.emerson@whiteoaksecurity.com>  
  
RUN apk add --update perl perl-net-dns git wget && rm -rf /var/cache/apk/*  
  
RUN git clone git://git.kali.org/packages/fierce.git  
  
RUN mkdir /output  
VOLUME ["/output"]  
WORKDIR /fierce  
  
ENTRYPOINT ["/usr/bin/perl", "fierce.pl"]  

