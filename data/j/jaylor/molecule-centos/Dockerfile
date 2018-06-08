FROM centos:7.4.1708  
  
COPY ./requirements.txt /requirements.txt  
  
RUN set -ex; \  
\  
yum install -y epel-release; \  
yum install -y \  
gcc python-pip python-devel openssl-devel docker \  
&& yum clean all; \  
rm -rf /var/cache/yum ; \  
pip install \--no-cache-dir -r /requirements.txt  

