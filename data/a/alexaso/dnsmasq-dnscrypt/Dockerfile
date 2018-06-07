FROM alpine:latest as builder  
WORKDIR /dnscrypt-proxy  
RUN apk update && apk add wget ca-certificates libsodium-dev ldns-dev make gcc
g++ build-base  
RUN wget https://download.dnscrypt.org/dnscrypt-proxy/LATEST.tar.gz  
RUN tar xzvf LATEST.tar.gz  
RUN mv dnscrypt* dnscrypt-latest  
WORKDIR /dnscrypt-proxy/dnscrypt-latest/  
RUN ./configure && make  
RUN make install  
  
FROM alpine:latest  
RUN apk --no-cache add dnsmasq libsodium ldns  
COPY \--from=builder /usr/local/sbin/dnscrypt-proxy /usr/sbin/  
COPY dnsmasq.conf /etc/dnsmasq.conf  
COPY entrypoint.sh /entrypoint.sh  
COPY dnscrypt-resolvers.csv /usr/local/share/dnscrypt-proxy/dnscrypt-
resolvers.csv  
RUN chmod +x /entrypoint.sh  
ENV RESOLVER=cisco  
ENTRYPOINT ["/entrypoint.sh"]  

