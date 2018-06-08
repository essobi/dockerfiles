FROM shurshun/alpine-moscow  
  
LABEL maintainer "4lifenet@gmail.com"  
  
LABEL SERVICE_NAME="pdns-recursor"  
  
# HEALTHCHECK --interval=1m --timeout=2s \  
# CMD curl -f http://localhost/nginx_status || exit 1  
RUN set -ex \  
&& apk add --no-cache pdns-recursor  
  
EXPOSE 53/udp  
  
ENTRYPOINT ["/usr/sbin/pdns_recursor", "--daemon=no", "--config-dir=/conf.d",
"--allow-from=0.0.0.0/0", "--local-address=0.0.0.0"]

