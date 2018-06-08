FROM jdeathe/centos-ssh:centos-7  
MAINTAINER sffxzzp <sffxzzp@126.com>  
RUN yum -y update; yum clean all  
RUN yum -y install yum-utils; yum clean all  
RUN rpm --rebuilddb  
RUN rpm --import
"http://keyserver.ubuntu.com/pks/lookup?op=get&search=0x3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF"  
RUN yum-config-manager --add-repo http://download.mono-
project.com/repo/centos/  
RUN yum -y install mono-complete; yum clean all  
RUN yum -y install screen; yum clean all  
RUN ln -s /usr/lib64/libMonoPosixHelper.so /usr/lib/libMonoPosixHelper.so  
  
EXPOSE 22  
EXPOSE 8989

