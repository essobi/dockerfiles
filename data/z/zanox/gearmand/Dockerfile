FROM debian:jessie  
  
RUN apt-get update && DEBIAN_FRONTENT=noninteractive \  
apt-get install -yqq gearman-job-server && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
EXPOSE 4730  
CMD ["gearmand"]  

