FROM debian:jessie  
  
RUN echo "deb http://cdn.debian.or.jp/debian jessie main" >
/etc/apt/sources.list && \  
echo "deb http://cdn.debian.or.jp/debian jessie-updates main" >>
/etc/apt/sources.list &&\  
echo "deb http://security.debian.org/ jessie/updates main" >>
/etc/apt/sources.list  
  
RUN apt-get update && \  
apt-get install -y less vim curl ca-certificates --no-install-recommends && \  
rm -rf /var/lib/apt/lists/*  
  

