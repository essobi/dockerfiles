FROM debian:jessie  
MAINTAINER Derek Vance <dvance@cerb-tech.com>  
  
  
RUN apt-get update && apt-get -y install wget software-properties-common  
  
RUN add-apt-repository 'deb http://repo.powerdns.com/debian jessie-auth-40
main'  
  
RUN echo "Package: pdns-*" >> /etc/apt/preferences.d/pdns && \  
echo "Pin: origin repo.powerdns.com" >> /etc/apt/preferences.d/pdns && \  
echo "Pin-Priority: 600" >> /etc/apt/preferences.d/pdns  
  
RUN wget https://repo.powerdns.com/FD380FBB-pub.asc && \  
apt-key add FD380FBB-pub.asc && \  
rm FD380FBB-pub.asc  
  
RUN apt-get update && \  
apt-get -y install pdns-server pdns-backend-mysql && \  
rm -rf /var/lib/apt/lists/*  
  
RUN rm /etc/powerdns/pdns.d/* && \  
echo "launch=gmysql" >> /etc/powerdns/pdns.d/gmysql.conf && \  
echo "gmysql-host=$SQL_HOST" >> /etc/powerdns/pdns.d/gmysql.conf && \  
echo "gmysql-port=$SQL_PORT" >> /etc/powerdns/pdns.d/gmysql.conf && \  
echo "gmysql-dbname=$SQL_DB" >> /etc/powerdns/pdns.d/gmysql.conf && \  
echo "gmysql-user=$SQL_USER" >> /etc/powerdns/pdns.d/gmysql.conf && \  
echo "gmysql-password=$SQL_PASS" >> /etc/powerdns/pdns.d/gmysql.conf && \  
echo "gmysql-dnssec=$SQL_DNSSEC" >> /etc/powerdns/pdns.d/gmysql.conf  
  
EXPOSE 53/tcp 53/udp 53000/tcp 8081/tcp  
  
ENTRYPOINT ["/usr/sbin/pdns_server", "--daemon=no"]

