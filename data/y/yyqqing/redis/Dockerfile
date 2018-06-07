FROM redis:alpine  
  
MAINTAINER yyqqing <y_yqing@163.com>  
  
# RUN echo never > /sys/kernel/mm/transparent_hugepage/enabled  
# RUN_MODE = master / slave / sentinel  
ENV RUN_MODE=master \  
MASTER_NAME='master1' \  
MASTER_HOST='' \  
MASTER_PORT=6379 \  
MASTER_PASSWORD='' \  
PASSWORD='' \  
SENTINEL_MASTER_QUORUM=1 \  
SENTINEL_DOWN_AFTER_MS=30000 \  
SENTINEL_PARALLEL_SYNCS=1 \  
SENTINEL_FAILOVER_TIMEOUT=180000  
  
EXPOSE 26379  
  
COPY docker-entrypoint.sh /usr/local/bin/

