# For travis  
FROM ubuntu:latest  
# Set the locale  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y
locales  
  
RUN locale-gen en_US.UTF-8 &&\  
DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y fontconfig fontconfig-
config  
#libvirt-clients not found?  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libvirt-bin virtinst
qemu-kvm libvirt-daemon libvirt-daemon-system qemu qemu-user wget shellcheck  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y upgrade  
  
RUN modprobe kvm  
RUN lsmod  
  
EXPOSE 16509  
#This didn't work?  
RUN mknod /dev/kvm c 10 232  
  
#Running in a container we can't access the socket?  
RUN echo "listen_tls = 0" >> /etc/libvirt/libvirtd.conf; \  
echo 'listen_tcp = 1' >> /etc/libvirt/libvirtd.conf; \  
echo 'tls_port = "16514"' >> /etc/libvirt/libvirtd.conf; \  
echo 'tcp_port = "16509"' >> /etc/libvirt/libvirtd.conf; \  
echo 'auth_tcp = "none"' >> /etc/libvirt/libvirtd.conf  
  
#RUN whoami  
# root  
#  
#RUN pwd  
# /  
#  
RUN ls -l /dev/  
RUN ls -l /sys/module/  
#RUN cat /sys/module/kvm_amd/parameters/nested  
#RUN cat /sys/module/kvm_intel/parameters/nested  
RUN cat /etc/issue  
  
#setup ability to run kvm/qemu  
VOLUME [ "/sys/fs/cgroup" ]  
#RUN sed -i "/Service/a ExecStartPost=\/bin\/chmod 666 /dev/kvm"
/lib/systemd/system/libvirtd.service  
RUN service libvirt-bin restart  
RUN service qemu-kvm restart  
RUN service libvirt-guests restart  
RUN service virtlogd restart  
RUN service --status-all  
  
RUN mkdir tests  
  
ADD docker-test.sh ./  
  
#ADD /bin/chmod u+x docker-test.sh  
#/bin/chmod no such file or directory  
RUN ["chmod", "+x", "/docker-test.sh"]  
  
#CMD ./docker-test.sh  

