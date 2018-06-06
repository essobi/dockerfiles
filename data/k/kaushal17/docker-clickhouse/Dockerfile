FROM ubuntu:14.04  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv E0C56BD4  
  
RUN mkdir -p /etc/apt/sources.list.d && echo "deb
http://repo.yandex.ru/clickhouse/trusty stable main" | tee
/etc/apt/sources.list.d/clickhouse.list  
  
RUN apt-get update  
  
RUN apt-get install -y clickhouse-server-common clickhouse-client  
  
EXPOSE 9000 8123  
  
CMD service clickhouse-server start  
  
  

