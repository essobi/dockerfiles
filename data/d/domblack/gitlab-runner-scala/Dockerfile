FROM domblack/scala:latest  
  
LABEL maintainer "thephenix@gmail.com"  
  
COPY install_protobuf.sh /  
  
RUN yum install -y graphviz.x86_64 rpm-build.x86_64 wget curl which gcc
gcc-c++ make git \  
&& /install_protobuf.sh \  
&& curl --silent --location https://rpm.nodesource.com/setup_6.x | bash - \  
&& yum -y install nodejs \  
&& yum clean all \  
&& rm -fR /tmp/*

