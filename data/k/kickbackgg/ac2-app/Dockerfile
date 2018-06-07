FROM centos:7.2.1511  
RUN yum install -y yum-utils  
RUN rpm --import
"http://keyserver.ubuntu.com/pks/lookup?op=get&search=0x3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF"  
RUN yum-config-manager --add-repo http://download.mono-
project.com/repo/centos/  
  
RUN yum -y clean all  
RUN yum -y install yum-plugin-ovl  
RUN yum -y update  
RUN yum install -y mono-complete  
RUN yum group install -y "Development Tools"  
  
RUN yum install -y epel-release  
RUN yum install -y git  
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" && python get-
pip.py  
RUN yum install -y pypy  
RUN yum install -y python-crypto  
  
ADD docker_deploy /tmp/docker_deploy  
ADD docker_bsp_parser /tmp/docker_bsp_parser  
  
ADD start.sh /start  
  
CMD /start  

