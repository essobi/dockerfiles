FROM mesoform/concierge-debian-base-image:latest  
  
# Add some labels  
LABEL maintainer="Daniel Perez <dan@mesoform.com>"  
LABEL description="Concierge managed Zabbix web frontend for Mesoform"  
LABEL com.mesoform.baseimage=False  
LABEL com.joyent.autopilotpattern=True  
LABEL com.mesoform.builddate="2018-03-25T19:59:10Z"  
LABEL com.mesoform.baseimage.ver="mesoform/concierge-debian-base-image:latest"  
LABEL com.docker.img.ver="mesoform/concierge-zabbix-web:0.1.11"  
  
# Set some environment variables  
ENV DOCKER_IMG_VER="mesoform/concierge-zabbix-web:0.1.11"  
RUN unset CONSUL_AGENT  
ENV LOG_LEVEL="INFO"  
ENV LOG_FORMAT="text"  
ENV COMMAND="/usr/local/bin/run_zabbix_component.sh frontend mysql apache"  
ENV SHELL=/bin/bash  
ENV DOCKER_IMG_VER="mesoform/concierge-zabbix-web:0.1.11"  
ENV HOSTMETADATA=zabbix-web.dockerlx  
ENV CONSUL_AGENT=True  
ENV LANG=en_US.UTF-8  
ENV LANGUAGE=en_US:en  
ENV LC_ALL=en_US.UTF-8  
ENV DEBIAN_FRONTEND=noninteractive  
ENV TERM=xterm  
ENV ZBX_WEB_VER=3.2.6  
ENV ZBX_WEB_SRC=svn://svn.zabbix.com/tags/3.2.6/  
ENV SVC_DISCOVERY=consul  
  
# Set some build arguments  
ARG APT_FLAGS_COMMON="-qq -y"  
ARG APT_FLAGS_PERSISTANT="${APT_FLAGS_COMMON} --no-install-recommends"  
ARG APT_FLAGS_DEV="${APT_FLAGS_COMMON} --no-install-recommends"  
ARG DB_TYPE=mysql  
ARG MAJOR_VERSION=3.2  
ARG ZBX_WEB_VER=3.2.6  
ARG ZBX_WEB_SRC=svn://svn.zabbix.com/tags/3.2.6/  
  
  
# If we have any install scripts, run them.  
RUN chmod -R +x /usr/local/bin/install.sh && \  
sync && \  
/usr/local/bin/install.sh  
  
# make directories  
RUN mkdir -p /etc/ssl/apache2  
# define volumes if set  
VOLUME /etc/ssl/apache2  
  
# Expose primary service port  
EXPOSE 80  
# Expose additional container ports  
EXPOSE 80/TCP 443/TCP  
HEALTHCHECK \  
\--interval=10s \  
\--timeout=3s \  
\--retries=4 \  
CMD /usr/local/bin/zabbix-manage.sh health_check  

