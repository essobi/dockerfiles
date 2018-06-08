FROM golang:1.8-alpine  
  
# Adding edge repo so we can add glide  
RUN echo "@edge http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories && apk update  
RUN apk add --no-cache glide@edge git g++ make  

