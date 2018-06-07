FROM centos:7.3.1611  
  
ADD [ "build-*.sh", "rpm-*.sh", "/root/bin/" ]  
  
ENV PATH=/root/bin:$PATH \  
RPM_OUT="/eucalyptus/rpms"  
  
RUN chown --recursive root:root /root/bin/*.sh \  
&& chmod 755 /root/bin/*.sh \  
&& mkdir --parents /eucalyptus \  
&& chown --recursive root:root /eucalyptus \  
&& build-all-rpms-44.sh setupenv \  
&& build-eucalyptus-cloud-libs-rpm.sh setup \  
&& build-eucalyptus-rpms.sh setup \  
&& build-eucalyptus-selinux-rpm.sh setup \  
&& build-eucalyptus-console-rpm.sh setup \  
&& build-eucalyptus-console-selinux-rpm.sh setup \  
&& build-eucalyptus-sim-imaging-worker-rpm.sh setup \  
&& build-eucalyptus-sim-load-balancer-servo-rpm.sh setup \  
&& build-eucalyptus-service-image-rpm.sh setup \  
&& build-eucalyptus-sosreport-plugins-rpm.sh setup \  
&& build-eucalyptus-release-rpm.sh setup \  
&& build-euca2ools-release-rpm.sh setup \  
&& sed --in-place "s/^#user =/user =/" /etc/libvirt/qemu.conf \  
&& sed --in-place "s/^#group =/group =/" /etc/libvirt/qemu.conf \  
&& yum -y install curl gnupg2 rpm-sign which yajl \  
&& yum -y clean all  
  
VOLUME /eucalyptus  
WORKDIR /eucalyptus  
  

