#only ment for develpoment  
FROM centos:7  
MAINTAINER manjula@thinkcube.com  
  
RUN yum clean all  
  
RUN yum install -y httpd && yum clean all  
  
RUN echo "IncludeOptional vhost.d/*.conf" >> /etc/httpd/conf/httpd.conf  
  
RUN sed -i 's/^\\([^#]\\)/#\1/g' /etc/httpd/conf.d/welcome.conf  
  
RUN sed -i "s|#ServerName www.example.com:80|ServerName proxy|"
/etc/httpd/conf/httpd.conf  
  
COPY default.conf /etc/httpd/conf.d/default.conf  
  
COPY index.html /var/www/html/index.html  
  
COPY rp /usr/local/bin/rp  
  
VOLUME ["/etc/httpd/vhost.d"]  
  
EXPOSE 80  
COPY run.sh /run.sh  
  
CMD ["/run.sh"]  

