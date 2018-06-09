FROM haproxy:1.8-alpine  
  
RUN set -ex \  
&& apk add --no-cache tini  
  
COPY run.sh /  
CMD ["/run.sh"]  
ENTRYPOINT ["/sbin/tini", "--"]  

