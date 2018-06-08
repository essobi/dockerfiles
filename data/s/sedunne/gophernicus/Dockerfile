FROM alpine:latest  
MAINTAINER Stephen Dunne III <sedunne@icanhazmail.net>  
ENV vers 2.1  
  
## dat image size tho  
RUN apk --no-cache --update add -t build-deps build-base gcc abuild binutils
make && \  
cd /tmp && curl -sL
http://gophernicus.org/software/gophernicus/gophernicus-${vers}.tar.gz |tar
-zx && \  
cd gophernicus-${vers}/ && make && mv /tmp/gophernicus-${vers}/in.gophernicus
/sbin/in.gophernicus && \  
mkdir -p /var/gopher/ && cp /tmp/gophernicus-${vers}/gophermap
/var/gopher/gophermap && \  
rm -rf /tmp/gophernicus-${vers} && apk del build-deps  
  
EXPOSE 70  
CMD nc -lk -p 70 -e /sbin/in.gophernicus -h $(hostname) -p 70 -nr -r
/var/gopher/  

