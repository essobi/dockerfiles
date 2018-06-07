FROM alpine  
RUN apk update ; \  
apk add git ;\  
apk add make go; \  
go version; \  
git clone https://github.com/vzex/dog-tunnel.git;\  
cd dog-tunnel;\  
git checkout origin/udpVersion -b udp;\  
make client;\  
cp dtunnel_lite /usr/bin;\  
apk info;\  
apk del run-parts openssl lua5.2-libs lua5.2 ncurses-terminfo ncurses-widec-
libs lua5.2-posix ca-certificates libssh2 curl expat pcre git go make;\  
apk cache clean;\  
rm -rf /usr/lib/go;\  
cd ..;\  
rm -rf dog-tunnel;  

