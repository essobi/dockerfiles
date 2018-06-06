FROM yandex/clickhouse-server  
  
RUN sed -i
's,<listen_host>::</listen_host>,<listen_host>0.0.0.0</listen_host>,'
/etc/clickhouse-server/config.xml  
RUN sed -i 's,<listen_host>::1</listen_host>,,' /etc/clickhouse-
server/config.xml  
  
ENTRYPOINT exec /usr/bin/clickhouse-server --config=${CLICKHOUSE_CONFIG}  
  

