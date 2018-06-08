FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y \  
libblas-dev \  
libatlas-base-dev \  
gfortran \  
python3-pip  
  
RUN apt-get -y build-dep python3-scipy  
  
RUN pip3 install virtualenv  
  
RUN mkdir myapp  
RUN cd myapp && \  
virtualenv -p /usr/bin/python3.5 .env  
  
ADD requirements.txt /myapp  
  
RUN cd /myapp && \  
.env/bin/pip install -r requirements.txt  
  

