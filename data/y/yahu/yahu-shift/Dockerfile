FROM openshift/base-centos7  
MAINTAINER NGINX Docker Maintainers "docker-maint@nginx.com"  
USER root  
  
RUN yum -y install wget curl zip epel-release  
  
RUN yum -y install python \  
python-devel \  
python-pip \  
mercurial  
  
RUN pip install --upgrade pip && yum clean all  
  
# Install dev cron  
RUN pip install -e hg+https://bitbucket.org/dbenamy/devcron#egg=devcron  
  
ADD ./etc/crontab /cron/crontab  
ADD ./etc/yahu.sh /yahu.sh  
RUN chmod 777 /yahu.sh  
  
EXPOSE 22  
USER 1001  
CMD ["devcron.py", "/cron/crontab"]  

