FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update && \  
apt-get -y install python3 python3-dev curl  
  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python3 get-pip.py && \  
rm get-pip.py  
COPY requirements.lock /app/requirements.lock  
RUN python3 -m pip install -r /app/requirements.lock  
  
ENV PORT 3000  
ENV PYTHONPATH /app  
ENV DEBUG 0  
  
COPY . /app  
WORKDIR /app  
  
CMD python3 start_scheduler.py  

