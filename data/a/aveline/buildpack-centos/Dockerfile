FROM centos:centos7  
  
RUN yum makecache && \  
yum groupinstall -y "Development Tools" && \  
yum install -y gcc-c++ patch readline readline-devel zlib zlib-devel libyaml-
devel libffi-devel openssl-devel make bzip2 autoconf automake libtool bison
iconv-devel tar which  
  
ADD install.bash /install.bash  
  
RUN /install.bash  
  
ADD run.bash /run.bash  
  
VOLUME ["/build"]  
ENTRYPOINT ["/bin/bash", "-l"]  
CMD ["-c", "/run.bash"]  

