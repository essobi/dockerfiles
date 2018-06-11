FROM wnameless/oracle-xe-11g  
  
MAINTAINER Ian Collington <ian@iancollington.com>  
  
ADD scripts /scripts  
RUN /scripts/setup.sh  
  
EXPOSE 22  
EXPOSE 1521  
EXPOSE 8080  
ENTRYPOINT ["/usr/sbin/oracle_entrypoint.sh"]  

