FROM centos:centos7  
  
RUN yum -y update  
RUN yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
RUN yum -y install python-pip bind-utils  
  
ADD app /app  
WORKDIR /app  
RUN pip install --upgrade pip && pip install -r requirements.txt  
  
CMD ["python", "run.py"]  

