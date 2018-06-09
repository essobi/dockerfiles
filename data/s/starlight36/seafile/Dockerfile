FROM phusion/baseimage:latest  
MAINTAINER Max Liu <starlight36@163.com>  
  
  
  
RUN apt-get update && \  
apt-get install -y python2.7 python-setuptools python-imaging python-mysqldb
expect  
  
RUN mkdir -p /opt/seafile/ && \  
cd /opt/seafile && \  
curl -O http://download-cn.seafile.com/seafile-server_4.3.2_x86-64.tar.gz && \  
tar zxf seafile-server_4.3.2_x86-64.tar.gz && \  
rm -rf seafile-server_4.3.2_x86-64.tar.gz && \  
mv seafile-server-* seafile-server && \  
cd seafile-server  
  
RUN mkdir -p /etc/service/seafile /etc/service/seahub  
ADD seafile.sh /etc/service/seafile/run  
ADD seahub.sh /etc/service/seahub/run  
ADD entrypoint.sh /sbin/entrypoint.sh  
RUN chmod +x /etc/service/seafile/run \  
/etc/service/seahub/run \  
/sbin/entrypoint.sh  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /opt/seafile/seafile-server  
ENTRYPOINT ["/sbin/entrypoint.sh"]  
CMD ["/sbin/my_init"]

