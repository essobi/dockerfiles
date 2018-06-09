FROM mvnfenzan/pentaho-di  
COPY pentaho /home/pentaho  
USER root  
RUN chown -R pentaho:pentaho /home/pentaho  
USER pentaho  
CMD ["-job=Data Warehouse/Clean Import"]  

