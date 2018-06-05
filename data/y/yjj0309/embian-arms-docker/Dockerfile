FROM dockerfile/java:oracle-java7  
MAINTAINER Kyoungmo yang <mo@embian.com>  
  
# Define Evn  
ENV DEBIAN_FRONTEND noninteractive  
ENV ES_VERSION 1.4.1  
ENV INFLUXDB_VERSION 0.8.6  
ENV DEFAULT_USER arms  
ENV DEFAULT_PASS arms  
ENV HOST_NAME localhost  
  
##############################################  
# 1. Install required package  
##############################################  
# Install curl, wget, supervisor  
RUN apt-get update && apt-get install -y curl wget supervisor && rm -rf
/var/lib/apt/lists/*  
  
##############################################  
# 2. Install memcached  
##############################################  
RUN apt-get update && apt-get -y install memcached && rm -rf
/var/lib/apt/lists/*  
  
##############################################  
# 3. Install ElasticSearch.  
##############################################  
RUN \  
cd /opt && \  
wget
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-${ES_VERSION}.tar.gz
&& \  
tar xvzf elasticsearch-${ES_VERSION}.tar.gz && \  
rm -f elasticsearch-${ES_VERSION}.tar.gz && \  
ln -s /opt/elasticsearch-${ES_VERSION} /opt/elasticsearch  
  
# Install head plugin  
RUN /opt/elasticsearch/bin/plugin --install mobz/elasticsearch-head  
# Install bigdesk plugin  
RUN /opt/elasticsearch/bin/plugin --install lukas-vlcek/bigdesk  
  
##############################################  
# 4. Install InfluxDB  
##############################################  
RUN curl -s -o /tmp/influxdb_latest_amd64.deb
https://s3.amazonaws.com/influxdb/influxdb_${INFLUXDB_VERSION}_amd64.deb && \  
dpkg -i /tmp/influxdb_latest_amd64.deb && \  
rm /tmp/influxdb_latest_amd64.deb && \  
rm -rf /var/lib/apt/lists/*  
  
##############################################  
# 5. Install RabbitMQ  
##############################################  
RUN \  
wget -qO - https://www.rabbitmq.com/rabbitmq-signing-key-public.asc | apt-key
add - && \  
echo "deb http://www.rabbitmq.com/debian/ testing main" >
/etc/apt/sources.list.d/rabbitmq.list && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y rabbitmq-server && \  
rm -rf /var/lib/apt/lists/* && \  
rabbitmq-plugins enable rabbitmq_management  
  
##############################################  
# 6. Install nginx  
##############################################  
RUN \  
add-apt-repository -y ppa:nginx/stable && \  
apt-get update && \  
apt-get install -y nginx && \  
rm -rf /var/lib/apt/lists/* && \  
echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \  
chown -R www-data:www-data /var/lib/nginx  
  
##############################################  
# 7. Install dashboard  
##############################################  
RUN mkdir -p /var/www/dashboard  
ADD dashboard.tar.gz /var/www/dashboard  
  
##############################################  
# 8. Install cep-engine  
##############################################  
RUN apt-get update && \  
apt-get install -y maven && \  
rm -rf /var/lib/apt/lists/* && \  
mkdir -p /opt/cep-engine-service  
  
  
ADD cep-engine-service.tar.gz /opt/cep-engine-service  
RUN chown root:root -R /opt/cep-engine-service && \  
cd /opt/cep-engine-service && \  
mvn clean package && \  
chmod 755 /opt/cep-engine-service/cep-engine  
  
##############################################  
# 9. Configuration  
##############################################  
#############################################################################  
#memcached  
EXPOSE 11211  
  
#############################################################################  
#influxdb  
RUN sed -i \  
-e 's/reporting-disabled[ \t]*=[ \t]*false/reporting-disabled = true/g' \  
-e 's/^file[^"]*"[^"]*log.txt"/file = "\/var\/log\/influxdb\/log.txt"/g' \  
-e 's/^dir[^"]*"[^"]*raft"/dir = "\/var\/influxdb\/data\/raft"/g' \  
-e 's/^dir[^"]*"[^"]*db"/dir = "\/var\/influxdb\/data\/db"/g' \  
-e 's/^dir[^"]*"[^"]*wal"/dir = "\/var\/influxdb\/data\/wal"/g' \  
/opt/influxdb/current/config.toml  
  
RUN echo 'curl -X POST "http://localhost:8086/cluster_admins?u=root&p=root" -d
"{\"name\": \"${DEFAULT_USER}\", \"password\": \"${DEFAULT_PASS}\"}"' >
/opt/influxdb/arms_init.sh && \  
echo 'curl -X POST "http://localhost:8086/cluster_admins/root?u=root&p=root"
-d "{\"password\": \"${DEFAULT_PASS}\"}"' >> /opt/influxdb/arms_init.sh && \  
chmod 755 /opt/influxdb/arms_init.sh  
  
# Admin server  
EXPOSE 8083  
# HTTP API  
EXPOSE 8086  
# HTTPS API  
EXPOSE 8084  
  
VOLUME ["/var/influxdb/data","/var/log/influxdb"]  
  
#############################################################################  
# elasticsearch  
RUN sed -i \  
-e 's/#cluster[.]name:[ \t]*elasticsearch/cluster.name: arms_ela/g' \  
-e 's/#path[.]data:[ \t]*\/path\/to\/data$/path.data: \/var\/elasticsearch\/data/g' \  
-e 's/#path[.]logs:[ \t]*\/path\/to\/logs/path.logs: \/var\/log\/elasticsearch/g' \  
/opt/elasticsearch/config/elasticsearch.yml  
  
# RUN echo 'curl -XDELETE "http://localhost:9200/arms"' >
/opt/elasticsearch/arms_init.sh && \  
# echo 'curl -XPUT "http://localhost:9200/arms" -d
"{\"settings\":{\"analysis\":{\"analyzer\":{\"default\":{\"stopwords\":\"_none_\",\"type\":\"pattern\",\"pattern\":\"\\\\\\\\\\\s+\"}}}}}"'
>> /opt/elasticsearch/arms_init.sh && \  
# chmod 755 /opt/elasticsearch/arms_init.sh  
  
  
# Expose ports.  
# - 9200: HTTP  
# - 9300: transport  
EXPOSE 9200  
EXPOSE 9300  
  
VOLUME ["/var/elasticsearch/data","/var/log/elasticsearch"]  
  
#############################################################################  
# RabbitMQ  
RUN echo "echo '[{rabbit, [' > /etc/rabbitmq/rabbitmq.config && \\\" >
/etc/rabbitmq/arms_init.sh && \  
echo "echo '{default_user, <<\"'\${DEFAULT_USER}'\">>},' >>
/etc/rabbitmq/rabbitmq.config && \\\" >> /etc/rabbitmq/arms_init.sh && \  
echo "echo '{default_pass, <<\"'\${DEFAULT_PASS}'\">>},' >>
/etc/rabbitmq/rabbitmq.config && \\\" >> /etc/rabbitmq/arms_init.sh && \  
echo "echo '{default_permissions, [<<\".*\">>, <<\".*\">>, <<\".*\">>]},' >>
/etc/rabbitmq/rabbitmq.config && \\\" >> /etc/rabbitmq/arms_init.sh && \  
echo "echo '{default_user_tags, [administrator]},' >>
/etc/rabbitmq/rabbitmq.config && \\\" >> /etc/rabbitmq/arms_init.sh && \  
echo "echo '{loopback_users, []}' >> /etc/rabbitmq/rabbitmq.config && \\\" >>
/etc/rabbitmq/arms_init.sh && \  
echo "echo ']}].' >> /etc/rabbitmq/rabbitmq.config" >>
/etc/rabbitmq/arms_init.sh && \  
chmod 755 /etc/rabbitmq/arms_init.sh  
  
# Expose ports.  
EXPOSE 5672  
EXPOSE 15672  
#############################################################################  
# nginx  
RUN echo "server {" > /etc/nginx/sites-enabled/default && \  
echo " listen 80 default_server;" >> /etc/nginx/sites-enabled/default && \  
echo " listen [::]:80 default_server;" >> /etc/nginx/sites-enabled/default &&
\  
echo " root /var/www/dashboard/src;" >> /etc/nginx/sites-enabled/default && \  
echo " index index.html index.htm index.nginx-debian.html;" >>
/etc/nginx/sites-enabled/default && \  
echo " server_name localhost;" >> /etc/nginx/sites-enabled/default && \  
echo " location / {" >> /etc/nginx/sites-enabled/default && \  
echo " try_files \$uri \$uri/ @rules;" >> /etc/nginx/sites-enabled/default &&
\  
echo " }" >> /etc/nginx/sites-enabled/default && \  
echo " location ~ (/_nodes|_search)\$ {" >> /etc/nginx/sites-enabled/default
&& \  
echo " proxy_pass http://localhost:9200;" >> /etc/nginx/sites-enabled/default
&& \  
echo " }" >> /etc/nginx/sites-enabled/default && \  
echo "}" >> /etc/nginx/sites-enabled/default  
  
# Expose ports.  
EXPOSE 80  
EXPOSE 443  
  
#############################################################################  
# dashboard  
#############################################################################  
# cep-engine  
RUN echo 'sed -i \' > /opt/cep-engine-service/arms_init.sh && \  
echo '-e "s/DEFAULT_USER/`echo $DEFAULT_USER`/gi" \' >> /opt/cep-engine-
service/arms_init.sh && \  
echo '-e "s/DEFAULT_PASS/`echo $DEFAULT_PASS`/gi" \' >> /opt/cep-engine-
service/arms_init.sh && \  
echo '-e
"s/^access.control.allow.origin=.*/access.control.allow.origin=http:\/\/`echo
$HOST_NAME`/gi" \' >> /opt/cep-engine-service/arms_init.sh && \  
echo '/opt/cep-engine-service/application.properties' >> /opt/cep-engine-
service/arms_init.sh && \  
chmod 755 /opt/cep-engine-service/arms_init.sh  
  
