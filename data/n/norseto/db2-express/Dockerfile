FROM ibmcom/db2express-c  
  
ENV LICENSE accept  
ENV DB2INST1_PASSWORD '<YourStrong!Passw0rd>'  
RUN mv /entrypoint.sh /entrypoint_org.sh  
COPY entrypoint.sh /  
COPY db2-setup.sh /  
RUN chmod +x /entrypoint.sh \  
&& chmod +x /db2-setup.sh \  
&& mkdir /docker-entrypoint-initdb.d  
#COPY create_db_script.sh /docker-entrypoint-initdb.d/  
#COPY insert_initial_data.sql /docker-entrypoint-initdb.d/  
ENTRYPOINT ["/entrypoint.sh"]  
CMD [""]  
  

