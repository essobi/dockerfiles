FROM haproxy:alpine  
  
LABEL maintainer "Ian Li <OpenSource@ianli.xyz>"  
  
RUN apk add --no-cache bash curl && \  
curl -O https://raw.githubusercontent.com/tests-always-included/mo/master/mo
&& \  
mv mo /usr/local/bin && \  
chmod +x /usr/local/bin/mo && \  
curl -L -O https://github.com/techotaku/docker-
files/raw/master/haproxy/entrypoint.sh && \  
chmod +x entrypoint.sh && \  
mv entrypoint.sh /usr/local/bin/entrypoint.sh && \  
rm /docker-entrypoint.sh  
  
ENTRYPOINT ["entrypoint.sh"]  
  
CMD ["-W", "-db", "-f", "/usr/local/etc/haproxy/haproxy.cfg"]

