FROM alpine:edge  
  
RUN set -x \  
\  
&& apk add --no-cache \  
openvpn \  
bash \  
shadow  
  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  

