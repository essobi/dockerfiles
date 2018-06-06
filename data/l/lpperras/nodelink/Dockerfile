FROM mono:5.0.1.1  
RUN mkdir /NodeLink  
  
EXPOSE 8090  
COPY startup.sh /usr/local/myscripts/mystart.sh  
  
VOLUME NodeLink  
  
CMD ["/bin/bash", "/usr/local/myscripts/mystart.sh"]  

