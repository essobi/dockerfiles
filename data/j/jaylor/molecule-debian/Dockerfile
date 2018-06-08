FROM debian:9.3  
  
COPY ./requirements.txt /requirements.txt  
  
RUN set -ex; \  
\  
apt-get update; \  
apt-get install -y \  
python-pip libssl-dev procps \  
; \  
rm -rf /var/lib/apt/lists/* ; \  
pip install --no-cache-dir -r /requirements.txt  

