FROM debian:stretch  
#FROM debian:stretch-backports  
ENV container docker  
  
# Add services helper utilities to start and stop LAVA  
COPY scripts/*.sh /  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \  
systemd \  
screen \  
sudo \  
wget \  
gnupg \  
vim-tiny \  
tftpd-hpa  
  
# Idea came from https://github.com/solita/docker-systemd  
# Don't start any optional services except for the few we need.  
RUN find /etc/systemd/system \  
/lib/systemd/system \  
-path '*.wants/*' \  
-not -name '*journald*' \  
-not -name '*systemd-tmpfiles*' \  
-not -name '*systemd-user-sessions*' \  
# keep apache2 related service files  
-not -name 'runlevel3.target' \  
-exec rm \\{} \; \  
&& systemctl set-default multi-user.target \  
&& ln -s ../runlevel3.target /lib/systemd/system/multi-user.target.wants  
  
# Install debian packages used by the container  
# Configure apache to run the lava server  
# Log the hostname used during install for the slave name  
RUN echo 'lava-server lava-server/instance-name string lava-docker-instance' |
debconf-set-selections \  
&& echo 'locales locales/locales_to_be_generated multiselect C.UTF-8 UTF-8,
en_US.UTF-8 UTF-8 ' | debconf-set-selections \  
&& echo 'locales locales/default_environment_locale select en_US.UTF-8' |
debconf-set-selections  
  
# Install latest postgresql  
RUN wget --no-check-certificate
https://www.postgresql.org/media/keys/ACCC4CF8.asc \  
&& apt-key add ACCC4CF8.asc \  
&& echo 'deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main' >
/etc/apt/sources.list.d/pgdg.list \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \  
postgresql  
  
RUN wget --no-check-certificate https://images.validation.linaro.org/staging-
repo/staging-repo.key.asc \  
&& apt-key add staging-repo.key.asc \  
&& echo 'deb http://images.validation.linaro.org/staging-repo stretch-
backports main' > /etc/apt/sources.list.d/lava.list \  
&& apt-get update  
  
# removed --no-install-recommends option for now, will add it back later  
RUN service postgresql start \  
&& DEBIAN_FRONTEND=noninteractive apt-get -t stretch-backports install -y \  
lava-server \  
lava-tool \  
ser2net \  
u-boot-tools \  
python-setproctitle \  
&& apt-get clean \  
&& a2dissite 000-default \  
&& a2enmod proxy \  
&& a2enmod proxy_http \  
&& a2ensite lava-server.conf \  
&& apt-get autoremove -y \  
&& mv /usr/share/doc/lava* /root && rm -rf /usr/share/doc/* && mv /root/lava*
/usr/share/doc/ \  
&& service postgresql stop \  
&& dpkg -l lava-server lava-dispatcher lava-tool python3-django
python3-django-tables2  
  
COPY configs/tftpd-hpa /etc/default/tftpd-hpa  
  
EXPOSE 69/udp 80 3079 5555 5556  
#CMD /start.sh && bash  
STOPSIGNAL SIGRTMIN+3  
# Workaround for docker/docker#27202, technique based on comments from
docker/docker#9212  
CMD ["/bin/bash", "-c", "exec /sbin/init --log-target=journal 3>&1"]  

