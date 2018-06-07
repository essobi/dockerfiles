FROM python:2.7  
MAINTAINER Tomas Turek <tturek@redhat.com>  
  
ENV VERSION 2.0.7  
WORKDIR /opt  
  
RUN cd /opt \  
&& git clone -b ${VERSION} \--single-branch git://git.openstack.org/openstack-
infra/jenkins-job-builder \  
&& cd /opt/jenkins-job-builder \  
&& pip install -r requirements.txt \  
&& python setup.py install \  
&& rm -R /opt/jenkins-job-builder  
  
ENTRYPOINT ["/usr/local/bin/jenkins-jobs"]  

