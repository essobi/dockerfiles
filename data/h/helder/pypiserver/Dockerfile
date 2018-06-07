FROM python:3.6-alpine  
LABEL maintainer=helder  
  
RUN pip install pypiserver passlib  
RUN mkdir -p /data && touch /.htpasswd  
  
EXPOSE 80  
VOLUME ["/data"]  
  
CMD ["pypi-server", "-p", "80", "-P", "/.htpasswd", "-a",
"update,download,list", "/data"]  

