FROM debian:jessie  
  
MAINTAINER Andrea Usuelli <andreausu@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y wget && \  
wget
https://github.com/sysown/proxysql/releases/download/1.3.0f/proxysql_1.3.0f-debian8_amd64.deb
-O /opt/proxysql_1.3.0f-debian8_amd64.deb && \  
dpkg -i /opt/proxysql_1.3.0f-debian8_amd64.deb && \  
rm -f /opt/proxysql_1.3.0f-debian8_amd64.deb && \  
rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["proxysql", "-f"]  

