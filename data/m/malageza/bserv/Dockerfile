FROM ubuntu:16.04  
#FROM armv7/armhf-ubuntu:16.04  
MAINTAINER Malasits Geza: 0.1  
RUN apt-get update && apt-get install -y python3-pip && apt-get clean && rm
-rf /var/lib/apt/lists/*  
ADD ./static /opt/backups  
ADD ./static /opt/static  
ADD ./templates /opt/templates  
ADD bserv2.py /opt  
ADD requirements.txt /opt  
  
RUN pip3 install -r /opt/requirements.txt  
WORKDIR /opt  
  
EXPOSE 53535  
VOLUME ["/opt/backups"]  
  
CMD ["python3","bserv2.py"]  

