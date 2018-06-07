FROM ubuntu:latest  
MAINTAINER Vineet Ghatge "vgh4uster@gmail.com"  
RUN apt-get update -y  
RUN apt-get install -y python-pip python-dev build-essential  
COPY . /testapp  
WORKDIR /testapp  
RUN pip install -r requirements.txt  
ENTRYPOINT ["python"]  
CMD ["flask_demo.py"]  

