FROM python:3.5.2  
MAINTAINER tecnologia@scielo.org  
  
RUN apt-get update && apt-get install -y supervisor  
RUN mkdir -p /var/log/supervisor  
RUN apt-get install -y vsftpd ftp  
  
COPY . /app  
COPY requirements.txt /app/requirements.txt  
COPY docker/entrypoint.sh /app/docker/entrypoint.sh  
COPY docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
WORKDIR /app  
  
RUN pip install -r requirements.txt  
  
RUN python setup.py install  
  
ADD docker/entrypoint.sh /app/docker/entrypoint.sh  
RUN chmod +x /app/docker/entrypoint.sh  
  
ENTRYPOINT [ "/app/docker/entrypoint.sh" ]

