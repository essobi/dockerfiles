FROM ubuntu:latest  
  
ENV LANG C.UTF-8  
ADD install.sh /tmp/install.sh  
RUN sh /tmp/install.sh  
  
ENV PYTHONUNBUFFERED 1  
RUN pip3 install --upgrade pip  
ADD requirements.txt /tmp/requirements.txt  
RUN pip3 install -r /tmp/requirements.txt  

