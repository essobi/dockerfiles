FROM centos:6  
MAINTAINER Zhanwei Wang <wangzw@wangzw.org>  
  
COPY install-repo.sh /tmp/install-repo.sh  
COPY install-software.sh /tmp/install-software.sh  
COPY setup-system.sh /tmp/setup-system.sh  
  
RUN /tmp/install-repo.sh  
  
RUN yum install -y man passwd sudo tar which git mlocate links \  
autoconf automake automake14 libtool m4 gcc gcc-c++ bison flex \  
libuuid-devel krb5-devel libgsasl-devel expat-devel libxml2-devel \  
perl-ExtUtils-Embed pam-devel python-devel cmake \  
bzip2-devel openssl-devel fuse-devel readline-devel pstack python-pip \  
apache-maven apache-ivy java-1.7.0-openjdk-devel \  
devtoolset-3-gcc-c++ devtoolset-3-gcc && \  
yum upgrade -y && \  
yum clean all  
  
RUN pip install Glances logutils argparse  
  
RUN /tmp/install-software.sh  
  
RUN /tmp/setup-system.sh  
  
WORKDIR /home/wangzw/  
  
USER wangzw  
CMD bash  

