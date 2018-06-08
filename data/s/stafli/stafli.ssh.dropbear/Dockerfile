  
#  
# CentOS 7 (centos7) Dropbear2017 SSH Server (dockerfile)  
# Copyright (C) 2016-2017 Stafli  
# Luís Pedro Algarvio  
# This file is part of the Stafli Application Stack.  
#  
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.  
#  
# This program is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
#  
# You should have received a copy of the GNU General Public License  
# along with this program. If not, see <http://www.gnu.org/licenses/>.  
#  
  
#  
# Build  
#  
  
# Base image to use  
FROM stafli/stafli.init.supervisor:supervisor31_centos7  
  
# Labels to apply  
LABEL description="Stafli Dropbear SSH Server (stafli/stafli.ssh.dropbear),
Based on Stafli Init Supervisor (stafli/stafli.init.supervisor)" \  
maintainer="lp@algarvio.org" \  
org.label-schema.schema-version="1.0.0-rc.1" \  
org.label-schema.name="Stafli Dropbear SSH Server
(stafli/stafli.ssh.dropbear)" \  
org.label-schema.description="Based on Stafli Init Supervisor
(stafli/stafli.init.supervisor)" \  
org.label-schema.keywords="stafli, dropbear, ssh, debian, centos" \  
org.label-schema.url="https://stafli.org/" \  
org.label-schema.license="GPLv3" \  
org.label-schema.vendor-name="Stafli" \  
org.label-schema.vendor-email="info@stafli.org" \  
org.label-schema.vendor-website="https://www.stafli.org" \  
org.label-schema.authors.lpalgarvio.name="Luis Pedro Algarvio" \  
org.label-schema.authors.lpalgarvio.email="lp@algarvio.org" \  
org.label-schema.authors.lpalgarvio.homepage="https://lp.algarvio.org" \  
org.label-schema.authors.lpalgarvio.role="Maintainer" \  
org.label-schema.registry-
url="https://hub.docker.com/r/stafli/stafli.ssh.dropbear" \  
org.label-schema.vcs-url="https://github.com/stafli-org/stafli.ssh.dropbear" \  
org.label-schema.vcs-branch="master" \  
org.label-schema.os-id="centos" \  
org.label-schema.os-version-id="7" \  
org.label-schema.os-architecture="amd64" \  
org.label-schema.version="1.0"  
  
#  
# Arguments  
#  
  
ARG app_dropbear_listen_addr="0.0.0.0"  
ARG app_dropbear_listen_port="22"  
ARG app_dropbear_key_size="4096"  
  
#  
# Environment  
#  
  
# Working directory to use when executing build and run instructions  
# Defaults to /.  
#WORKDIR /  
  
# User and group to use when executing build and run instructions  
# Defaults to root.  
#USER root:root  
  
#  
# Packages  
#  
  
