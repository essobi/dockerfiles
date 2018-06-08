FROM blang/latex  
  
RUN apt-get update -q && apt-get install -qy wget tar unzip  
  
ADD entrypoint.sh /opt/entrypoint.sh  
  
ENTRYPOINT ["/opt/entrypoint.sh"]  

