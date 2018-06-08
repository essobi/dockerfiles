FROM wow73611/ubuntu  
MAINTAINER wow73611 <wow73611@gmail.com>  
  
RUN \  
apt-get update -y && \  
apt-get install -y gearman-job-server && \  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 4730  
  
CMD ["gearmand"]  

