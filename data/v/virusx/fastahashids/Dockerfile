FROM ubuntu:16.04  
COPY regenerate_ids.py update_ids.py /usr/local/bin/  
RUN apt-get update && \  
apt-get install -y python-pip python-biopython && \  
pip install base32-crockford && \  
chmod +x /usr/local/bin/regenerate_ids.py && \  
chmod +x /usr/local/bin/update_ids.py && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

