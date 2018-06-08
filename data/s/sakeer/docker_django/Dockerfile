FROM sakeer/ubuntu:version-3  
FROM mysql  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN apt-get update && apt-get install -y \  
python \  
python-dev \  
python-pip \  
python-virtualenv && \  
rm -rf /var/lib/apt/lists/*  
  
ENV PYTHONUNBUFFERED 1  
RUN mkdir /docker_django  
WORKDIR /docker_django  
ADD requirements.txt /docker_django/  
RUN pip install -r requirements.txt  
ADD . /docker_django/  

