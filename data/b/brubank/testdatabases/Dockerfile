FROM ubuntu:16.04  
ENV ES_SKIP_SET_KERNEL_PARAMETERS true  
RUN apt-get update && apt-get install -y curl default-jre apt-transport-https
&&\  
curl https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add \- &&\  
echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | tee -a
/etc/apt/sources.list.d/elastic-6.x.list &&\  
apt-get update && apt-get install -y elasticsearch &&\  
apt-get remove -y curl apt-transport-https &&\  
chown -R elasticsearch:elasticsearch /usr/share/elasticsearch &&\  
echo "action.auto_create_index: false" >> /etc/elasticsearch/elasticsearch.yml
&&\  
sed -E -i 's/-Xms1g/-Xms512m/g' /etc/elasticsearch/jvm.options &&\  
sed -E -i 's/-Xmx1g/-Xmx512m/g' /etc/elasticsearch/jvm.options  
RUN apt-get install -y rabbitmq-server  
RUN apt-get install -y redis-server  
CMD service redis-server start & service rabbitmq-server start & su -c
"ES_PATH_CONF=/etc/elasticsearch /usr/share/elasticsearch/bin/elasticsearch"
-s /bin/bash elasticsearch  
EXPOSE 9200  
EXPOSE 6379  

