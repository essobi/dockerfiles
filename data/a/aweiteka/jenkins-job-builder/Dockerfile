FROM centos:centos7  
  
MAINTAINER Aaron Weitekamp <aweiteka@redhat.com>  
  
RUN echo -e
"[epel]\nname=epel\nenabled=1\nbaseurl=https://dl.fedoraproject.org/pub/epel/7/x86_64/\ngpgcheck=0"
> /etc/yum.repos.d/epel.repo  
  
RUN yum install -y --setopt=tsflags=nodocs python-pip gcc git && \  
# pip install jenkins-job-builder && \  
yum clean all  
  
RUN git clone https://git.openstack.org/openstack-infra/jenkins-job-builder
/opt/jenkins-job-builder  
  
WORKDIR /opt/jenkins-job-builder  
  
RUN python setup.py install && \  
# install from source doesn't install python 'six'  
pip install -r /opt/jenkins-job-builder/requirements.txt  
  
WORKDIR /jjb  
  
LABEL RUN="docker run -it --rm -v `pwd`:/jjb:Z --net=host --name NAME -e
NAME=NAME -e IMAGE=IMAGE IMAGE  
  
ENTRYPOINT ["/usr/bin/jenkins-jobs"]  
CMD ["\--conf", "config/jenkins-jobs.ini", "\--ignore-cache", \  
"update", "jenkins-jobs.yaml"]  
  

