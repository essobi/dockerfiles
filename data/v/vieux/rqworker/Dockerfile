FROM ubuntu:14.04  
MAINTAINER Victor Vieux <victor@vieux.fr>  
  
RUN echo 'deb http://archive.ubuntu.com/ubuntu precise main universe' >
/etc/apt/sources.list  
RUN apt-get update && apt-get upgrade -y && apt-get clean  
  
RUN apt-get install -y python-pip  
  
RUN pip install rq  
  
ENTRYPOINT ["rqworker"]

