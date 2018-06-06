FROM python:3-alpine  
  
COPY requirements.txt /  
  
RUN apk add --no-cache gcc linux-headers musl-dev python-dev && \  
pip install --no-cache -r /requirements.txt && \  
apk del gcc linux-headers musl-dev python-dev  
  
COPY manage-cluster-state /  
  
# Expose volume for adding credentials  
VOLUME ["/root/.aws"]  
  
# Expose directory to write output to, and to potentially read certs from  
VOLUME ["/etc/sysconfig/", "/etc/certs"]  
  
CMD ["python3", "/manage-cluster-state"]  

