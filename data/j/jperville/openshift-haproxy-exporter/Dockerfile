FROM prom/haproxy-exporter:v0.8.0  
ENTRYPOINT ["/bin/sh", "-c", "exec /bin/haproxy_exporter --haproxy.scrape-uri
\"http://${STATS_USERNAME}:${STATS_PASSWORD}@localhost:${STATS_PORT}/;csv\"" ]  

