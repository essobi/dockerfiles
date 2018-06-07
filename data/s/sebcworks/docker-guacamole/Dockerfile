  
FROM guacamole/guacamole  
  
RUN apt update && apt -y upgrade && \  
apt -y install postgresql-client  
  
RUN mkdir -p /init && \  
chmod 750 /init  
  
# Will init database and/or launch guacamole  
COPY guacamole-start.sh /guacamole-start.sh  
  
RUN chmod 750 /guacamole-start.sh  
  
ENTRYPOINT ["/guacamole-start.sh"]  

