FROM fedora:21  
RUN yum groupinstall -y 'Development Tools' && \  
yum install -y rpm-build && \  
yum clean -y all  
RUN mkdir -p /rpmbuild/{SPEC,SOURCES,RPMS,SRPMS,BUILD,BUILDROOT}  
ADD build.py /usr/local/sbin/  
VOLUME /rpmbuild  
ENTRYPOINT ["build.py"]  
  

