FROM ubuntu:14.04  
MAINTAINER rocky wang <rocky.wang@finisar.com>  
  
RUN sudo apt-get update && apt-get install -y python  
RUN sudo apt-get install -y python-pip  
RUN sudo pip install django==1.8.13  
  
RUN sudo apt-get install -y python-lxml  
RUN sudo pip install python-ntlm  
RUN sudo apt-get install -y tdsodbc unixodbc  
RUN sudo pip install pypyodbc  
  
COPY freetds.conf /etc/freetds/  
COPY odbcinst.ini /etc/  
  
EXPOSE 8000  
#CMD ["python", "/website/WebEther/manage.py","runserver","0.0.0.0:8000"]

