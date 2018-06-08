FROM rancher/server:v1.6.16  
  
RUN apt-get update \  
&& service mysql stop \  
&& apt-get purge -y mysql-server \  
&& rm -rf /etc/mysql/* \  
&& apt-get autoremove -y --purge \  
&& rm -rf /var/lib/apt/lists/*  

