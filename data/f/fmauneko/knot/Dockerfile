FROM alpine:edge  
  
EXPOSE 53/tcp 53/udp  
  
VOLUME /etc/knot/conf.d /var/lib/knot  
  
RUN set -ex \  
&& apk add --no-cache knot tini \  
&& mkdir -p /run/knot/ \  
&& chmod -R 0750 /run/knot/ \  
&& chown -R knot:knot /run/knot/  
  
COPY knot.conf /etc/knot/knot.conf  
COPY docker-entrypoint.sh /usr/local/bin/run  
  
ENTRYPOINT ["/sbin/tini", "--", "/usr/local/bin/run"]  
CMD ["/usr/sbin/knotd", "-c", "/etc/knot/knot.conf"]  

