FROM redis:3.2  
RUN set -x \  
&& mkdir -p /usr/local/etc/redis \  
&& touch /usr/local/etc/redis/redis.conf \  
&& chown redis:redis /usr/local/etc/redis/redis.conf  
  
ENV REDIS_PASS **None**  
  
# Backup script  
COPY backup.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/backup.sh  
  
# Entrypoint script  
# Entrypoint directive is specified in inherited image  
COPY docker-entrypoint.sh /usr/local/bin/  
  
# Healthcheck  
COPY healthcheck.sh /usr/local/bin/  
HEALTHCHECK \--timeout=5s CMD bash /usr/local/bin/healthcheck.sh  
  
# Expose redis data folder (/data) and backup folder (/snapshots)  
VOLUME ["/data", "/snapshots"]  
  
# Default start  
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]  

