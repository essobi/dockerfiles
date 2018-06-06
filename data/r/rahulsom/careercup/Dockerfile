FROM python:latest  
MAINTAINER Rahul Somasunderam  
  
RUN pip install lxml requests cssselect  
RUN mkdir -p /opt/careercup  
  
COPY careercup.py /opt/careercup/  
  
VOLUME ["/local"]  
WORKDIR /local  
ENTRYPOINT ["python", "/opt/careercup/careercup.py"]  

