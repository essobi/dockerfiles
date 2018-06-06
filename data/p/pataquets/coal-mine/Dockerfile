FROM python:3  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y pandoc \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
pip install --no-cache-dir coal-mine  
  
ADD ./files/etc/coal-mine.ini /etc/  
  
CMD [ "coal-mine" ]  

