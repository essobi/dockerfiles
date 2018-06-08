# centos7 based dockerfile image  
  
# This builder image is for development purposes which has the development  
# tools necessary to build native applications  
# This relies on a runtime image called mts-runtime which is a centos7 based  
# docker image with minimal runtime libraries.  
#  
# This structure is to save space for docker imagesFROM centos:centos7  
  
FROM centos:centos7  
  
LABEL name="mts-runtime" \  
description="CentOS 7.2 based runtime image"  
  
#################################################################  
# Python related packages  
#  
# Some of the python modules require gcc & python devel to be installed  
# for external module builds  
  
# Basic runtime packages handling python2 python3 and gcc compiled binaries  
RUN yum update -y \  
&& yum install -y epel-release \  
&& yum install -y \  
bash \  
cmake3 \  
make \  
gcc \  
libgcc \  
libstdc++ \  
python \  
python34 \  
python2-pip \  
python34-pip \  
python-devel \  
python34-devel \  
iproute \  
nc \  
wget \  
curl \  
&& pip2 install --upgrade pip \  
&& pip3 install --upgrade pip \  
&& pip2 install virtualenv \  
&& pip3 install virtualenv  
  
# Common python runtimes required for MTS  
RUN pip2 install \  
click \  
click-plugins \  
requests \  
pex \  
PyYAML \  
&& pip3 install \  
click \  
click-plugins \  
requests \  
pex \  
PyYAML  
  
#################################################################  
# Data plane dependencies  
  
# I/O intercept library for interactive I/O  
RUN yum install -y \  
fuse \  
lmdb-devel  
  
#################################################################  
# Control plane dependencies  
RUN yum install -y \  
mysql-devel \  
nginx \  
supervisor  
  
#################################################################  
# TORQUE setup  
RUN yum install -y \  
wget \  
git \  
libtool \  
openssl-devel \  
libxml2-devel \  
boost-devel \  
gcc \  
gcc-c++ \  
make \  
openssh-server \  
openssh-client \  
libcgroup-tools  
  
# This fetches & installs torque binaries  
RUN mkdir -p /torque \  
&& cd /torque \  
&& wget https://www.open-
mpi.org/software/hwloc/v1.9/downloads/hwloc-1.9.1.tar.gz \  
&& tar xzf hwloc-1.9.1.tar.gz \  
&& cd hwloc-1.9.1 \  
&& ./configure && make -j 4 && make install \  
&& echo /usr/local/lib >/etc/ld.so.conf.d/hwloc.conf \  
&& ldconfig \  
&& cd /torque \  
&& git clone https://github.com/adaptivecomputing/torque.git -b 6.1.1 6.1.1 \  
&& cd 6.1.1 \  
&& ./autogen.sh \  
&& ./configure --enable-cgroups --with-hwloc-path=/usr/local \  
&& make -j 4 && make install \  
&& make packages  
  
# This will setup a default queue & default nodelists on the torque server  
# This should be overridden (or we can use this with ONBUILD)  
RUN ls -al /torque \  
&& cd /torque/6.1.1 \  
&& echo "localhost" > /var/spool/torque/server_name \  
&& echo '/usr/local/lib' > /etc/ld.so.conf.d/torque.conf \  
&& ldconfig \  
&& yes y | ./torque.setup root localhost && \  
pbs_sched && \  
qmgr -c "create queue debug queue_type=execution" && \  
qmgr -c "set queue debug enabled=true" && \  
qmgr -c "set queue debug started=true" && \  
qmgr -c "set server scheduling=True" && \  
qmgr -c 'set queue batch resources_default.walltime = 48:00:00' && \  
qmgr -c 'set queue batch resources_default.nodes = 1' && \  
qmgr -c 'set server default_queue = debug' \  
&& echo "localhost np=1" >> /var/spool/torque/server_priv/nodes \  
&& echo "mts-torque-base np=1" >> /var/spool/torque/server_priv/nodes  
  
# This is for the MOM (compute node)  
RUN cd /torque/6.1.1 \  
&& ./torque-package-mom-linux-x86_64.sh --install \  
&& ./torque-package-clients-linux-x86_64.sh --install \  
&& echo "\$pbsserver mts-torque-base" >> /var/spool/torque/mom_priv/config  
  
# Initiating the supervisor  
RUN pip2 install supervisor \  
&& mkdir -p /var/log/supervisor && chmod -R 777 /var/log/supervisor  
  
# An ordinary default supervisord  
ADD supervisord.conf /etc/supervisord.conf  
  
# Supervisord instances for Torque  
# Default entrypoint let this image act as a Torque server / mom node / client  
ADD torque/supervisord_server.conf /torque/supervisord_server.conf  
ADD torque/supervisord_login.conf /torque/supervisord_login.conf  
ADD torque/supervisord_mom.conf /torque/supervisord_mom.conf  
  
# Default port exposure and entrypoints just for reference since it cannot be
overridden by the children  
# We just annotate them here and let the children choose whatever they want  
  
ADD torque/docker_entrypoint.sh /docker_entrypoint.sh  
#ENTRYPOINT [ "/docker_entrypoint.sh" ]  
#EXPOSE 10389 22 9618  
#CMD ["/usr/bin/supervisord -c /torque/supervisord_server.conf"]  
  
###############################################  
## Adding sensu binaries  
  
# Installation of 'sensu' binaries  
COPY sensu/sensu.repo /etc/yum.repos.d/  
RUN yum install -y sensu  
  
###############################################  
## Adding condor binaries  
  
# Installation of 'sensu' binaries  
COPY htcondor//htcondor-rhel7.repo /etc/yum.repos.d/  
RUN cd / \  
&& wget http://research.cs.wisc.edu/htcondor/yum/RPM-GPG-KEY-HTCondor \  
&& rpm --import RPM-GPG-KEY-HTCondor  
RUN yum install -y condor.x86_64  
  
# GLIB  
RUN yum install -y \  
glib2-devel \  
libyaml-devel  
  

