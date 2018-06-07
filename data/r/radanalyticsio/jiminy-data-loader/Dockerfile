FROM centos:latest  
  
COPY * /opt/data-loader/  
  
WORKDIR /opt/data-loader  
  
RUN yum -y install epel-release && \  
yum -y install python-pip && \  
yum clean all  
  
RUN pip install -r requirements.txt  
  
CMD ["python", "app.py"]  

