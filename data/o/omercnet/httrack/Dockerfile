FROM alpine:edge  
  
RUN echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
RUN apk add --update httrack@testing && rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["httrack"]  

