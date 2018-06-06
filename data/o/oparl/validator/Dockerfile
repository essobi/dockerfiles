FROM oparl/liboparl  
  
# Provide Validator  
ADD . /validator  
WORKDIR /validator  
  
# Install dependencies  
RUN apt update && \  
apt install -y --no-install-recommends \  
python3-pip python3-setuptools python3-gi redis-server && \  
apt autoremove -y && \  
apt clean && \  
rm -rf /var/lib/apt/lists/* && \  
echo "daemonize yes" >> /etc/redis/redis.conf && \  
pip3 install -r requirements.txt  
  
ENTRYPOINT ["sh", "./docker-validate.sh"]  

