FROM python:3.6.0  
LABEL maintainer "Ryan Desfosses <ryan@desfo.org>"  
RUN pip install --upgrade pip  
  
RUN pip install scrapy pymongo  
  
RUN groupadd -g 1000 user && \  
useradd -m -g user -u 1000 user  
  
USER user  
WORKDIR /home/user  
  

