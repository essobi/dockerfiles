FROM python:3.5  
# File Author / Maintainer  
MAINTAINER SoftFIRE  
  
  
RUN mkdir -p /var/log/softfire && mkdir -p /etc/softfire  
COPY etc/nfv-manager.ini /etc/softfire/  
COPY etc/openstack-credentials.json /etc/softfire/  
RUN ssh-keygen -t rsa -b 4096 -C "info@softfire.eu" -f /etc/softfire/softfire-
key.pem.pub  
COPY . /app  
# RUN pip install nfv-manager  
WORKDIR /app  
RUN pip install .  
  
EXPOSE 5053  
CMD ./nfv-manager  

