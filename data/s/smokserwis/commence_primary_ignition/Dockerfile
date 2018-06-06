FROM debian:jessie-slim  
  
RUN apt-get update && \  
apt-get install -y \  
python \  
python-setuptools \  
ca-certificates && \  
apt-get clean  
  
RUN easy_install requests && \  
rm -rf /tmp/easy*  
  
ADD commence_primary_ignition.py /root/commence_primary_ignition.py  
  
CMD ["/usr/bin/python", "/root/commence_primary_ignition.py"]  

