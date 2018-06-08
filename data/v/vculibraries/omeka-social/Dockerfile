FROM centos:centos7  
  
RUN yum -y update && yum clean all  
RUN yum -y install httpd  
RUN yum -y install php  
RUN yum -y install ImageMagick  
RUN yum -y install unzip  
RUN yum -y install wget  
RUN yum -y install mysql  
RUN yum -y install php-mysql  
RUN yum -y install openssl  
RUN yum -y install mod_ssl  
RUN yum -y install php-xml  
ADD run_httpd.sh /  
RUN chmod -v +x /run_httpd.sh  
COPY . /var/www/html  
COPY httpd.conf /etc/httpd/conf/httpd.conf  
RUN chown -R apache:apache /var/www/html/application/logs  
WORKDIR /var/www/html  
VOLUME /var/www/html/files  
VOLUME /etc/httpd/conf.d  
VOLUME /etc/pki/tls/certs  
EXPOSE 80  
EXPOSE 443  
CMD /run_httpd.sh  

