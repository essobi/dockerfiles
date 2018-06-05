FROM supersoftware/bop:base  
MAINTAINER yamazawa@supersoftware.co.jp  
  
ADD ./wrapdocker /usr/local/bin/wrapdocker  
  
RUN apk --update add \  
bash iptables ca-certificates e2fsprogs docker && \  
rm -rf /var/cache/apk/*  
  
VOLUME /var/lib/docker  
  
RUN chmod +x /usr/local/bin/wrapdocker && wrapdocker  
  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  

