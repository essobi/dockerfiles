FROM debian:wheezy  
  
ADD . /pastie  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends python2.7 python-pip && \  
pip install -r /pastie/requirements.txt && \  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists/*  
  
CMD /pastie/start.sh  
  

