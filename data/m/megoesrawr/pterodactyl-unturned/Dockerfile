FROM centos:centos7  
  
MAINTAINER Isaac A, <isaac@isaacs.site>  
  
RUN yum update -y && \  
yum upgrade -y && \  
rpm --import
"http://keyserver.ubuntu.com/pks/lookup?op=get&search=0x3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF"
&& \  
yum-config-manager --add-repo http://download.mono-project.com/repo/centos-
beta/ && \  
yum repolist && \  
yum -y install deltarpm yum-utils && \  
yum -y install glibc libstdc++ glibc.i686 libstdc++.i686 glibc.i686
libstdc++.i686 ca-certificates mesa-libGL mesa-libGL-devel libXcursor
libXrandr-devel gcc-c++ kernel-devel unzip mono-devel && \  
useradd -d /home/container -m container  
  
USER root  
ENV USER root  
ENV HOME /home/container  
  
VOLUME /lib  
VOLUME /lib64  
  
WORKDIR /home/container  
  
COPY ./entrypoint.sh /entrypoint.sh  
  
CMD ["/bin/bash", "/entrypoint.sh"]  

