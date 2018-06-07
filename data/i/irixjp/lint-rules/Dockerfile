FROM centos:7  
ENV container docker  
  
ENV ANSIBLE_VERSION 2.4.2.0  
ENV LINT_VERSION 3.4.21  
ENV PYTHON_DOCKER_PY_VERSION 1.10.6  
ENV DOCKER_CLIENT_VERSION 1.13.1  
RUN yum install -y epel-release && \  
yum install -y git && \  
yum install -y ansible-${ANSIBLE_VERSION:?} && \  
yum install -y ansible-lint-${LINT_VERSION:?} && \  
yum install -y python-docker-py-${PYTHON_DOCKER_PY_VERSION:?} docker-
client-${DOCKER_CLIENT_VERSION:?} && \  
yum clean all  

