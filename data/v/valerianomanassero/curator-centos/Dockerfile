FROM centos:7  
MAINTAINER Valeriano Manassero https://github.com/valeriano-manassero  
  
ENV CURATOR_VERSION 5.4.0  
RUN yum -y update && \  
yum clean all && \  
yum -y install cronie  
  
RUN curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py
| python  
  
RUN pip install elasticsearch-curator==${CURATOR_VERSION}  
  
ADD configs/curator.yml /root/.curator/curator.yml  
ADD configs/actions.yml /root/.curator/actions.yml  
  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod 755 /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

