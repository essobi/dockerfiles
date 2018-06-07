FROM wnameless/oracle-xe-11g  
  
MAINTAINER Fabio H Gonzales Barbosa <fbarbosa@atech.com.br>  
  
COPY assets/healthcheck.sh /usr/sbin/healthcheck.sh  
  
HEALTHCHECK \--interval=30s --retries=16 CMD [ "/usr/sbin/healthcheck.sh"]  
  
CMD /usr/sbin/startup.sh && tail -f /dev/null

