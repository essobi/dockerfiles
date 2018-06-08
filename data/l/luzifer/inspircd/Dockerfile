FROM debian:jessie  
  
MAINTAINER Knut Ahlers <knut@ahlers.me>  
  
ADD https://github.com/inspircd/inspircd/archive/v2.0.18.tar.gz /src/  
  
RUN apt-get update && \  
apt-get install -y build-essential libssl-dev libssl1.0.0 openssl pkg-config
&& \  
useradd -u 10000 -d /inspircd/ inspircd && \  
cd /src && \  
tar -xzf *.tar.gz && \  
ln -sf inspircd-* inspircd && \  
cd /src/inspircd && \  
./configure --disable-interactive --prefix=/inspircd/ --uid 10000 --enable-
openssl && \  
make && make install && \  
apt-get purge -y build-essential  
  
VOLUME ["/inspircd/conf"]  
  
EXPOSE 6667 6697  
ENTRYPOINT ["/inspircd/bin/inspircd"]  
CMD ["--runasroot", "--nofork"]  

