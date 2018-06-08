FROM ubuntu:latest  
  
MAINTAINER Roberto Previtera <roberto.previtera@gmail.com>  
  
RUN apt-get update  
RUN apt-get -y install python-pip python-dev  
  
RUN pip install Flask  
RUN pip install flask-cors  
  
RUN mkdir /appl \  
mkdir /appl/api_vdc  
  
COPY . /appl/api_vdc  
  
EXPOSE 5000  
CMD ["python", "/appl/api_vdc/api.py"]  

