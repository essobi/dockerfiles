FROM python:2.7  
maintainer compass  
  
RUN apt-get update  
RUN apt-get install -y libldap2-dev libsasl2-dev  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY requirements.txt /usr/src/app/  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY . /usr/src/app  
  
CMD ["python", "collect.py"]  

