FROM ubuntu  
MAINTAINER Roger Stark "rho.ajax@gmail.com"  
RUN apt-get update -y  
RUN apt-get -y install libgsl-dev libopenblas-dev liblapacke-dev  
RUN apt-get -y install python-pip python-dev build-essential imagemagick  
COPY . /app  
WORKDIR /app  
RUN pip install -r requirements.txt  
  
ENTRYPOINT ["python"]  
CMD ["app.py"]  
  

