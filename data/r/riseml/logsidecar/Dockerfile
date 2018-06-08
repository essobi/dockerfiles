FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG C.UTF-8  
  
RUN apt-get -y update && \  
apt-get -y install python3 python3-dev curl  
  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python3 get-pip.py && \  
rm get-pip.py  
RUN mkdir /app  
COPY requirements.txt /app/requirements.txt  
RUN python3 -m pip install -r /app/requirements.txt  
  
ENV PYTHONPATH /app  
  
COPY . /app  
  
CMD stdbuf -o0 python3 -u /app/log.py

