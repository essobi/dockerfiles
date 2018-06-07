FROM centos:latest  
MAINTAINER Kostiantyn Iarovyi <kiarovyi@cisco.com>  
RUN yum -y install epel-release && yum -y install python-pip && pip install
--upgrade pip && pip install requests docopt  
COPY kube2pyconsul.py /kube2pyconsul.py  
WORKDIR /  
ENTRYPOINT ["python", "/kube2pyconsul.py"]

