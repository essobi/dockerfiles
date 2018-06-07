FROM alpine:edge  
  
RUN set -x \  
\  
&& apk add --no-cache keepalived  
  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  

