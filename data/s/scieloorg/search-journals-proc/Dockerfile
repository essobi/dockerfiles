FROM python:3.5.2  
MAINTAINER tecnologia@scielo.org  
  
RUN apt-get update && apt-get install -y libxml2  
  
COPY . /app  
  
RUN pip install --upgrade pip  
RUN chmod -R 755 /app/*  
  
WORKDIR /app  
  
RUN python setup.py install  
  
CMD ["update_search", "--help"]  

