FROM debian:jessie-backports  
  
# Add services helper utilities to start and stop LAVA  
COPY stop.sh .  
COPY start.sh .  
  
# Install debian packages used by the container  
# Configure apache to run the lava server  
# Log the hostname used during install for the slave name  
RUN echo 'lava-server lava-server/instance-name string lava-docker-instance' |
debconf-set-selections \  
&& echo 'locales locales/locales_to_be_generated multiselect C.UTF-8 UTF-8,
en_US.UTF-8 UTF-8 ' | debconf-set-selections \  
&& echo 'locales locales/default_environment_locale select en_US.UTF-8' |
debconf-set-selections \  
&& apt-get clean && apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y -t jessie-backports \  
locales \  
postgresql \  
screen \  
sudo \  
wget \  
expect \  
vim \  
&& service postgresql start \  
&& wget http://images.validation.linaro.org/production-repo/production-
repo.key.asc \  
&& apt-key add production-repo.key.asc \  
&& echo 'deb http://images.validation.linaro.org/production-repo/ sid main' >
/etc/apt/sources.list.d/lava.list \  
&& apt-get clean && apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y -t jessie-backports \  
lava \  
qemu-system \  
qemu-system-arm \  
qemu-system-i386 \  
qemu-kvm \  
&& a2enmod proxy \  
&& a2enmod proxy_http \  
&& a2dissite 000-default \  
&& a2ensite lava-server \  
&& /stop.sh \  
&& rm -rf /var/lib/apt/lists/*  
  
# (Optional) Add lava user SSH key and/or configuration  
# or mount a host file as a data volume (read-only)  
# e.g. -v /path/to/id_rsa_lava.pub:/home/lava/.ssh/authorized_keys:ro  
#COPY lava-credentials/.ssh /home/lava/.ssh  
  
# Remove comment to enable local proxy server (e.g. apt-cacher-ng)  
#RUN echo 'Acquire::http { Proxy "http://dockerproxy:3142"; };' >>
/etc/apt/apt.conf.d/01proxy  
  
# Add lava user with super-user privilege  
RUN useradd -m -G plugdev lava \  
&& echo 'lava ALL = NOPASSWD: ALL' > /etc/sudoers.d/lava \  
&& chmod 0440 /etc/sudoers.d/lava \  
&& mkdir -p /var/run/sshd /home/lava/bin /home/lava/.ssh \  
&& chmod 0700 /home/lava/.ssh \  
&& chown -R lava:lava /home/lava/bin /home/lava/.ssh  
  
# Add some job submission utilities  
COPY submittestjob.sh /home/lava/bin/  
COPY *.json *.py *.yaml /home/lava/bin/  
  
RUN mkdir -p /etc/lava-dispatcher/devices \  
&& mkdir -p /etc/lava-dispatcher/device-types  
  
# Add misc utilities  
COPY createsuperuser.sh add-devices-to-lava.sh getAPItoken.sh lava-
credentials.txt /home/lava/bin/  
COPY qemu-aarch64-01.conf qemu-aarch64-02.conf qemu-arm-01.conf qemu-
arm-02.conf qemu-arm-cortex-a9-01.conf qemu-arm-cortex-a9-02.conf qemu-arm-
cortex-a15-01.conf qemu-arm-cortex-a15-02.conf qemu-i386-01.conf
qemu-i386-02.conf kvm-01.conf kvm-02.conf /etc/lava-dispatcher/devices/  
COPY qemu-i386.conf /etc/lava-dispatcher/device-types/  
  
# (Optional) Add lava user SSH key and/or configuration  
# or mount a host file as a data volume (read-only)  
# e.g. -v /path/to/id_rsa_lava.pub:/home/lava/.ssh/authorized_keys:ro  
#COPY lava-credentials/.ssh /home/lava/.ssh  
  
# Remove comment to enable local proxy server (e.g. apt-cacher-ng)  
#RUN echo 'Acquire::http { Proxy "http://dockerproxy:3142"; };' >>
/etc/apt/apt.conf.d/01proxy  
  
# Create a admin user (Insecure note, this creates a default user, username:
kernel-ci/shazbot)  
RUN /start.sh \  
&& /home/lava/bin/createsuperuser.sh \  
&& /stop.sh  
  
# Install latest from master  
RUN /start.sh \  
&& git clone -b master https://git.linaro.org/lava/lava-dispatcher.git
/home/lava/lava-dispatcher \  
&& cd /home/lava/lava-dispatcher \  
&& git clone -b master https://git.linaro.org/lava/lava-server.git
/home/lava/lava-server \  
&& cd /home/lava/lava-server \  
&& echo "cd \${DIR} && dpkg -i *.deb" >> /home/lava/lava-server/share/debian-
dev-build.sh \  
&& cd /home/lava/lava-dispatcher && /home/lava/lava-server/share/debian-dev-
build.sh -p lava-dispatcher \  
&& cd /home/lava/lava-server && /home/lava/lava-server/share/debian-dev-
build.sh -p lava-server \  
&& /stop.sh  
  
EXPOSE 22 80  
  
CMD /start.sh && /home/lava/bin/getAPItoken.sh && /home/lava/bin/add-devices-
to-lava.sh && bash  
# Following CMD option starts the lava container without a shell and exposes
the logs  
#CMD /start.sh && tail -f /var/log/lava-*/*  

