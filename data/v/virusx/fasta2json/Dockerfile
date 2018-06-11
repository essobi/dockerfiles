FROM ubuntu:16.04  
COPY fasta2json.py /usr/local/bin/  
RUN apt-get update && \  
apt-get install -y python-biopython && \  
chmod +x /usr/local/bin/fasta2json.py && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

