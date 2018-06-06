FROM hachque/opensuse  
  
# Perform initial setup  
ADD setup /setup  
RUN /setup  
RUN rm /setup  
  
# Add the init script  
ADD init /init  
  
# Set /init as the default  
CMD ["/init"]  

