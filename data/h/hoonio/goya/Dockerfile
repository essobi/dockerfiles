FROM ubuntu:xenial  
COPY . /app  
WORKDIR /app  
  
RUN apt-get update -y && \  
apt-get install -y python-pip python-dev build-essential && \  
pip install --upgrade pip && \  
pip install -r requirements.txt  
  
EXPOSE 8080  
ENTRYPOINT ["python"]  
CMD ["app.py"]  

