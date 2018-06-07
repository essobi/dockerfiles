FROM alpine:3.4  
CMD ["/usr/local/bin/hitch-start"]  
  
COPY ./bootstrap /usr/local/bin/hitch-start  
  
RUN apk --no-cache --update add autoconf automake bash build-base byacc curl
flex libev libev-dev openssl openssl-dev && \  
cd /tmp && \  
curl -L https://api.github.com/repos/varnish/hitch/tarball/hitch-1.4.4 | tar
xz && \  
cd varnish-hitch* && \  
./bootstrap && \  
./configure && \  
make && \  
make install && \  
adduser -h /var/lib/hitch -s /sbin/nologin -u 8379 -D hitch && \  
rm -rf /tmp/* && \  
apk del git build-base libev-dev automake autoconf openssl-dev flex byacc  
  
USER hitch  

