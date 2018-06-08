FROM haskell:8.0.2  
# Copy source into Docker image  
COPY ./ /home/app/  
WORKDIR /home/app  
  
# Install all dependencies and build project  
RUN stack build  
  
EXPOSE 8080  
# Start server  
CMD ["/usr/local/bin/stack", "exec", "silver-magpie"]  

