FROM nyasara/docker-managementbase  
  
# Declare the volume for where the config will be  
VOLUME /etc/synchronizer  
WORKDIR /working  
  
# Copy the worker script in and make it executable  
COPY synchronizer.sh /working/  
RUN chmod 750 /working/synchronizer.sh  
  
# Run the watch script forever  
CMD ["/bin/bash","/working/synchronizer.sh"]  

