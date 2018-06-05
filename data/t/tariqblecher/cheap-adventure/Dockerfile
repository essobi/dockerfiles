FROM ubuntu:14.04  
ENV USER root  
RUN apt-get update -y && apt-get install -y \  
python2.7 \  
python-pip \  
  
RUN pip install \  
kliko  
  
ADD src/ /  
  
ADD kliko.yml /  
  
WORKDIR /  
  
CMD python kliko_test.py  
  
  
  

