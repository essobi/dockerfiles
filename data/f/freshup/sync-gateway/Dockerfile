FROM couchbase/sync-gateway:1.3.1-community  
  
RUN wget http://stedolan.github.io/jq/download/linux64/jq && \  
chmod +x ./jq && \  
cp jq /usr/bin  
  
COPY entrypoint.sh /tmp/entrypoint.sh  
RUN chmod +x /tmp/entrypoint.sh  
  
ENTRYPOINT ["/bin/bash", "/tmp/entrypoint.sh"]  

