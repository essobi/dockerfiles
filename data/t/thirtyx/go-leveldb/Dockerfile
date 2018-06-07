FROM golang:1.7.1-alpine  
  
# We need both "testing" and "community" repositories here.  
RUN \  
echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& echo "@community http://nl.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
&& apk add --no-cache \  
git gcc musl-dev leveldb@testing leveldb-dev@testing glide@community  

