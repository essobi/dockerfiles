FROM ubuntu:14.04  
MAINTAINER Sam Day <me@samcday.com.au>  
  
RUN apt-get update  
RUN apt-get install --yes --force-yes wget  
RUN wget http://powerdnssec.org/downloads/packages/pdns-
static_3.4.0-rc1-1_amd64.deb  
RUN dpkg -i pdns-static_3.4.0-rc1-1_amd64.deb  
  
RUN mkdir -p /var/lib/powerdns  
ADD pdns.sqlite3 /var/lib/powerdns/pdns.sqlite3  
  
ENTRYPOINT [ "/usr/sbin/pdns_server" ]  
CMD [ "--no-config", \  
"--master", \  
"--daemon=no", \  
"--local-address=0.0.0.0", \  
"--webserver=yes", \  
"--webserver-port=8081", \  
"--webserver-password=", \  
"--webserver-address=0.0.0.0", \  
"--experimental-json-interface=yes", \  
"--launch=gsqlite3", \  
"--gsqlite3-database=/var/lib/powerdns/pdns.sqlite3"]  

