FROM python:2.7.11  
MAINTAINER Masashi Kurita <marty.marron@gmail.com>  
  
USER root  
RUN apt-get update  
  
RUN pip install --upgrade pip  
RUN pip install argparse ordereddict PyYAML python-jenkins  
RUN pip install git+https://git.openstack.org/openstack-infra/jenkins-job-
builder  
  
RUN mkdir /home/jenkins_jobs && \  
groupadd jenkins_jobs && \  
useradd -g jenkins_jobs -d /home/jenkins_jobs jenkins_jobs && \  
chown -R jenkins_jobs:jenkins_jobs /home/jenkins_jobs  
  
RUN mkdir -m 0755 /etc/jenkins_jobs && \  
chown -R jenkins_jobs:jenkins_jobs /etc/jenkins_jobs  
  
USER jenkins_jobs  
WORKDIR /home/jenkins_jobs  
  
ENTRYPOINT ["jenkins-jobs"]  
  
CMD ["--help"]

