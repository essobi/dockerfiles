FROM ubuntu:latest  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
curl \  
wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY exec.sh /exec.sh  
  
ENTRYPOINT ["/exec.sh"]  

