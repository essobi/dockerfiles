FROM alpine  
MAINTAINER Steve Vega "steve.vega@hulilabs.com"  
COPY build.sh /tmp/build.sh  
RUN /tmp/build.sh  
  
VOLUME /input  
VOLUME /output  
VOLUME /images  
  
WORKDIR /input  
  
COPY config.rb /input/config.rb  
  
ENTRYPOINT [ "compass" ]  

