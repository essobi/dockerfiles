FROM ubuntu:16.04  
COPY install.sh /usr/bin/install.sh  
  
RUN chmod +x /usr/bin/install.sh && bash install.sh  
  
CMD ["python", "-m", "SimpleHTTPServer"]  

