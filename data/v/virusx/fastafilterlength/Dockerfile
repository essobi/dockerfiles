FROM ubuntu:16.04  
COPY fastafilterlength.py /usr/local/bin/  
RUN apt-get update && \  
apt-get install -y python-biopython && \  
chmod +x /usr/local/bin/fastafilterlength.py && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

