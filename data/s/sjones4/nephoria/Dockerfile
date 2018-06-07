FROM centos:7  
  
RUN yum -y install epel-release \  
&& yum -y install make gcc git libffi-devel openssl-devel patch \  
python-devel python2-pip readline-devel libyaml-devel \  
&& pip install --upgrade pip setuptools \  
&& cd /root \  
&& git clone --depth 1 https://github.com/eucalyptus/adminapi.git \  
&& cd adminapi \  
&& python setup.py install \  
&& cd /root \  
&& git clone --depth 1 \--branch devel-4.4
https://github.com/sjones4/nephoria.git \  
&& cd nephoria \  
&& python setup.py install \  
&& cd /root \  
&& rm -rf adminapi nephoria \  
&& pip uninstall -y setuptools pip \  
&& yum -y erase make gcc git python-setuptools perl openssl-devel \  
python-devel readline-devel libyaml-devel *-headers patch \  
&& yum -y clean all  
  
ENV PATH=/root/bin:$PATH  
  
ADD [ "nephoria-test.sh", "/root/bin/" ]  
  
RUN chown --recursive root:root /root/bin/*.sh \  
&& chmod 755 /root/bin/*.sh  

