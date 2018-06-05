FROM centos  
  
MAINTAINER tecnologia@scielo.org  
  
RUN yum -y install gcc  
RUN yum -y install epel-release  
RUN yum -y install python-devel  
RUN yum -y install python-pip  
RUN yum -y upgrade python-setuptools  
  
COPY . /app  
  
RUN pip install --upgrade pip  
RUN chmod -R 755 /app/*  
  
WORKDIR /app  
  
RUN python setup.py install

