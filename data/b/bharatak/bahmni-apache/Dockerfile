FROM centos:7  
MAINTAINER Bharat Akkinepalli <bharatak@thoughtworks.com>  
  
RUN sed -i 's/enabled=1/enabled=0/g' /etc/yum/pluginconf.d/fastestmirror.conf  
RUN yum --setopt=tsflags=nodocs -y update  
RUN yum --setopt=tsflags=nodocs -y install httpd mod_ssl wget unzip && yum
clean all  
  
ENV APACHE_RUN_USER apache  
ENV APACHE_RUN_GROUP apache  
ENV APACHE_LOG_DIR /var/log/httpd  
ENV APACHE_PID_FILE /var/run/httpd/httpd.pid  
ENV APACHE_RUN_DIR /var/run/httpd  
  
RUN mkdir -p $APACHE_LOG_DIR $APACHE_RUN_DIR  
RUN chown -R root:root /var/www/html  
  
ADD localhost.crt /etc/ssl/certs/localhost.crt  
RUN chown root:root /etc/ssl/certs/localhost.crt  
ADD localhost.key /etc/pki/tls/private/localhost.key  
RUN chown root:root /etc/pki/tls/private/localhost.key  
ADD ssl.conf /etc/httpd/conf.d/ssl.conf  
  
ADD setup-artifacts.sh /tmp/setup-artifacts.sh  
  
RUN chmod +x /tmp/setup-artifacts.sh  
  
RUN /tmp/setup-artifacts.sh apache  
  
WORKDIR /var/www/html  
  
EXPOSE 443  
VOLUME [ "/var/www/bahmni_config" ]  
  
VOLUME [ "/var/www/bahmniapps" ]  
  
ENTRYPOINT [ "/usr/sbin/httpd","-k","start", "-D", "FOREGROUND" ]  

