FROM alpine:3.4  
MAINTAINER ytnobody <ytnobody@gmail.com>  
  
RUN apk update && apk add gcc g++ make git patch perl perl-dev curl wget ca-
certificates && update-ca-certificates && rm -fr /var/cache/apk/*  
  
RUN curl -sL https://git.io/cpm > /usr/bin/cpm && chmod +x /usr/bin/cpm  
  
WORKDIR /usr  
RUN cpm install Plack  
  
ENV PERL5LIB=/usr/local/lib/perl5  
ENV PATH=/usr/local/bin:$PATH  
  
WORKDIR /  

