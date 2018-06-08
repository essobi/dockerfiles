FROM debian:jessie  
MAINTAINER Mustafa Bayrak <mustafa.bayrak@windowslive.com>  
  
ENV PROXYSQL_VERSION=1.4.3  
RUN apt-get update && \  
apt-get install -y wget logrotate debconf-utils && \  
wget
https://www.percona.com/redir/downloads/proxysql/proxysql-${PROXYSQL_VERSION}/binary/debian/jessie/x86_64/proxysql_${PROXYSQL_VERSION}-1.1.jessie_amd64.deb
&& \  
wget https://repo.percona.com/apt/percona-release_0.1-5.jessie_all.deb && \  
dpkg -i percona-release_0.1-5.jessie_all.deb && \  
dpkg -i proxysql_${PROXYSQL_VERSION}-1.1.jessie_amd64.deb && \  
apt-get update && \  
apt-get install -y percona-server-client-5.7 && \  
rm -f percona-release_0.1-5.jessie_all.deb
proxysql_${PROXYSQL_VERSION}-1.1.jessie_amd64.deb && \  
rm -rf /var/lib/apt/lists/*  
  
ADD proxysql.cnf /etc/proxysql.cnf  
  
COPY proxysql-entry.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
VOLUME ["/var/lib/proxysql"]  
  
EXPOSE 6032 6033  
CMD [""]  

