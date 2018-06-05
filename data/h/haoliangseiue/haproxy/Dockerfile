FROM haproxy:1-alpine  
  
RUN apk add --no-cache tini  
  
RUN apk add --no-cache tzdata \  
&& ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
COPY ./another-entrypoint.sh /another-entrypoint.sh  
  
# https://github.com/dockerfile/haproxy/issues/3#issuecomment-349480504  
ENTRYPOINT ["tini"]  
  
CMD ["--", "/another-entrypoint.sh", "haproxy", "-f",
"/usr/local/etc/haproxy/haproxy.cfg"]  

