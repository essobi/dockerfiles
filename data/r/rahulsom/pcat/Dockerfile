FROM python:alpine  
MAINTAINER Rahul Somasunderam <rahul.som@gmail.com>  
  
RUN pip install pygments  
  
VOLUME ["/local"]  
WORKDIR /local  
ENTRYPOINT ["pygmentize", "-g"]  

