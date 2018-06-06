FROM mesoform/concierge-debian-base-image:latest  
  
# Add some labels  
LABEL maintainer="Gareth Brown <gareth@mesoform.com>"  
LABEL description="Concierge managed Zabbix server for event management"  
LABEL com.mesoform.baseimage=False  
LABEL com.joyent.autopilotpattern=True  
LABEL com.mesoform.builddate="2018-03-28T14:59:38Z"  
LABEL com.mesoform.baseimage.ver="mesoform/concierge-debian-base-image:latest"  
LABEL com.docker.img.ver="mesoform/concierge-zabbix:1.1.28"  
  
# Set some environment variables  
ENV DOCKER_IMG_VER="mesoform/concierge-zabbix:1.1.28"  
RUN unset CONSUL_AGENT  
ENV LOG_LEVEL="INFO"  
ENV LOG_FORMAT="text"  
ENV COMMAND="/usr/local/bin/run_zabbix_component.sh server mysql"  
ENV SHELL=/bin/bash  
ENV DOCKER_IMG_VER="mesoform/concierge-zabbix:1.1.28"  
ENV DNS_DOMAIN=zabbix.dockerlx.oaas.mesoform.com  
ENV HOSTMETADATA=zabbix.dockerlx  
ENV CONSUL_AGENT=True  
ENV LANG=en_US.UTF-8  
ENV LANGUAGE=en_US:en  
ENV LC_ALL=en_US.UTF-8  
ENV DEBIAN_FRONTEND=noninteractive  
ENV TERM=xterm  
ENV MIBDIRS=/usr/share/snmp/mibs:/var/lib/zabbix/mibs  
ENV MIBS=+ALL  
ENV ZBX_SRV_VER=3.2.6  
ENV ZBX_SRV_SRC=svn://svn.zabbix.com/tags/3.2.6/  
ENV SVC_DISCOVERY=consul  
  
# Set some build arguments  
ARG APT_FLAGS_COMMON="-qq -y"  
ARG APT_FLAGS_PERSISTANT="${APT_FLAGS_COMMON} --no-install-recommends"  
ARG APT_FLAGS_DEV="${APT_FLAGS_COMMON} --no-install-recommends"  
ARG DB_TYPE=mysql  
ARG MAJOR_VERSION=3.2  
ARG ZBX_SRV_VER=3.2.6  
ARG ZBX_SRV_SRC=svn://svn.zabbix.com/tags/3.2.6/  
ARG DOCKER_VERSION=17.12.0~ce-0~debian  
ARG OS_DISTRO=debian  
ARG LSB_RELEASE=jessie  
ARG DOCKER_COMP=1.16.1/docker-compose-Linux-x86_64  
ARG GIT_USR=dperezs  
ARG GIT_PASS=YgxnbS5dyGwJLgGQhypx  
ARG JSON_BCK_FILES_URL=bitbucket.org/dperezs/zabbix-config-json-files.git  
ARG
CONCIERGE_SCHED_URL=https://github.com/mesoform/concierge_scheduler.git/trunk/src/concierge_scheduler  
  
  
# If we have any install scripts, run them.  
RUN chmod -R +x /usr/local/bin/install.sh && \  
sync && \  
/usr/local/bin/install.sh  
  
# make directories  
RUN mkdir -p /usr/lib/zabbix/alertscripts /usr/lib/zabbix/externalscripts
/var/lib/zabbix/enc /var/lib/zabbix/modules /var/lib/zabbix/ssh_keys
/var/lib/zabbix/ssl/certs /var/lib/zabbix/ssl/keys /var/lib/zabbix/ssl/ssl_ca
/var/lib/zabbix/snmptraps /var/lib/zabbix/mibs  
# define volumes if set  
VOLUME /usr/lib/zabbix/alertscripts /usr/lib/zabbix/externalscripts
/var/lib/zabbix/enc /var/lib/zabbix/modules /var/lib/zabbix/ssh_keys
/var/lib/zabbix/ssl/certs /var/lib/zabbix/ssl/keys /var/lib/zabbix/ssl/ssl_ca
/var/lib/zabbix/snmptraps /var/lib/zabbix/mibs  
  
# Expose primary service port  
EXPOSE 10051  
# Expose additional container ports  
EXPOSE 10051/TCP  
HEALTHCHECK \  
\--interval=12s \  
\--timeout=6s \  
\--retries=4 \  
CMD /usr/local/bin/zabbix-manage.sh health_check  

