FROM stackbrew/ubuntu  
MAINTAINER Spencer Herzberg "spencer.herzberg@gmail.com"  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
  
RUN apt-get update  
RUN apt-get upgrade -y -qq  
  
RUN apt-get install -qq -y \  
python-dev \  
python-pip \  
libmysqlclient-dev  
  
RUN pip install sandman MySQL-python  
  
ADD entrypoint /app/  
  
EXPOSE 5000  
ENTRYPOINT ["/app/entrypoint"]  

