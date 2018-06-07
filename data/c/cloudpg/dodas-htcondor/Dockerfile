FROM cloudpg/centos-7-grid-tini-sshd  
  
WORKDIR /etc/yum.repos.d  
  
RUN useradd -ms /bin/bash condor \  
&& wget http://research.cs.wisc.edu/htcondor/yum/repo.d/htcondor-development-
rhel7.repo \  
&& wget http://research.cs.wisc.edu/htcondor/yum/repo.d/htcondor-stable-
rhel7.repo \  
&& wget http://research.cs.wisc.edu/htcondor/yum/RPM-GPG-KEY-HTCondor \  
&& rpm --import RPM-GPG-KEY-HTCondor \  
&& yum --setopt=tsflags=nodocs -y update \  
&& yum --setopt=tsflags=nodocs -y install condor-all python-devel python-pip \  
&& yum --setopt=tsflags=nodocs -y install binutils \  
boost-devel \  
cmake \  
curl \  
cvs \  
emacs \  
freetype \  
freetype-devel \  
fuse \  
gcc \  
gcc-c++ \  
gcc-gfortran \  
git \  
glibc-devel \  
glibc-headers \  
gsl-devel \  
initscripts \  
krb5-workstation \  
libSM \  
libX11-devel \  
libXext \  
libXext-devel \  
libXft-devel \  
libXpm \  
libXpm-devel \  
make \  
man \  
nano \  
ncurses \  
ncurses-devel \  
openssh-clients \  
openssh-server \  
openssl098e \  
pam-krb5 \  
screen \  
subversion \  
sudo \  
vim \  
&& yum clean all \  
&& pip install --upgrade pip setuptools \  
&& pip install j2cli paramiko psutil kazoo requests \  
&& systemctl disable condor  
  
# Root home  
WORKDIR /root  
  
# condor_collector  
EXPOSE 9618  
# condor_negotiator  
EXPOSE 9614  
# condor_ckpt_server  
EXPOSE 5651-5654  
# condor_ports  
EXPOSE 1024-2048  
# condor env default values  
ENV CONDOR_DAEMON_LIST="COLLECTOR, MASTER, NEGOTIATOR, SCHEDD, STARTD"  
ENV CONDOR_HOST="\$(FULL_HOSTNAME)"  
ENV CCB_ADDRESS_STRING=""  
ENV NETWORK_INTERFACE_STRING=""  
ENV CONDOR_SCHEDD_SSH_PORT=31042  
ENV TUNNEL_FROM="UNDEFINED"  
ENV TUNNEL_TO="UNDEFINED"  
ENV SEC_DAEMON_AUTHENTICATION_METHODS=CLAIMTOBE  
ENV SEC_CLIENT_AUTHENTICATION_METHODS=CLAIMTOBE  
ENV SEC_NEGOTIATOR_AUTHENTICATION_METHODS=CLAIMTOBE  
ENV SEC_ADVERTISE_STARTD_AUTHENTICATION_METHODS=CLAIMTOBE  
ENV NUM_SLOTS=1  
ENV NUM_SLOTS_TYPE_1=1  
ENV SLOT_TYPE_1="cpus=1, mem=4096"  
ENV FLOCK_FROM=""  
ENV FLOCK_TO=""  
ENV FLOCK_TO_COL_NEG=""  
ENV HOST_ALLOW_FLOCK=""  
RUN mkdir -p /opt/dodas/htc_config \  
&& mkdir -p /opt/dodas/fs_remote_dir \  
&& mkdir -p /opt/dodas/health_checks \  
&& mkdir -p /etc/skel/.ssh  
COPY condor.sh /opt/dodas/  
COPY ./health_checks/check_condor_processes.py /opt/dodas/health_checks/  
COPY ./health_checks/check_cvmfs_folders.py /opt/dodas/health_checks/  
COPY ./health_checks/check_ssh_server.py /opt/dodas/health_checks/  
COPY ./health_checks/check_condor_master_ip.sh /opt/dodas/health_checks/  
COPY ./health_checks/check_condor_schedd_tunnel.sh /opt/dodas/health_checks/  
COPY cache.py /opt/dodas/  
COPY ./config/condor_config.template /opt/dodas/htc_config/  
  
RUN ln -s /opt/dodas/condor.sh /usr/local/sbin/dodas_condor \  
&& ln -s /opt/dodas/health_checks/check_condor_processes.py
/usr/local/sbin/dodas_check_condor_processes \  
&& ln -s /opt/dodas/health_checks/check_cvmfs_folders.py
/usr/local/sbin/dodas_check_cvmfs_folders \  
&& ln -s /opt/dodas/health_checks/check_ssh_server.py
/usr/local/sbin/dodas_check_ssh_server \  
&& ln -s /opt/dodas/health_checks/check_condor_master_ip.sh
/usr/local/sbin/dodas_check_condor_master_ip \  
&& ln -s /opt/dodas/health_checks/check_condor_schedd_tunnel.sh
/usr/local/sbin/dodas_check_condor_schedd_tunnel \  
&& ln -s /opt/dodas/cache.py /usr/local/sbin/dodas_cache  
  
# CentOS uname characteristics  
RUN mv /bin/uname /bin/uname_old  
COPY ./bin/uname /bin/  
  
ENTRYPOINT ["/usr/bin/tini", "--", "/usr/local/sbin/dodas_condor"]  

