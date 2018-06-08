FROM alpine:edge  
  
ENV ROOT_HINTS_URL https://www.internic.net/domain/named.cache  
  
RUN set -x \  
\  
&& apk add --no-cache \  
unbound \  
\  
&& mkdir -p /etc/unbound/unbound.conf.d  
  
ADD $ROOT_HINTS_URL /etc/unbound/root.hints  
COPY unbound.conf /etc/unbound/unbound.conf  
  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  

