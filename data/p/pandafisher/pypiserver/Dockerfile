FROM python:2.7-slim  
RUN pip install pypiserver==1.2.0 passlib==1.7.0 && mkdir -p /apps/pypiserver
/apps/pypiserver/packages  
CMD ["/usr/local/bin/pypi-server","-p","80", "/apps/pypiserver/packages"]  
EXPOSE 80  

