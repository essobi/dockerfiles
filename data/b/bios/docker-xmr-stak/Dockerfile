FROM centos:centos7  
MAINTAINER Tobias Sgoff  
  
RUN yum -y install centos-release-scl epel-release  
RUN yum -y install cmake3 devtoolset-4-gcc* hwloc-devel libmicrohttpd-devel
openssl-devel make git  
  
RUN git clone https://github.com/fireice-uk/xmr-stak.git  
  
ADD install.sh /install.sh  
RUN /install.sh  
  
ENTRYPOINT ["/xmr-stak/bin/xmr-stak"]  

