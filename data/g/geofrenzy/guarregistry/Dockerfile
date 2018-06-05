FROM ubuntu:16.04  
LABEL vendor=GeoFrenzy\ Incorporated \  
com.example.is-beta= \  
com.example.is-production="" \  
com.example.version="0.0.1-beta" \  
com.example.release-date="2017-08-15"  
RUN apt-get update && apt-get install -y \  
curl \  
apt-utils \  
&& echo deb [arch=amd64] http://repo.powerdns.com/ubuntu xenial-auth-40 main >
/etc/apt/sources.list.d/pdns.list \  
&& printf "Package: pdns-*\nPin: origin repo.powerdns.com\nPin-Priority: 600"
| tee --append /etc/apt/preferences.d/pdns \  
&& curl https://repo.powerdns.com/FD380FBB-pub.asc | apt-key add - \  
&& apt-get update && apt-get install -y \  
pdns-server \  
pdns-backend-sqlite3 \  
pdns-backend-remote \  
pdns-tools \  
&& rm -rf /var/lib/apt/lists/*  
VOLUME ["/data"]  
COPY pdns-sqlite.conf /etc/powerdns/pdns.d/pdns-sqlite.conf  
COPY powerdns.sqlite3 /tmp/powerdns.sqlite3  
COPY delegate.sh /usr/local/bin/  
EXPOSE 53/udp 53/tcp 8081/tcp 53000/tcp  
  
ENTRYPOINT ["/usr/local/bin/delegate.sh"]  

