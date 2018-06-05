FROM wnameless/oracle-xe-11g:16.04  
  
MAINTAINER Laurent Leseigneur <laurent.leseigneur@bonitasoft.com>  
ADD sysdba/init-databases.sql /docker-entrypoint-initdb.d/sysdba/  
ADD create-xaview.sh /docker-entrypoint-initdb.d/

