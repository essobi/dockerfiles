# DOCKER-VERSION 1.1.0  
#inherit from the base container, which have all the needed script to launch
tasks  
FROM ingi/inginious-c-base  
LABEL org.inginious.grading.name="mono"  
  
RUN rpm --import
"http://keyserver.ubuntu.com/pks/lookup?op=get&search=0x3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF"
&& \  
yum install -y yum-utils && \  
yum-config-manager --add-repo http://download.mono-project.com/repo/centos/ &&
\  
yum install -y mono-complete && \  
yum clean all  

