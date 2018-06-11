FROM centos:7  
RUN yum install -y epel-release  
RUN rpmkeys --import file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7  
RUN yum install -y --setopt=tsflags=nodocs bind-utils gettext iproute v8314
mongodb24-mongodb mongodb24  
RUN yum -y clean all  
  
LABEL imagesize=naive  

