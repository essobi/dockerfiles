FROM debian:stretch  
  
ENV PDNS_ALLOW_AXFR_IPS 127.0.0.1  
ENV PDNS_MASTER yes  
ENV PDNS_SLAVE no  
ENV PDNS_CACHE_TTL 20  
ENV PDNS_DISTRIBUTOR_THREADS 3  
ENV PDNS_RECURSIVE_CACHE_TTL 10  
ENV PDNS_ALLOW_RECURSION 127.0.0.1  
ENV PDNS_RECURSOR no  
  
ENV MYSQL_HOST localhost  
ENV MYSQL_PORT 3306  
ENV MYSQL_USER pdns  
ENV MYSQL_PASS ""  
ENV MYSQL_DB pdns  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y curl gnupg2 \  
&& curl https://repo.powerdns.com/FD380FBB-pub.asc | apt-key add - \  
&& echo "deb http://repo.powerdns.com/debian stretch-auth-40 main" \  
> /etc/apt/sources.list.d/pdns.list \  
&& apt-get update \  
&& apt-get install -y mariadb-client pdns-server pdns-backend-mysql \  
&& apt-get autoremove --purge -y curl \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY entrypoint.sh assets/pdns.sql /  
COPY assets/pdns.conf /etc/powerdns/pdns.conf  
COPY assets/pdns.local.*.conf /etc/powerdns/pdns.d/  
  
EXPOSE 53 53/udp  
  
ENTRYPOINT [ \  
"/bin/bash", \  
"/entrypoint.sh" \  
]  

