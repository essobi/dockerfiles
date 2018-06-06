FROM python:3.5  
ENV PYTHONUNBUFFERED 1  
RUN mkdir /code  
WORKDIR /code  
ADD requirements.txt /code/  
RUN pip install -r requirements.txt  
ADD . /code/  
  
RUN mkdir -p /srv/logs  
  
EXPOSE 8000  
CMD ["./docker-entrypoint.sh"]  
  

