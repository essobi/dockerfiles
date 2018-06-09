FROM ubuntu:latest  
  
RUN apt-get update -y  
RUN apt-get install -y python-pip python-dev build-essential  
COPY hello.py requirements.txt /app/  
WORKDIR /app  
RUN pip install -r requirements.txt  
ENTRYPOINT ["python"]  
CMD ["hello.py"]  

