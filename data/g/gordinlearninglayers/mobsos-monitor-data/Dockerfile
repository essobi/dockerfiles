FROM learninglayers/base  
  
# add files to data volume  
ADD etc /opt/mobsos-monitor/etc  
  
# in MobSOS Monitor config replace API URI (environment variable
$LAYERS_API_URI), database user and generated password (environment variables
$MM_DB_USER and $MM_DB_PASS), and a valid key for the used IPInfoDB API
(environment variable $IPINFODB_KEY).  
CMD sed -i "s#LAYERS_API_URI#${LAYERS_API_URI}#g" /opt/mobsos-
monitor/etc/conf.properties && \  
sed -i "s#PASSWORD#${MM_DB_PASS}#g" /opt/mobsos-monitor/etc/conf.properties &&
\  
sed -i "s#USER#${MM_DB_USER}#g" /opt/mobsos-monitor/etc/conf.properties && \  
sed -i "s#DATABASE#${MM_DB_NAME}#g" /opt/mobsos-monitor/etc/conf.properties &&
\  
sed -i "s#IPINFODB_KEY#${IPINFODB_KEY}#g" /opt/mobsos-
monitor/etc/conf.properties && \  
sed -i "s#MM_DB_PASS#${MM_DB_PASS}#g" /opt/mobsos-monitor/etc/sql/schema.sql
&& \  
sed -i "s#MM_DB_USER#${MM_DB_USER}#g" /opt/mobsos-monitor/etc/sql/schema.sql
&& \  
sed -i "s#MM_DB_NAME#${MM_DB_NAME}#g" /opt/mobsos-monitor/etc/sql/schema.sql
&& \  
sed -i "s#OIDC_DB_NAME#${OIDC_DB_NAME}#g" /opt/mobsos-
monitor/etc/sql/schema.sql  
  
# provide directories etc and log as volumes  
VOLUME ["/opt/mobsos-monitor/etc/","/opt/mobsos-monitor/log"]  

