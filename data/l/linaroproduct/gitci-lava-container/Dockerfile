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
&& a2enmod proxy \  
&& a2enmod proxy_http \  
&& a2dissite 000-default \  
&& a2ensite lava-server \  
&& /stop.sh \  
&& rm -rf /var/lib/apt/lists/*  
  
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
  
# Add misc utilities  
COPY createsuperuser.sh /home/lava/bin/  
COPY add-devices-to-lava.sh /home/lava/bin/  
COPY getAPItoken.sh /home/lava/bin/  
COPY lava-credentials.txt /home/lava/bin/  
COPY qemu.jinja2 /etc/dispatcher-config/devices/  
COPY nrf52-nitrogen.jinja2 /etc/dispatcher-config/devices/  
COPY nxp-k64f.jinja2 /etc/dispatcher-config/devices/  
COPY stm32-carbon-01.jinja2 /etc/dispatcher-config/devices/  
COPY stm32-carbon-02.jinja2 /etc/dispatcher-config/devices/  
COPY stm32-carbon-03.jinja2 /etc/dispatcher-config/devices/  
COPY stm32-carbon-04.jinja2 /etc/dispatcher-config/devices/  
  
# Create a admin user (Insecure note, this creates a default user, username:
admin/admin)  
RUN /start.sh \  
&& /home/lava/bin/createsuperuser.sh \  
&& /stop.sh  
  
# Install latest from 2016.11  
RUN /start.sh \  
&& git clone -b master https://git.linaro.org/lava/lava-dispatcher.git
/home/lava/lava-dispatcher \  
&& cd /home/lava/lava-dispatcher \  
&& git checkout 2016.11 \  
&& cd /home/lava/ \  
&& git clone -b master https://git.linaro.org/lava/lava-server.git
/home/lava/lava-server \  
&& cd /home/lava/lava-server \  
&& git checkout 2016.11 \  
&& echo "cd \${DIR} && dpkg -i *.deb" >> /home/lava/lava-server/share/debian-
dev-build.sh \  
&& cd /home/lava/lava-dispatcher && /home/lava/lava-server/share/debian-dev-
build.sh -p lava-dispatcher \  
&& cd /home/lava/lava-server && /home/lava/lava-server/share/debian-dev-
build.sh -p lava-server \  
&& /stop.sh  
  
# To run jobs using python XMLRPC, we need the API token (really ugly)  
RUN /start.sh \  
&& /home/lava/bin/getAPItoken.sh \  
&& /stop.sh  
  
EXPOSE 22 80 5555 5556  
CMD /start.sh && /home/lava/bin/add-devices-to-lava.sh 41 && bash  

