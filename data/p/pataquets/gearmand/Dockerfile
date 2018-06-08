FROM pataquets/ubuntu:trusty  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
gearman-job-server \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 4730  
  
ENTRYPOINT [ "gearmand" ]  

