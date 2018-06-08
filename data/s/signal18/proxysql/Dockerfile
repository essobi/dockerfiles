# vim:set ft=dockerfile:  
FROM debian:jessie  
  
MAINTAINER Guillaume Lefranc <guillaume@signal18.io>  
  
ENV PROXYSQL_MAJOR 1.4  
ENV PROXYSQL_VERSION 1.4.8  
  
RUN apt-get update && \  
apt-get install -y curl && \  
curl -sLO
https://github.com/sysown/proxysql/releases/download/v$PROXYSQL_VERSION/proxysql_$PROXYSQL_VERSION-
debian8_amd64.deb && \  
dpkg -i proxysql_$PROXYSQL_VERSION-debian8_amd64.deb && \  
rm -f proxysql_$PROXYSQL_VERSION-debian8_amd64.deb && \  
rm -rf /var/lib/apt/lists/*  
  
CMD ["proxysql", "-f"]  

