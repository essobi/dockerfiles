FROM ligo/base:el7  
  
LABEL name="LALSuite Development - Enterprise Linux 7 (CR)" \  
maintainer="Adam Mercer <adam.mercer@ligo.org>" \  
date="20180503" \  
support="Best Effort"  
  
# enable continuous release repository  
RUN yum-config-manager --enable cr  
  
# enable upstream epel  
RUN yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm && \  
yum-config-manager --disable lscsoft-epel  
  
# install any updates  
RUN yum groups mark convert && \  
yum makecache && \  
yum -y update  
  
COPY /environment/.rpmmacros /root/.rpmmacros  
  
# install development tools and git from IUS  
RUN yum -y groups install "Development Tools" && \  
yum -y remove git && \  
yum -y install git2u  
  
# install lalsuite dependencies  
RUN yum -y install ccache \  
glue \  
ligo-gracedb \  
lscsoft-lalsuite-dev  
  
# git-lfs post-install  
RUN git lfs install  
  
# clear package cache  
RUN yum clean all && rm -rf /var/cache/yum  

