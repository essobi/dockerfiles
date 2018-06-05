FROM fedora:27  
RUN dnf install -y http://resources.ovirt.org/pub/yum-repo/ovirt-release-
master.rpm && \  
useradd analyzer && \  
dnf install -y openssl xz findutils ovirt-log-collector-analyzer  
USER analyzer  
WORKDIR /home/analyzer  
CMD ovirt-log-collector-analyzer /1.tar.xz 2>/dev/null 1>&2 && cat
analyzer_report.html  

