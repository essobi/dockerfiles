FROM haproxy:alpine  
RUN apk add --no-cache --update tini  
COPY haproxy.cfg /etc/haproxy/haproxy.cfg  
COPY docker-entrypoint.sh /  
CMD ["haproxy", "-f", "/etc/haproxy/haproxy.cfg"]

