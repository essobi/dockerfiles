FROM gliderlabs/alpine  
  
MAINTAINER packeteer <packeteer@gmail.com>  
  
RUN apk-install varnish  
  
ENV LDAPCONF /etc/openldap/slapd.conf  
  
EXPOSE 80  
ENTRYPOINT ["/usr/sbin/varnishd"]  
CMD ["-F", "-u", "varnish", "-f", "$VCL_CONFIG", "-s", "malloc",
"$CACHE_SIZE", "$VARNISHD_PARAMS"]  

