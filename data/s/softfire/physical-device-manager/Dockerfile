FROM python:3.5  
# File Author / Maintainer  
MAINTAINER SoftFIRE  
  
  
RUN mkdir -p /var/log/softfire && mkdir -p /etc/softfire  
COPY etc/physical-device-manager.ini /etc/softfire/  
COPY etc/physical-resources.json /etc/softfire/  
COPY . /app  
# RUN pip install nfv-manager  
WORKDIR /app  
RUN pip install .  
  
EXPOSE 5054  
CMD ./physical-device-manager  

