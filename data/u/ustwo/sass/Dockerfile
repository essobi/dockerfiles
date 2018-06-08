FROM alpine:3.3  
MAINTAINER Arnau Siches <arnau@ustwo.com>  
  
ENV SASSC_VERSION=3.3.6 \  
LIBSASS_VERSION=3.3.6 \  
SASS_LIBSASS_PATH=/usr/local/libsass-$LIBSASS_VERSION  
  
COPY build.sh /build.sh  
RUN /build.sh  
  
RUN adduser -D ustwo \  
&& addgroup ustwo ustwo  
  
WORKDIR /home/ustwo  
  
ENTRYPOINT ["/usr/local/bin/sassc"]  
CMD ["-v"]  

