FROM centos:centos7  
  
MAINTAINER fenoyc  
  
# base system upgrade and system dependencies  
RUN yum upgrade -y && \  
yum install -y epel-release &&\  
yum install -y ganglia-gmond ganglia-gmond-python ganglia ganglia-web ganglia-
gmetad supervisor &&\  
yum clean all &&\  
cp /usr/share/ganglia/conf/default.json
/usr/share/ganglia/conf/view_default.json /var/lib/ganglia/conf/ &&\  
sed -i -e 's:DocumentRoot "/var/www/html":DocumentRoot "/usr/share/ganglia":'
-e 's:Directory "/var/www/html":Directory "/usr/share/ganglia":'
/etc/httpd/conf/httpd.conf  
  
# add the start script  
ADD start.sh start.sh  
  
ADD supervisord.conf /etc/supervisord.conf  
  
EXPOSE 80 8649/udp 8651 8652  
# entrypoint is the start script  
ENTRYPOINT ["bash","start.sh"]  
  
# default is with gmond for seeing something  
CMD ["--with-gmond"]  

