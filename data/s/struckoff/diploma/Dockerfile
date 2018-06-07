FROM ubuntu:14.04  
MAINTAINER Alexey Struckov <struckov@protonmail.com>  
RUN apt-get update  
RUN apt-get install -y nginx nodejs python python-pip build-essential  
COPY . /app  
WORKDIR /app  
RUN pip install -r requirements.txt  
ENTRYPOINT ["python"]  
CMD ["main.py"]  

