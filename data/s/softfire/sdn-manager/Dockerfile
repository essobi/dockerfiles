FROM python:3.5  
# File Author / Maintainer  
MAINTAINER SoftFIRE  
  
  
RUN mkdir -p /var/log/softfire && mkdir -p /etc/softfire  
COPY etc/sdn-manager.ini /etc/softfire/  
COPY etc/sdn-resources.json /etc/softfire/  
COPY . /app  
# RUN pip install sdn-manager  
WORKDIR /app  
RUN pip install .  
  
EXPOSE 5058  
CMD ./sdn-manager  

