FROM debian:jessie  
  
COPY pdns.list /etc/apt/sources.list.d/pdns.list  
COPY preferences /etc/apt/preferences.d/pdns  
COPY FD380FBB-pub.asc /tmp/apt-key.asc  
  
RUN apt-key add /tmp/apt-key.asc \  
&& apt-get update \  
&& apt-get install -y pdns-server pdns-backend-mysql \  
&& rm -rf /var/cache/apt \  
&& mv /etc/powerdns /etc/powerdns.dist  
  
EXPOSE 53 53/udp 8081  
ENTRYPOINT ["pdns_server", "--master=yes", "--slave=yes", "--webserver=yes"]  

