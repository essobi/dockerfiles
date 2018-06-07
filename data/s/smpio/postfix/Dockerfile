FROM alpine  
  
RUN apk add -U postfix socat bash \  
&& rm -rf /var/cache/apk/*  
  
COPY entrypoint.sh /  
  
EXPOSE 25 465 587  
VOLUME /var/spool/postfix  
  
ENTRYPOINT ["/entrypoint.sh"]  

