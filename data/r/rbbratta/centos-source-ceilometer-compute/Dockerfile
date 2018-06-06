FROM rbbratta/centos-source-ceilometer-base:2.3.20161011  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
  
RUN yum -y install \  
libvirt-devel \  
&& yum clean all  
  
  
  
RUN /var/lib/kolla/venv/bin/pip \--no-cache-dir install --upgrade -c
requirements/upper-constraints.txt libvirt-python  
  
  
  
  
  
  
  
# NOTE(huikang): non-root user does not work with libvirt.sock.  
# Need configuration in nova-libvirt container to allow  
# USER ceilometer to access libvirt.sock

