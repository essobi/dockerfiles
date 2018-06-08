FROM centos:7.2.1511  
LABEL maintainer.name=GiuseppaMuscianisi
maintainer.email=g.muscianisi@cineca.it  
  
RUN yum -y install perl atlas libpsm2 libibverbs qperf pciutils tcl tcsh \  
expect sysfsutils librdmacm libibcm perftest rdma bc \  
elfutils-libelf-developenssh-clients openssh-server \  
libstdc++-devel gcc-gfortran rpm-buildx \  
compat-rdma-devel libibmad libibumad ibacm-devel \  
libibumad-devel libibumad-static libuuid-devel \  
pci-utils iproute net-tools \  
libhfi1 opensm-libs numactl-libs \  
infinipath-psm elfutils-libelf-devel irqbalance \  
papi libibumad openssl tar vim wget && \  
yum clean all  
  
  
RUN mkdir /tmpdir && cd /tmpdir && \  
wget
https://gitlab.hpc.cineca.it/container_data_example/data_example/raw/master/mpi_marconi/intelopa/IntelOPA-
Basic.RHEL72-x86_64.10.5.0.0.155.tgz && \  
wget
https://gitlab.hpc.cineca.it/container_data_example/data_example/raw/master/mpi_marconi/intelopa/modified_installation_scripts.tgz
&& \  
tar -xvf modified_installation_scripts.tgz && \  
tar -xvf IntelOPA-Basic.RHEL72-x86_64.10.5.0.0.155.tgz && \  
cd IntelOPA-Basic.RHEL72-x86_64.10.5.0.0.155 && \  
cp INSTALL INSTALL_original && \  
cp /tmpdir/modified_installation_scripts/modified_scripts/INSTALL_main_dir
INSTALL && \  
cp IntelOPA-Tools.RHEL72-x86_64.10.5.0.0.140/comp.pl IntelOPA-
Tools.RHEL72-x86_64.10.5.0.0.140/comp.pl_original && \  
cp /tmpdir/modified_installation_scripts/modified_scripts/comp.pl_tool_140
IntelOPA-Tools.RHEL72-x86_64.10.5.0.0.140/comp.pl && \  
cp IntelOPA-OFED_DELTA.RHEL72-x86_64.10.5.0.0.159/comp.pl IntelOPA-
OFED_DELTA.RHEL72-x86_64.10.5.0.0.159/comp.pl_original && \  
cp
/tmpdir/modified_installation_scripts/modified_scripts/comp.pl_ofed_delta_159
IntelOPA-OFED_DELTA.RHEL72-x86_64.10.5.0.0.159/comp.pl && \  
./INSTALL --user-space -n  
  
CMD ["/bin/bash"]  

