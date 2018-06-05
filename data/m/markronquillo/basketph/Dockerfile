FROM ubuntu:14.04  
MAINTAINER Mark Joseph Ronquillo, markronquillo23@gmail.com  
  
RUN apt-get -yqq update  
RUN apt-get -yqq install python-pip python-dev  
  
ADD basketph /var/www/basketph  
WORKDIR /var/www/basketph  
  
# INSTALL DEPENDENCIES  
RUN pip install -r requirements.txt  
  
EXPOSE 8000  
CMD ["python", "./manage.py", "migrate"]  
CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]  
  

