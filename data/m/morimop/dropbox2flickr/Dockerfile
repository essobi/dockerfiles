FROM python:2.7-alpine  
  
RUN pip install flickr_api \  
&& pip install dropbox \  
&& mkdir /usr/local/python-app  
  
COPY transfer.py /usr/local/python-app  
  
WORKDIR /usr/local/python-app  
  
CMD ["python", "transfer.py"]  

