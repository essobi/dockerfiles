FROM download13/alpine-tls  
  
RUN apk-install mysql \  
&& mkdir -p /var/lib/mysql \  
&& chown -R mysql:mysql /var/lib/mysql  
  
CMD ["mysqld", "--skip-grant-tables", "--bind-address", "0.0.0.0", "--user",
"mysql", "--socket", "none"]  

