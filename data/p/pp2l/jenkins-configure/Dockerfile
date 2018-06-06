FROM centos:centos7  
  
ENV JENKINS_USERNAME admin  
ENV JENKINS_PASSWORD password  
ENV JENKINS_URL http://127.0.0.1:8080  
RUN yum install -y git libyaml-devel python-devel python-setuptools \  
&& yum clean all  
RUN easy_install pip==8.0.2  
RUN pip install --no-cache-dir PyYAML python-jenkins jenkins-job-builder  
  
RUN mkdir -p /opt/src  
VOLUME /opt/src  
  
ADD bin/jenkins-configure /usr/bin/jenkins-configure  
  
WORKDIR /opt/src  
  
ENTRYPOINT ["jenkins-configure"]  
  

