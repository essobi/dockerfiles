FROM centos:7  
MAINTAINER Anderson Santos anderson@gruponeuro.c  
  
RUN yum -y update && yum install git sudo -y  
RUN git clone https://github.com/apache/ambari /root/ambari  
  
# Installing pip and dependencies  
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "/root/get-pip.py"  
RUN python /root/get-pip.py  
RUN pip install coverage Jinja2 mock coveralls  
  
# Exporting the needed paths (/lib/python2.7/site-packages:)  
ENV AMBARIPYTHON=/root/ambari/ambari-common/src/main/python  
ENV PYTHONPATH=$AMBARIPYTHON:$AMBARIPYTHON/ambari_jinja2  
ENV PATH=$PATH:/root/ambari/ambari-agent/conf/unix  
  
VOLUME /app  
WORKDIR /app

