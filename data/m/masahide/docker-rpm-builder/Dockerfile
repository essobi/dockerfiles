FROM amazonlinux:1  
  
RUN yum groupinstall -y "Development Tools" \  
&& yum install -y rpmdevtools asciidoc hmaccalc perl-ExtUtils-Embed pesign
xmlto audit-libs-devel binutils-devel elfutils-devel elfutils-libelf-devel
ncurses-devel newt-devel numactl-devel pciutils-devel python-devel zlib-devel
rpm-build patchutils openssl-devel kernel-devel net-tools bc gtk2-devel
systemtap-sdt-devel git rpm-sign \  
&& yum clean all  
  

