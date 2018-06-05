FROM python:2.7  
MAINTAINER Benoit NORRIN <benoit@norrin.fr>  
  
RUN apt-get update && apt-get install -y libevent-dev python-pip && rm -rf
/var/lib/apt/lists/*  
  
RUN pip install boom  
RUN rm -rf /root/.cache/pip/  
  
ENTRYPOINT ["boom"]  

