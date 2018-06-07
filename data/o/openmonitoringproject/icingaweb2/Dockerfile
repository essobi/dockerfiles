FROM centos:7  
MAINTAINER Frank Hildebrandt <fhildebrandt@freicon.de>  
  
ENV DOCKERIZE_VERSION v0.2.0  
ENV TIMEZONE europe/berlin  
  
RUN rpm -i https://packages.icinga.org/epel/7/release/noarch/icinga-rpm-
release-7-1.el7.centos.noarch.rpm  
  
RUN [ -f /etc/rpm/macros.imgcreate ] && sed -i '/excludedocs/d'
/etc/rpm/macros.imgcreate || exit 0  
RUN [ -f /etc/yum.conf ] && sed -i '/nodocs/d' /etc/yum.conf || exit 0  
  
RUN yum -y install epel-release \  
&& yum -y install icingaweb2 icingacli wget mariadb \  
&& wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& yum clean all \  
&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
ADD . /  
  
RUN usermod -a -G icingaweb2 apache \  
&& icingacli setup config directory --group icingaweb2 \  
&& icingacli setup token create  
  
VOLUME /var/log/apache2  
VOLUME /var/lib/icingaweb2  
  
ENTRYPOINT
["/usr/local/bin/dockerize","-template","/resources.ini.tmpl:/etc/icingaweb2/resources.ini","-stdout","/var/log/apache2/access.log","-stderr","/var/log/apache2/error.log","-template","/phpdefaults.tmpl:/etc/php.d/icinga.ini"]  
CMD ["/entrypoint.sh"]  

