FROM alpine  
RUN apk add --no-cache varnish  
ENTRYPOINT ["/usr/sbin/varnishd", "-F"]  
CMD ["-f", "/etc/varnish/default.vcl", "-s", "malloc,64m", "-p",
"default_ttl=60", "-p", "default_grace=60"]  

