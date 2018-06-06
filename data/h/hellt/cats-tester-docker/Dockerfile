FROM alpine:3.6  
  
RUN apk add --no-cache python py-paramiko && \  
python -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip install --upgrade pip setuptools && \  
pip install future jinja2 py2-ipaddress pyvmomi PyYAML robotframework
robotframework-sshlibrary tabulate vspk==5.3.1 && \  
rm -r /root/.cache  
  
ENV NUAGE_RELEASE 5.3.1  

