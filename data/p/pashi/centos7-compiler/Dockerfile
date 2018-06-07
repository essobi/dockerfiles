FROM centos:centos7  
MAINTAINER Pasi Lammi <pasi.lammi@iki.fi>  
  
RUN yum clean all  
RUN yum -y groupinstall "Development tools"  
RUN yum grouplist hidden  
  
RUN yum -y install sudo git  
RUN echo 'build NOPASSWD: ALL=(ALL)' >> /etc/sudoers  
RUN useradd -m -u 12435 build  
RUN mkdir -p /home/build/rpmbuild/{SRPMS,RPMS,BUILD,BUILDROOT} /work  
RUN chown -R build /home/build/rpmbuild/  
RUN ln -s /work/SOURCES /home/build/rpmbuild/SOURCES  
RUN ln -s /work/SPECS /home/build/rpmbuild/SPECS  
WORKDIR /home/build/rpmbuild  
  
USER build  
RUN ["/bin/bash"]  

