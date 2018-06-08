FROM centos:7  
RUN yum groupinstall -y 'Development Tools' && yum clean -y all  
RUN mkdir -p /rpmbuild/{SPEC,SOURCES,RPMS,SRPMS,BUILD,BUILDROOT}  
ADD build.py /usr/local/sbin/  
VOLUME /rpmbuild  
ENTRYPOINT ["build.py"]  
  

