FROM centos:7  
RUN yum update -y && \  
yum install -y curl &&\  
curl -sSL
https://github.com/oracle/graal/releases/download/vm-1.0.0-rc1/graalvm-
ce-1.0.0-rc1-linux-amd64.tar.gz > /var/tmp/graalvm-ce-1.0.0-rc1-linux-
amd64.tar.gz && \  
cd /var/tmp && tar zxf graalvm-ce-1.0.0-rc1-linux-amd64.tar.gz && \  
mv graalvm-1.0.0-rc1 /var/lib/ && \  
yum clean all  
  
ADD graalvm.sh /etc/profile.d/graalvm.sh  
RUN . /etc/profile  
  
CMD ["bash"]  

