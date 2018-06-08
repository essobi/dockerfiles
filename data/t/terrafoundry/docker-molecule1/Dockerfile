FROM centos  
  
MAINTAINER Adam Dean <adam@terrafoundry.net>  
  
RUN yum -y update  
RUN yum install -y epel-release  
RUN yum install -y python-pip git  
  
RUN pip install --upgrade pip  
RUN pip install docker molecule==1.25.1  
RUN pip uninstall -y backports.functools_lru_cache  
RUN pip install backports.functools_lru_cache  
  
RUN yum-config-manager --add-repo
https://download.docker.com/linux/centos/docker-ce.repo  
RUN yum install -y docker-ce  
  
ENTRYPOINT ["molecule"]  

