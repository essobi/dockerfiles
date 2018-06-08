#  
# Docker image for graph-tool server  
#  
# implement graph processing web API.  
#  
FROM ubuntu:xenial  
MAINTAINER Keiichiro Ono <kono@ucsd.edu>  
  
RUN apt-get update && apt-get install -y apt-transport-https python-pip  
RUN pip install --upgrade pip  
RUN pip install flask flask-restful twisted  
  
# For installing graph-tool  
RUN mkdir /graph-tool  
WORKDIR /graph-tool  
ADD . /graph-tool  
  
RUN echo "deb http://downloads.skewed.de/apt/xenial xenial universe"
>>/etc/apt/sources.list  
RUN echo "deb-src http://downloads.skewed.de/apt/xenial xenial universe"
>>/etc/apt/sources.list  
  
RUN apt-key adv --keyserver pgp.skewed.de --recv-key 612DEFB798507F25  
  
# Install OS-level packages and misc. tools  
RUN apt-get update  
RUN apt-get install -y python-graph-tool  
  
# Add directory for REST API server code  
RUN mkdir /app  
WORKDIR /app  
  
ADD . /app  
RUN mkdir /app/images  
  
EXPOSE 5000  
RUN python --version  
# Run API server  
CMD ["python", "api/api.py"]  
#CMD ["twistd", "-n", "web", "--port", "5000", "--wsgi", "api/api.py"]

