# centos7 based Torque binary base  
FROM centos:centos7  
  
LABEL name="mts-torque-base" \  
description="CentOS 7.2 based per manager node runtime"  
  
# TORQUE settings can be overridden by providing the below from a derived
image  
# - /var/spool/torque/server_priv/nodes --> for servers  
# - /var/spool/torque/mom_priv/config --> for the compute nodes  
# Supervisor scripts which would differ between node types  
RUN yum update -y \  
&& yum install -y \  
epel-release \  
&& yum install -y \  
python \  
python-devel \  
python2-pip \  
&& pip2 install --upgrade pip \  
&& pip2 install virtualenv  
  
RUN yum install -y \  
wget \  
git \  
libtool \  
openssl-devel \  
libxml2-devel \  
boost-devel \  
gcc \  
gcc-c++ \  
supervisor \  
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
  
RUN pip2 install supervisor \  
&& mkdir -p /var/log/supervisor && chmod -R 777 /var/log/supervisor  
ADD supervisord.conf /etc/supervisord.conf  
ADD torque/supervisord_server.conf /torque/supervisord_server.conf  
ADD torque/supervisord_login.conf /torque/supervisord_login.conf  
ADD torque/supervisord_mom.conf /torque/supervisord_mom.conf  
ADD torque/docker_entrypoint.sh /docker_entrypoint.sh  
  
# Default entrypoint let this image act as a Torque server / mom node / client  
ENTRYPOINT [ "/docker_entrypoint.sh" ]  
EXPOSE 10389 22 9618  
CMD ["/usr/bin/supervisord -c /supervisord.conf"]  
  
# An example script  
ADD torque/torque.submit /torque.submit  

