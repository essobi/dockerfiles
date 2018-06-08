  
#  
# Debian 7 (wheezy) Cron30 Job Scheduler (dockerfile)  
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
FROM stafli/stafli.init.supervisor:supervisor30_debian7  
  
# Labels to apply  
LABEL description="Stafli Cron Job Scheduler (stafli/stafli.job.cron), Based
on Stafli Init Supervisor (stafli/stafli.init.supervisor)" \  
maintainer="lp@algarvio.org" \  
org.label-schema.schema-version="1.0.0-rc.1" \  
org.label-schema.name="Stafli Cron Job Scheduler (stafli/stafli.job.cron)" \  
org.label-schema.description="Based on Stafli Init Supervisor
(stafli/stafli.init.supervisor)" \  
org.label-schema.keywords="stafli, cron, job, debian, centos" \  
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
url="https://hub.docker.com/r/stafli/stafli.job.cron" \  
org.label-schema.vcs-url="https://github.com/stafli-org/stafli.job.cron" \  
org.label-schema.vcs-branch="master" \  
org.label-schema.os-id="debian" \  
org.label-schema.os-version-id="7" \  
org.label-schema.os-architecture="amd64" \  
org.label-schema.version="1.0"  
#  
# Arguments  
#  
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
# Install the cron packages  
# - cron: for crond, the process scheduling daemon  
# - anacron: for anacron, the cron-like program that doesn't go by time  
# Cleanup the package manager  
RUN printf "Installing repositories and packages...\n" && \  
\  
printf "Refresh the package manager...\n" && \  
apt-get update && \  
\  
printf "Install the selected packages...\n" && \  
apt-get install -qy \  
cron anacron && \  
\  
printf "Cleanup the package manager...\n" && \  
apt-get clean && rm -rf /var/lib/apt/lists/* && rm -Rf /var/cache/apt/* && \  
\  
printf "Finished installing repositories and packages...\n";  
  
#  
# Configuration  
#  
# Update daemon configuration  
# - Supervisor  
# - Cron  
RUN printf "Updading Daemon configuration...\n" && \  
\  
printf "Updading Supervisor configuration...\n" && \  
\  
# /etc/supervisor/conf.d/init.conf \  
file="/etc/supervisor/conf.d/init.conf" && \  
printf "\n# Applying configuration for ${file}...\n" && \  
printf "# init\n\  
[program:init]\n\  
command=/bin/bash -c \"supervisorctl start crond;\"\n\  
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
# /etc/supervisor/conf.d/crond.conf \  
file="/etc/supervisor/conf.d/crond.conf" && \  
printf "\n# Applying configuration for ${file}...\n" && \  
printf "# Cron\n\  
[program:crond]\n\  
command=/bin/bash -c \"\$(which cron) -f\"\n\  
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
printf "Updading Cron configuration...\n" && \  
\  
# ignoring /etc/default/cron \  
touch /etc/crontab && \  
\  
printf "Finished Daemon configuration...\n";  
  
#  
# Run  
#  
# Command to execute  
# Defaults to /bin/bash.  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf", "--
nodaemon"]  
  
# Ports to expose  
# Defaults to none  
#EXPOSE ...  

