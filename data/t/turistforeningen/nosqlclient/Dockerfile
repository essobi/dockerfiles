FROM mongoclient/mongoclient:2.2.0  
  
VOLUME ["/secrets"]  
  
# Need root to add files  
USER root  
  
# Add script for sourcing secrets and running the app  
RUN mkdir /app  
COPY run.sh /app/run.sh  
RUN chmod +x /app/run.sh  
  
# Switch back to user node  
USER node  

