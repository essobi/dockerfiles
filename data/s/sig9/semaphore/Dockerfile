FROM centos:7.4.1708  
ENV WAITFORIT_VERSION="2.1.0"  
ENV SEMAPHORE_VERSION="2.4.1"  
LABEL name="Ansible Semaphore" version=$SEMAPHORE_VERSION  
  
ADD files/ /  
ADD
https://github.com/maxcnunes/waitforit/releases/download/v$WAITFORIT_VERSION/waitforit-
linux_amd64 /waitforit  
  
RUN chmod a+x /waitforit \  
&& yum -y update \  
&& yum -y install gcc git python-devel wget \  
&& curl -L https://bootstrap.pypa.io/get-pip.py | python \  
&& pip install ansible pysphere \  
&& wget https://github.com/ansible-
semaphore/semaphore/releases/download/v$SEMAPHORE_VERSION/semaphore_linux_amd64
\  
&& mv semaphore_linux_amd64 /usr/bin/semaphore \  
&& chmod a+x /usr/bin/semaphore \  
&& mkdir -p /opt/semaphore  
  
EXPOSE 3000  
WORKDIR /opt/semaphore  
  
# Default Command  
CMD ["/bin/bash", "-c", "/var/lib/semaphore/start.sh"]  

