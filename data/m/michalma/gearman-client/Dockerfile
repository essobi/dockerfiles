FROM ubuntu:14.04  
  
RUN \  
apt-get update && \  
apt-get install -y python && \  
apt-get install -y git &&\  
apt-get install -y python-pip && \  
git clone https://github.com/zaro0508/gearman-plugin-client.git && \  
cp gearman-plugin-client/gear_client.py / && \  
python -m pip install gear && \  
python -m pip install simplejson && \  
python -m pip install uuid  
  
CMD ["bash"]  

