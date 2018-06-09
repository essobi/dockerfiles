FROM jbanetwork/tinydns  
  
RUN apk add --no-cache tinydns drill  
  
ENV ROOT="/opt/tinydns/" IP="0.0.0.0" UID="0" GID="0"  
EXPOSE 53  
WORKDIR /opt/tinydns  
  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
  
CMD ["tinydns"]  

