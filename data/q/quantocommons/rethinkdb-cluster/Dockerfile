FROM rethinkdb:2.3.6  
MAINTAINER Lucas Teske <lucas@contaquanto.com.br>  
  
RUN apt update && apt install -y curl && rm -rf /var/lib/apt/lists/*  
  
COPY main.sh /main.sh  
COPY proxy.sh /proxy.sh  
  
# For Dockerhub Automate build bug  
RUN chmod +x /main.sh  
RUN chmod +x /proxy.sh  
  
CMD /main.sh  

