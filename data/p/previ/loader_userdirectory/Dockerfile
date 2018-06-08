FROM ubuntu:latest  
  
MAINTAINER Roberto Previtera <roberto.previtera@gmail.com>  
  
RUN apt-get update  
RUN apt-get -y install curl unzip python-dev  
  
RUN mkdir /appl && \  
mkdir /appl/loader_userdirectory  
  
COPY . /appl/loader_userdirectory  
  
WORKDIR /appl/loader_userdirectory  
  
CMD ["python", "/appl/loader_userdirectory/loader.py"]  

