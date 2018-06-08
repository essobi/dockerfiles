FROM alpine:3.4  
MAINTAINER HAFEN.IO <hello@hafen.io>  
  
ENV version=1.3.0~1383~g4f4e5ac~snapshot  
  
RUN apk add --update wget tar ca-certificates && rm -rf /var/cache/apk/*  
RUN wget http://mumble.info/snapshot/murmur-static_x86-${version}.tar.bz2  
RUN tar -xvf murmur-static_x86-${version}.tar.bz2 && \  
mv murmur-static_x86-${version} /app && \  
rm murmur-static_x86-${version}.tar.bz2  
  
ADD ./murmur.ini /app/murmur.ini  
  
EXPOSE 64738/tcp 64738/udp  
  
ENTRYPOINT ["/app/murmur.x86", "-fg", "-v"]  
CMD ["-ini", "/app/murmur.ini"]  

