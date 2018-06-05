FROM centos:centos7  
RUN yum update -y && yum install -y wget  
RUN rpm --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro  
RUN rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-
release-0-1.el7.nux.noarch.rpm  
RUN yum update -y && yum install -y alien  
RUN wget -O eatmydata.deb
http://mirrors.kernel.org/ubuntu/pool/main/libe/libeatmydata/eatmydata_26-2_i386.deb  
RUN alien -r eatmydata.deb  
  

