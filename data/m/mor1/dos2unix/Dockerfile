FROM alpine:latest  
MAINTAINER Richard Mortier <mort@cantab.net>  
  
RUN apk --no-cache add --update \  
\--repository http://dl-3.alpinelinux.org/alpine/edge/testing/ \  
dos2unix  
  
WORKDIR /cwd  
ENTRYPOINT ["dos2unix"]  

