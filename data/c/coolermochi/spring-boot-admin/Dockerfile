FROM centos:6  
MAINTAINER coolermochi@gmail.com  
  
# install  
RUN yum install -y java-1.8.0-openjdk-devel.x86_64 | true  
RUN yum clean all  
  
# settings  
# language  
COPY conf/i18n /etc/sysconfig/  
RUN source /etc/sysconfig/i18n && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8  
  
# clock  
COPY conf/clock /etc/sysconfig/  
RUN source /etc/sysconfig/clock  
RUN \cp -p -f /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
  
# spring boot  
COPY conf/spring-boot-admin/spring-boot-admin.sh /etc/init.d/spring-boot-admin  
COPY conf/spring-boot-admin/spring-boot-admin.conf /etc/sysconfig/spring-boot-
admin  
  
# services  
COPY conf/services.sh /etc/  
  
# permission  
RUN chmod 777 -R /opt/ && \  
chmod 777 /etc/init.d/spring-boot-admin && \  
chmod 777 /etc/services.sh  
  
# port  
EXPOSE 8080  
# app  
COPY conf/spring-boot-admin/spring-boot-admin-1.2.1.jar /opt/spring-boot-
admin.jar  
  
# start  
ENTRYPOINT /etc/services.sh

