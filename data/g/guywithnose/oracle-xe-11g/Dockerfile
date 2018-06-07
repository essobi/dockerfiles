FROM ubuntu:16.04  
MAINTAINER Wei-Ming Wu <wnameless@gmail.com>  
  
ADD assets /assets  
RUN /assets/setup.sh  
  
ENV ORACLE_HOME /u01/app/oracle/product/11.2.0/xe  
ENV ORACLE_SID XE  
RUN /usr/sbin/startup.sh && echo 'alter profile DEFAULT limit
password_life_time UNLIMITED;' | /u01/app/oracle/product/11.2.0/xe/bin/sqlplus
sys/password as SYSDBA  
  
EXPOSE 22  
EXPOSE 1521  
EXPOSE 8080  
CMD /usr/sbin/startup.sh && /usr/sbin/sshd -D  

