FROM sudokeys/baseimage  
MAINTAINER Bertrand RETIF <bertrand@sudokeys.com>  
  
RUN apt-get update && apt-get install -y \  
ca-certificates \  
python2.7 \  
python-setuptools \  
python-simplejson \  
python-imaging \  
sqlite3 \  
python-mysqldb  
  
RUN ulimit -n 30000  
ENV SEAFILE_VERSION 4.0.5  
RUN useradd -d /opt/seafile -m seafile  
WORKDIR /opt/seafile  
RUN curl -L -O https://bitbucket.org/haiwen/seafile/downloads/seafile-
server_${SEAFILE_VERSION}_x86-64.tar.gz  
RUN tar xzf seafile-server_${SEAFILE_VERSION}_x86-64.tar.gz  
RUN mkdir -p logs  
  
# Config env variables  
ENV autostart true  
ENV autoconf true  
ENV autonginx false  
ENV fcgi false  
ENV CCNET_PORT 10001  
ENV CCNET_NAME my-seafile  
ENV SEAFILE_PORT 12001  
ENV FILESERVER_PORT 8082  
ENV EXISTING_DB false  
ENV MYSQL_HOST mysql-container  
ENV MYSQL_PORT 3306  
ENV MYSQL_USER seafileuser  
ENV SEAHUB_ADMIN_EMAIL seaadmin@sea.com  
ENV CCNET_DB_NAME ccnet-db  
ENV SEAFILE_DB_NAME seafile-db  
ENV SEAHUB_DB_NAME seahub-db  
ENV SEAHUB_PORT 8000  
ENV STATIC_FILES_DIR /opt/seafile/nginx/  
  
#removing default seafile installation scripts to replace them with our own  
RUN rm seafile-server-${SEAFILE_VERSION}/check_init_admin.py  
RUN rm seafile-server-${SEAFILE_VERSION}/setup-seafile-mysql.py  
  
RUN mkdir -p /etc/my_init.d  
  
#Adding all our scripts  
COPY scripts/setup-seafile-mysql.sh /etc/my_init.d/setup-seafile-mysql.sh  
COPY scripts/create_nginx_config.sh /etc/my_init.d/z_create_nginx_config.sh  
COPY scripts/check_init_admin.py /opt/seafile/seafile-
server-${SEAFILE_VERSION}/check_init_admin.py  
COPY scripts/setup-seafile-mysql.py /opt/seafile/seafile-
server-${SEAFILE_VERSION}/setup-seafile-mysql.py  
COPY nginx.conf /root/seafile.conf  
RUN chown -R seafile:seafile /opt/seafile  
  
# Seafile daemons  
RUN mkdir /etc/service/seafile /etc/service/seahub  
COPY scripts/seafile.sh /etc/service/seafile/run  
COPY scripts/seahub.sh /etc/service/seahub/run  
  
VOLUME /opt/seafile  
EXPOSE 10001 12001 8000 8082  
# Baseimage init process  
ENTRYPOINT ["/sbin/my_init"]  
  

