FROM alpine:3.2  
MAINTAINER Christian Blades <christian.blades@careerbuilder.com>  
  
RUN apk -U add ca-certificates nodejs python build-base && npm install -g
log.io@0.3.4 --user root && rm -r /var/cache/apk/* && \  
apk del sqlite-libs python binutils libgomp pkgconf pkgconfig \  
gmp mpfr3 mpc1 gcc make patch musl-dbg musl-dev libc-dev fortify-headers g++
build-base  
ADD web_server.conf /root/.log.io/web_server.conf  
  
EXPOSE 28777 28778  
CMD ["log.io-server"]  

