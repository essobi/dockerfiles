FROM python:3.6-slim  
ADD . /dusite  
WORKDIR /dusite  
RUN pip install -r requirements.txt  
EXPOSE 8000  
CMD ["./docker-entrypoint.sh"]  

