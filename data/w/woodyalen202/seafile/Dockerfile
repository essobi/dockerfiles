FROM ubuntu:14.04  
MAINTAINER lucienchu<lucienchu@hotmail.com>  
  
RUN echo "Asia/Shanghai" > /etc/timezone;dpkg-reconfigure -f noninteractive
tzdata \  
# && sed -Ei
'1,$s/http:\/\/archive.ubuntu.com\/ubuntu\//http:\/\/cn.archive.ubuntu.com\/ubuntu\//g'
/etc/apt/sources.list \  
&& apt-get update -q \  
&& apt-get upgrade -y \  
&& apt-get install -y python2.7 \  
python-setuptools \  
python-imaging \  
python-ldap \  
python-mysqldb \  
python-memcache \  
python-urllib3 \  
curl \  
nginx \  
mysql-client  
  
VOLUME /data  
WORKDIR /app  
ENV SEAFILE_VERSION=5.1.3 \  
INSTALL_PATH=/app/haiwen/seafile-server-5.1.3 \  
TOP_PATH=/app/haiwen  
  
  
RUN curl 'http://download-cn.seafile.com/seafile-server_5.1.3_x86-64.tar.gz'
-o seafile-server_5.1.3_x86-64.tar.gz \  
&& mkdir -p haiwen/installed \  
&& mv seafile-server_5.1.3_x86-64.tar.gz haiwen/installed \  
&& cd haiwen/installed \  
&& tar -zxvf seafile-server_5.1.3_x86-64.tar.gz -C /app/haiwen  
  
COPY docker-entrypoint.sh /app  
COPY check_admin.py /app  
COPY seafile.conf /app  
COPY crontab /etc/cron.d/  
  
ENTRYPOINT ["/app/docker-entrypoint.sh"]

