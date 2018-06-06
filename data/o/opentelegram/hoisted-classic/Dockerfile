FROM java:8  
RUN apt update && apt upgrade -y && \  
apt install -y apt-transport-https  
  
COPY hoisted.jar /usr/local/lib/  
  
COPY ./entrypoint.sh /usr/bin/entrypoint.sh  
RUN chmod +x /usr/bin/entrypoint.sh  
ENTRYPOINT ["/usr/bin/entrypoint.sh"]  

