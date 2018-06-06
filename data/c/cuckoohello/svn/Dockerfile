FROM phusion/baseimage  
MAINTAINER Yafeng Shan <cuckoo@kokonur.me>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Configure locales and timezone  
RUN apt-get update && apt-get install -y tzdata && apt-get clean && locale-gen
en_US.UTF-8 && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo
"Asia/Shanghai" > /etc/timezone  
  
RUN sed -i 's/archive.ubuntu.com/mirrors.tuna.tsinghua.edu.cn/g'
/etc/apt/sources.list \  
&& apt-get update && apt-get install -y apache2 libapache2-mod-svn && apt-get
clean  
RUN a2enmod authnz_ldap ldap headers  
  
COPY limit.conf /etc/apache2/conf-enabled/  
  
COPY 000-default.conf /etc/apache2/sites-enabled/000-default.conf  
  
RUN echo www-data > /etc/container_environment/APACHE_RUN_USER  
RUN echo www-data > /etc/container_environment/APACHE_RUN_GROUP  
RUN echo /var/log/apache2 > /etc/container_environment/APACHE_LOG_DIR  
RUN echo /var/lock/apache2 > /etc/container_environment/APACHE_LOCK_DIR  
RUN echo /var/run/apache2.pid > /etc/container_environment/APACHE_PID_FILE  
  
RUN mkdir -p /etc/service/apache  
COPY start-apache.sh /etc/service/apache/run  
  
VOLUME ["/var/lib/svn"]  
  
EXPOSE 80  

