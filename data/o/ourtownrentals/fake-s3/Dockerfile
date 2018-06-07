FROM alpine:3.7  
MAINTAINER Evan Sosenko <razorx@evansosenko.com>  
  
RUN mkdir -p /srv  
RUN apk add --no-cache ruby  
  
ENV FAKES3_VERSION 1.2.1  
RUN gem install --no-document fakes3 -v ${FAKES3_VERSION}  
  
WORKDIR /srv  
  
VOLUME /srv  
EXPOSE 80  
ENTRYPOINT ["/usr/bin/fakes3", "-r", "/srv", "-p", "80"]  

