FROM centos:7.3.1611  
# install dependencies  
RUN yum update -y && \  
yum groupinstall -y "Development Tools" && \  
yum install -y which wget && \  
yum install -y epel-release && \  
yum install -y python-pip python-devel openssl-devel Lmod && \  
# need this for --package to work to generate RPM  
yum install ruby ruby-devel rubygems -y && \  
gem install fpm && \  
  
pip install --upgrade pip && \  
pip install setuptools && \  
pip install easybuild && \  
# need this for git integration with eb  
pip install GitPython python-graph-dot graphviz keyring keyrings.alt  
  
RUN mkdir -p /app/modules/ && \  
mkdir -p /app/software && \  
mkdir -p /scratch/tmp && \  
useradd easybuild && \  
chown easybuild:easybuild -R /app && \  
chown easybuild:easybuild -R /scratch  
  

