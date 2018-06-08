FROM centos:centos7  
MAINTAINER The CentOS Project <cloud-ops@centos.org>  
  
RUN yum -y update; yum clean all  
RUN yum -y install epel-release; yum clean all  
RUN yum -y install python-pip; yum clean all  
RUN yum -y install libxml2 libxml2-devel libxslt libxslt-devel python-devel
libffi-devel openssl-devel gcc  
RUN pip install python-novaclient  
RUN pip install python-neutronclient  
RUN pip install python-cinderclient  
RUN pip install python-keystoneclient  
RUN pip install python-swiftclient  
RUN pip install python-glanceclient  
RUN pip install python-troveclient  
RUN pip install python-designateclient  

