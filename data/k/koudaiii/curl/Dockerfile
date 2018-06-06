FROM alpine:3.4  
ENV TIMEZONE Asia/Tokyo  
  
RUN apk --no-cache --update add tzdata \  
&& cp /usr/share/zoneinfo/$TIMEZONE /etc/localtime \  
&& apk del tzdata  
  
RUN apk add --no-cache --update --virtual=deps1 curl bash postgresql-client
tcpdump redis jq bind-tools libmemcached-libs memcached perl \  
&& curl
https://raw.githubusercontent.com/memcached/memcached/master/scripts/memcached-
tool -o /usr/local/bin/memcached-tool \  
&& chmod +x /usr/local/bin/memcached-tool  
  
CMD ["/usr/bin/curl"]  

