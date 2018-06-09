FROM tristanpenman/wordpress  
# Copy over scripts  
COPY run.sh /  
# Install sudo  
RUN apt-get update && apt-get install -y sudo  
# Set permissions  
RUN chmod +x /run.sh  
CMD ["/run.sh"]  

