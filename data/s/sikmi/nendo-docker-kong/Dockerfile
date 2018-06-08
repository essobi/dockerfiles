FROM mashape/kong:0.8.1  
COPY config.docker/kong.yml /etc/kong/kong.yml  
  
ADD setup.sh setup.sh  
  
CMD ./setup.sh && kong start  

