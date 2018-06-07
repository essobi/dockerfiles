FROM alpine:latest  
  
RUN apk update && apk upgrade && \  
apk add --no-cache git make automake autoconf gcc libc-dev ncurses-dev && \  
d=`mktemp -d` && \  
git clone https://github.com/emugel/mtr-geoip "$d" && \  
cd "$d" && \  
git checkout newdns && \  
./bootstrap.sh && \  
./configure --without-gtk && \  
make && \  
make install  
  
ENTRYPOINT ["mtr"]  