# Refresh the package manager  
# Install the selected packages  
# Install the dropbear packages  
# - dropbear: for dropbear, a lightweight SSH2 server and client that replaces
OpenSSH  
# Cleanup the package manager  
RUN printf "Installing repositories and packages...\n" && \  
\  
printf "Refresh the package manager...\n" && \  
rpm --rebuilddb && yum makecache && \  
\  
printf "Install the selected packages...\n" && \  
yum install -y \  
dropbear && \  
\  
printf "Cleanup the package manager...\n" && \  
yum clean all && rm -Rf /var/lib/yum/* && rm -Rf /var/cache/yum/* && \  
\  
printf "Finished installing repositories and packages...\n";  
  
#  
# Configuration  
#  
  
# Update daemon configuration  
# - Supervisor  
# - Dropbear  
RUN printf "Updading Daemon configuration...\n" && \  
\  
printf "Updading Supervisor configuration...\n" && \  
\  
# /etc/supervisord.d/init.conf \  
file="/etc/supervisord.d/init.conf" && \  
printf "\n# Applying configuration for ${file}...\n" && \  
printf "# init\n\  
[program:init]\n\  
command=/bin/bash -c \"supervisorctl start rclocal; sleep 5; supervisorctl
start dropbear;\"\n\  
autostart=true\n\  
autorestart=false\n\  
startsecs=0\n\  
stdout_logfile=/dev/stdout\n\  
stdout_logfile_maxbytes=0\n\  
stderr_logfile=/dev/stderr\n\  
stderr_logfile_maxbytes=0\n\  
stdout_events_enabled=true\n\  
stderr_events_enabled=true\n\  
\n" > ${file} && \  
printf "Done patching ${file}...\n" && \  
\  
# /etc/supervisord.d/rclocal.conf \  
file="/etc/supervisord.d/rclocal.conf" && \  
printf "\n# Applying configuration for ${file}...\n" && \  
printf "# rclocal\n\  
[program:rclocal]\n\  
command=/bin/bash -c \"/etc/rc.local\"\n\  
autostart=false\n\  
autorestart=false\n\  
startsecs=0\n\  
stdout_logfile=/dev/stdout\n\  
stdout_logfile_maxbytes=0\n\  
stderr_logfile=/dev/stderr\n\  
stderr_logfile_maxbytes=0\n\  
stdout_events_enabled=true\n\  
stderr_events_enabled=true\n\  
\n" > ${file} && \  
printf "Done patching ${file}...\n" && \  
\  
# /etc/rc.local \  
file="/etc/rc.local" && \  
touch ${file} && chown root ${file} && chmod 755 ${file} && \  
\  
# /etc/supervisord.d/dropbear.conf \  
file="/etc/supervisord.d/dropbear.conf" && \  
printf "\n# Applying configuration for ${file}...\n" && \  
printf "# Dropbear\n\  
[program:dropbear]\n\  
command=/bin/bash -c \"opts=\$(grep -o '^[^#]*' /etc/dropbear/dropbear.conf)
&& exec \$(which dropbear) \$opts -F\"\n\  
autostart=false\n\  
autorestart=true\n\  
stdout_logfile=/dev/stdout\n\  
stdout_logfile_maxbytes=0\n\  
stderr_logfile=/dev/stderr\n\  
stderr_logfile_maxbytes=0\n\  
stdout_events_enabled=true\n\  
stderr_events_enabled=true\n\  
\n" > ${file} && \  
printf "Done patching ${file}...\n" && \  
\  
printf "Updading Dropbear configuration...\n" && \  
\  
# ignoring /etc/sysconfig/dropbear \  
\  
# /etc/dropbear/dropbear.conf \  
file="/etc/dropbear/dropbear.conf" && \  
# clear old file  
printf "#\n# dropbear.conf\n#\n" > ${file} && \  
# disable daemon/run in foreground \  
printf "\n# Run in foreground mode\n#-F\n" >> ${file} && \  
# change interface and port \  
printf "\n# Listen on specified address and port (Default: 0.0.0.0:22)\n-p
${app_dropbear_listen_addr}:${app_dropbear_listen_port}\n" >> ${file} && \  
# change ssh keys \  
printf "\n# Use the following ssh keys:\n-r
/etc/dropbear/dropbear_rsa_host_key\n" >> ${file} && \  
printf "Done patching ${file}...\n" && \  
\  
# Remove persistent ssh keys \  
printf "\n# Removing persistent ssh keys...\n" && \  
rm -f /etc/dropbear/*host_key && \  
\  
# /etc/rc.local \  
file="/etc/rc.local" && \  
printf "\n# Applying configuration for ${file}...\n" && \  
perl -0p -i -e "s>\nexit 0>\n# exit 0\n>" ${file} && \  
printf "\n\  
# Recreate dropbear private keys\n\  
# https://github.com/simonswine/docker-dropbear/blob/master/run.sh\n\  
CONF_DIR=\"/etc/dropbear\";\n\  
SSH_KEY_RSA=\"\${CONF_DIR}/dropbear_rsa_host_key\";\n\  
SSH_KEY_DSS=\"\${CONF_DIR}/dropbear_dss_host_key\";\n\  
SSH_KEY_ECDSA=\"\${CONF_DIR}/dropbear_ecdsa_host_key\";\n\  
\n\  
# Check if conf dir exists\n\  
if [ ! -d \${CONF_DIR} ]; then\n\  
mkdir -p \${CONF_DIR};\n\  
fi;\n\  
chown root:root \${CONF_DIR};\n\  
chmod 755 \${CONF_DIR};\n\  
\n\  
# Check if keys exists\n\  
if [ ! -f \${SSH_KEY_DSS} ]; then\n\  
rm -f \${SSH_KEY_DSS};\n\  
fi;\n\  
if [ ! -f \${SSH_KEY_ECDSA} ]; then\n\  
rm -f \${SSH_KEY_ECDSA};\n\  
fi;\n\  
\n\  
# Generate only the RSA key  
if [ ! -f \${SSH_KEY_RSA} ]; then\n\  
dropbearkey -t rsa -f \${SSH_KEY_RSA} -s ${app_dropbear_key_size};\n\  
fi;\n\  
chown root:root \${SSH_KEY_RSA};\n\  
chmod 600 \${SSH_KEY_RSA};\n\  
\n\  
exit 0\n" >> ${file} && \  
printf "Done patching ${file}...\n" && \  
\  
printf "Finished Daemon configuration...\n";  
  
#  
# Run  
#  
  
# Command to execute  
# Defaults to /bin/bash.  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf", "--nodaemon"]  
  
# Ports to expose  
# Defaults to 22  
EXPOSE ${app_dropbear_listen_port}  
  

