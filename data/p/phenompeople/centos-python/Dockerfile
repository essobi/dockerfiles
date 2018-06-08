#Base image  
FROM centos:7.4.1708  
LABEL maintainer="rajesh.jonnalagadda@phenompeople.com"  
ENV container docker  
RUN useradd -d /opt/deployment -u 1000 phenom && \  
yum install -q -e 0 -y wget make gcc-c++ openssl-devel sqlite-devel zlib-devel
bzip2-devel && \  
mkdir -p /opt/deployment/scripts  
  
ARG PYTHON_VERSION=3.6.3  
ARG PYTHON_PIP_VERSION=9.0.1  
ENV PYTHON_VERSION=${PYTHON_VERSION} \  
PYTHON_PIP_VERSION=${PYTHON_PIP_VERSION} \  
SETUP_DIRECTORY=/opt/python/cache  
ADD setup /opt/deployment/scripts  
RUN /opt/deployment/scripts/install.sh && \  
yum clean all && \  
rm -rf /opt/deployment/scripts && \  
rm -rf /opt/python/cache/sources/Python-${PYTHON_VERSION}.tgz  
ADD requirements.txt /  
RUN pip3 install -q -r requirements.txt  
RUN python3 -m spacy download en_core_web_lg  
RUN python3 -m spacy download en_core_web_sm  
RUN python3 -m spacy download en_core_web_md

