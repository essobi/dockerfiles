FROM centos:centos7  
  
RUN yum install -y epel-release  
RUN yum install -y git python-pip  
RUN pip install shutit  
  
WORKDIR /opt  
# Change the next two lines to build your ShutIt module.  
RUN git clone https://github.com/ianmiell/shutit-airflow.git  
WORKDIR /opt/shutit-airflow  
RUN shutit build --delivery dockerfile  
  
CMD ["/bin/bash"]  

