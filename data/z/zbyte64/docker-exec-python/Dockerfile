FROM python:3.5-alpine  
  
RUN apk update  
RUN apk add git  
RUN pip3 install git+git://github.com/EditLLC/python-
montage@feature/v2#egg=montage  
  
RUN mkdir -p /opt/app  
WORKDIR /opt/app  
ADD ./start.py /opt/app/start.py  
  
CMD ["python3", "start.py"]  

