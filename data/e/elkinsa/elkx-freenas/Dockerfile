FROM sebp/elkx  
LABEL org.freenas.interactive="false" \  
org.freenas.version="1.0.007" \  
org.freenas.upgradeable="true" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.autostart="true" \  
org.freenas.capabilities-add="NET_BROADCAST" \  
org.freenas.web-ui-protocol="http" \  
org.freenas.web-ui-port="5601" \  
org.freenas.port-
mappings="5601:5601/tcp,5000:5000/tcp,514:514/tcp,9200:9200/tcp,5001:5001/tcp,5002:5002/tcp,5002:5002/udp,514:514/udp"
\  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/var/lib/elasticsearch\", \  
\"descr\": \"ES data\" \  
}, \  
{ \  
\"name\": \"/opt/kibana/config\", \  
\"descr\": \"Kibana config data\" \  
}, \  
{ \  
\"name\": \"/etc/logstash/conf.d\", \  
\"descr\": \"logstash config\" \  
} \  
]" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"TZ\", \  
\"descr\": \"Timezone information, eg Europe/London. Default Etc/UTC\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"PGID\", \  
\"descr\": \"GroupID\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"PUID\", \  
\"descr\": \"UserID\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"ES_HEAP_SIZE\", \  
\"descr\": \"Elasticsearch heap size (default is 256MB min, 1G max)\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"ES_JAVA_OPTS\", \  
\"descr\": \"additional Java options for Elasticsearch\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"ES_CONNECT_RETRY\", \  
\"descr\": \"number of seconds to wait for Elasticsearch to be up before
starting Logstash and/or Kibana (default: 30)\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"CLUSTER_NAME\", \  
\"descr\": \"the name of the Elasticsearch cluster (default: automatically
resolved when the container starts if Elasticsearch requires no user
authentication)\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"LS_HEAP_SIZE\", \  
\"descr\": \"Logstash heap size (default: 500m)\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"LS_OPTS\", \  
\"descr\": \"Logstash options\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"NODE_OPTIONS\", \  
\"descr\": \"Node options for Kibana (default: --max-old-space-size=250)\", \  
\"optional\": true \  
} \  
]"  

