FROM alpine:3.7  
EXPOSE 3128 3129 3130  
RUN apk add --no-cache squid openssl su-exec gettext iptables ip6tables
iproute2 && rm -rf /var/cache/apk/*  
  
ENV DNS_SERVERS="8.8.8.8 8.8.4.4"  
VOLUME /var/cache/squid  
# Redirect logs to stdout for the container  
#RUN ln -sf /dev/stdout /var/log/squid/access.log \  
# && ln -sf /dev/stdout /var/log/squid/store.log \  
# && ln -sf /dev/stdout /var/log/squid/cache.log  
# && chown squid:squid /var/log/squid/*  
COPY docker-entrypoint.sh /  
COPY log_helper.sh /  
COPY store_id_helper.sh /  
COPY squid.conf /etc/squid/squid.conf.template  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  
CMD [ "squid" ]

