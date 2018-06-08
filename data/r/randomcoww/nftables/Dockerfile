FROM alpine:edge  
  
RUN set -x \  
\  
&& apk add --no-cache nftables  
  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  

