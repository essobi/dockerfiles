FROM centos:latest  
  
MAINTAINER James Eckersall <james.eckersall@gmail.com>  
  
RUN \  
yum install -y epel-release scl-utils centos-release-scl centos-release-scl-rh
&& \  
rpm -ivh https://download.pydio.com/pub/linux/centos/7/pydio-
release-1-1.el7.centos.noarch.rpm && \  
rpm -Uvh
https://www.softwarecollections.org/en/scls/remi/php56more/epel-7-x86_64/download/remi-
php56more-epel-7-x86_64.noarch.rpm && \  
yum -y install httpd && \  
yum -y install pydio-all  
  
RUN \  
wget https://github.com/moxiecode/plupload/archive/v2.1.8.zip -O
/tmp/plupload.zip && \  
unzip /tmp/plupload.zip -d /tmp/ && \  
mv /tmp/plupload-2.1.8/js /usr/share/pydio/plugins/uploader.plupload/plupload
&& \  
rm -rf /tmp/plupload-2.1.8 /tmp/plupload.zip && \  
sed -i -e 's/^RewriteBase.*$/RewriteBase \//g' /usr/share/pydio/.htaccess && \  
sed -i -e 's/Listen 80/Listen 8080/g'
/opt/rh/httpd24/root/etc/httpd/conf/httpd.conf  
COPY run.sh /  
RUN chmod 0755 /run.sh  
COPY pydio.conf /opt/rh/httpd24/root/etc/httpd/conf.d/pydio.conf  
#RUN chown -R apache:root /opt/rh/httpd24/root /usr/share/pydio
/var/cache/pydio /var/lib/pydio /var/opt/rh/rh-php56/lib  
#RUN chmod 0775 -R /var/log /etc/opt/rh/rh-php56
/opt/rh/httpd24/root/etc/httpd /opt/rh/httpd24/root/var/run/httpd
/opt/rh/httpd24/root/etc/httpd/logs /var/cache/pydio /var/lib/pydio
/var/opt/rh/rh-php56/lib/php/session  
  
ENV MAX_UPLOAD 2048M  
  
EXPOSE 8080  
ENTRYPOINT '/run.sh'  

