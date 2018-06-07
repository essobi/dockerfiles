FROM indigolabs/secure-base:httpd  
MAINTAINER Nicolas Seigneur <nseigneur@indigoconsulting.ca>  
  
#Create Template folder  
RUN mkdir /etc/httpd/templates \  
&& mkdir /etc/httpd/bin/ \  
&& mkdir /var/www/html/private/  
  
#Copy Configuration script, templates, HTML files as well as startup script  
COPY ./conf/configure.sh /etc/httpd/bin/  
COPY ./templates/*.ctmpl /etc/httpd/templates/  
COPY ./html/index.html /var/www/html/index.html  
COPY ./html/private-index.html /var/www/html/private/index.html  
COPY ./run-httpd.sh /  
  
#Copy Consul and Vault property file  
COPY ./conf/consul.cfg /etc/bootstrap/conf/  
  
#Make scripts executable  
RUN chmod 744 ./run-httpd.sh \  
&& chmod 744 /etc/httpd/bin/*.sh  
  
#Allow other containers on same network to connect on these ports  
EXPOSE 80 443  
CMD ["/bin/bash","./run-httpd.sh"]  

