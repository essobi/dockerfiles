FROM httpd:2.4  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends libaprutil1-ldap ca-certificates
\  
&& rm -r /var/lib/apt/lists/*  
  
RUN echo "Include /usr/local/apache2/conf/proxy_ldap.conf" >>
/usr/local/apache2/conf/httpd.conf  
  
ADD ./proxy_ldap.conf.template /proxy_ldap.conf.template  
ADD ./run.sh /run.sh  
RUN chmod +x /run.sh  
  
CMD /run.sh  

