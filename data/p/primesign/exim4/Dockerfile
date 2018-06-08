FROM alpine:3.4  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
RUN apk add --update \  
exim \  
&& \  
rm -f /var/cache/apk/*  
  
RUN mkdir /usr/lib/exim/ /var/log/exim  
  
VOLUME ["/var/log/exim"]  
  
ENTRYPOINT ["exim"]  
CMD ["-bdf", "-v", "-q30m"]  

