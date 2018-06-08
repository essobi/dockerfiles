FROM golang:1.7.4  
ENV DEBIAN_FRONTEND=noninteractive  
RUN echo 'deb http://repo.powerdns.com/debian jessie-auth-40 main' >
/etc/apt/sources.list.d/pdns.list \  
&& { \  
echo 'Package: pdns-*'; \  
echo 'Pin: origin repo.powerdns.com'; \  
echo 'Pin-Priority: 600'; \  
} > /etc/apt/preferences.d/pdns \  
&& curl -sSL https://repo.powerdns.com/FD380FBB-pub.asc | apt-key add - \  
&& apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xcbcb082a1bb943db
\  
&& { \  
echo 'deb [arch=amd64,i386]
http://ftp.yz.yamagata-u.ac.jp/pub/dbms/mariadb/repo/10.1/debian jessie main';
\  
echo 'deb-src http://ftp.yz.yamagata-u.ac.jp/pub/dbms/mariadb/repo/10.1/debian
jessie main'; \  
} > /etc/apt/sources.list.d/mariadb.list \  
&& apt-get update \  
&& apt-get install -y pdns-server pdns-backend-mysql mariadb-client \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN go get -u github.com/mattes/migrate  
  
COPY ./entrypoint.sh /opt/entrypoint  
RUN chmod 755 /opt/entrypoint  
ENTRYPOINT ["/opt/entrypoint"]  
  
COPY ./assets/database /opt/database  
  
CMD ["start"]  