EXPOSE 8080  
  
  
#############################################################################  
#supervisor  
RUN mkdir -p /var/log/supervisor  
  
RUN echo '[supervisord]' > /etc/supervisor/conf.d/supervisord.conf && \  
echo 'nodaemon=true' >> /etc/supervisor/conf.d/supervisord.conf && \  
\  
echo '[program:memcached]' >> /etc/supervisor/conf.d/supervisord.conf && \  
echo 'command=/bin/bash -c "/usr/bin/memcached -u memcache -v"' >>
/etc/supervisor/conf.d/supervisord.conf && \  
\  
echo '[program:influxdb]' >> /etc/supervisor/conf.d/supervisord.conf && \  
echo 'command=/bin/bash -c "/usr/bin/influxdb
-config=/opt/influxdb/current/config.toml"' >>
/etc/supervisor/conf.d/supervisord.conf && \  
\  
echo '[program:elasticsearch]' >> /etc/supervisor/conf.d/supervisord.conf && \  
echo 'command=/bin/bash /opt/elasticsearch/bin/elasticsearch' >>
/etc/supervisor/conf.d/supervisord.conf && \  
\  
echo '[program:rabbitmq]' >> /etc/supervisor/conf.d/supervisord.conf && \  
echo 'command=/bin/bash -c "service rabbitmq-server start"' >>
/etc/supervisor/conf.d/supervisord.conf && \  
\  
echo '[program:influxdb-init]' >> /etc/supervisor/conf.d/supervisord.conf && \  
echo 'command=/bin/bash /opt/influxdb/arms_init.sh' >>
/etc/supervisor/conf.d/supervisord.conf && \  
\  
echo '[program:nginx]' >> /etc/supervisor/conf.d/supervisord.conf && \  
echo 'command=/bin/bash -c "service nginx start"' >>
/etc/supervisor/conf.d/supervisord.conf && \  
\  
echo '[program:cep-engine]' >> /etc/supervisor/conf.d/supervisord.conf && \  
echo 'command=/bin/bash -c "/opt/cep-engine-service/cep-engine start"' >>
/etc/supervisor/conf.d/supervisord.conf  
  
  
##############################################  
# 10. Start  
##############################################  
RUN echo "/etc/rabbitmq/arms_init.sh" > /usr/bin/start.sh && \  
echo "/opt/cep-engine-service/arms_init.sh" >> /usr/bin/start.sh && \  
echo "/usr/bin/supervisord" >> /usr/bin/start.sh && \  
chmod 755 /usr/bin/start.sh  
  
CMD ["sh", "-c", "/usr/bin/start.sh"]  

