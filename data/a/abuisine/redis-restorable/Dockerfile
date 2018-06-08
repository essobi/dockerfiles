FROM redis:3.2.11-alpine  
LABEL maintainer="Alexandre Buisine <alexandrejabuisine@gmail.com>"
version="3.2.11"  
  
RUN sed -ie '/chown -R redis \./ i \  
AOF_FILE="/restore/appendonly.aof"; \  
if [ -f "$AOF_FILE" ]; then \  
echo; \  
echo "Restore requested, processing ..."; \  
mv $AOF_FILE /data/appendonly.aof.restore && mv /data/appendonly.aof.restore
/data/appendonly.aof && echo "Done" || echo "Failed"; \  
echo; \  
echo "Redis restore process done. Ready for start up."; \  
echo; \  
fi;' /usr/local/bin/docker-entrypoint.sh  
  
VOLUME /restore  
  
CMD ["redis-server", "--appendonly", "yes"]

