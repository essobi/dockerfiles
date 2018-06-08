FROM python:3.5  
# File Author / Maintainer  
MAINTAINER SoftFIRE  
  
  
RUN mkdir -p /var/log/softfire && mkdir -p /etc/softfire  
COPY etc/template/security-manager.ini /etc/softfire/  
COPY . /app  
# RUN pip install security-manager  
WORKDIR /app  
RUN pip install .  
  
EXPOSE 5060  
EXPOSE 4096  
CMD ./security-manager  

