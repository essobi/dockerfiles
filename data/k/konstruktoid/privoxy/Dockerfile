FROM konstruktoid/alpine  
  
RUN apk update && \  
apk upgrade && \  
apk --update add privoxy && \  
rm -rf /var/cache/apk/  
  
COPY files/* /etc/privoxy/  
  
RUN chown -R privoxy:privoxy /etc/privoxy  
  
EXPOSE 8118  
ENTRYPOINT ["/usr/sbin/privoxy"]  
CMD [""]  

