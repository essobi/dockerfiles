#ibmcloudprivate/k8s-service-accounts  
FROM ubuntu  
  
# Copy files  
COPY runtime.sh /  
# Modify file permissions  
RUN chmod +x runtime.sh  
  
# Install curl  
RUN apt-get update  
RUN apt-get install curl -y  
  
# Run script on startup  
CMD [ "/runtime.sh" ]  

