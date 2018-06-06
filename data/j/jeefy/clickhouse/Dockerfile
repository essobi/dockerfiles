FROM ubuntu:14.04  
MAINTAINER Jeffrey Sica <jeef111x@gmail.com>  
  
EXPOSE 8123 9000  
RUN mkdir -p /etc/apt/sources.list.d && \  
echo "deb http://repo.yandex.ru/clickhouse/trusty/ dists/stable/main/binary-
amd64/" | \  
sudo tee /etc/apt/sources.list.d/clickhouse.list  
  
RUN apt-get update && \  
apt-get install -y \  
\--allow-unauthenticated \  
clickhouse-server-common clickhouse-client  
  
ENTRYPOINT ["clickhouse-server"]  
  
CMD ["--config-file", "/etc/clickhouse-server/config.xml"]

