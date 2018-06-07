FROM python:3.5.2  
MAINTAINER tecnologia@scielo.org  
  
COPY . /app  
  
RUN pip install --upgrade pip  
RUN chmod -R 755 /app/*  
  
WORKDIR /app  
  
RUN python setup.py install  
  
RUN chmod +x /app/docker/entrypoint.sh  
  
ENTRYPOINT [ "/app/docker/entrypoint.sh" ]

