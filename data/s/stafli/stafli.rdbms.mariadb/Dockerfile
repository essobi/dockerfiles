  
#  
# CentOS 6 (centos6) MariaDB10 RDBMS (dockerfile)  
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
FROM stafli/stafli.init.supervisor:supervisor31_centos6  
  
# Labels to apply  
LABEL description="Stafli MariaDB RDBMS (stafli/stafli.rdbms.mariadb), Based
on Stafli Supervisor Init (stafli/stafli.init.supervisor)" \  
maintainer="lp@algarvio.org" \  
org.label-schema.schema-version="1.0.0-rc.1" \  
org.label-schema.name="Stafli MariaDB RDBMS (stafli/stafli.rdbms.mariadb)" \  
org.label-schema.description="Based on Stafli Supervisor Init
(stafli/stafli.init.supervisor)" \  
org.label-schema.keywords="stafli, mariadb, rdbms, debian, centos" \  
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
url="https://hub.docker.com/r/stafli/stafli.rdbms.mariadb" \  
org.label-schema.vcs-url="https://github.com/stafli-org/stafli.rdbms.mariadb"
\  
org.label-schema.vcs-branch="master" \  
org.label-schema.os-id="centos" \  
org.label-schema.os-version-id="6" \  
org.label-schema.os-architecture="amd64" \  
org.label-schema.version="1.0"  
  
#  
# Arguments  
#  
  
ARG app_mariadb_global_user="mysql"  
ARG app_mariadb_global_group="mysql"  
ARG app_mariadb_global_home="/var/lib/mysql"  
ARG app_mariadb_global_loglevel="notice"  
ARG app_mariadb_global_listen_addr="0.0.0.0"  
ARG app_mariadb_global_listen_port="3306"  
ARG app_mariadb_global_default_storage_engine="InnoDB"  
ARG app_mariadb_global_default_character_set="utf8"  
ARG app_mariadb_global_default_collation="utf8_general_ci"  
ARG app_mariadb_tuning_max_connections="100"  
ARG app_mariadb_tuning_connect_timeout="5"  
ARG app_mariadb_tuning_wait_timeout="600"  
ARG app_mariadb_tuning_max_allowed_packet="128M"  
ARG app_mariadb_tuning_thread_cache_size="128"  
ARG app_mariadb_tuning_sort_buffer_size="4M"  
ARG app_mariadb_tuning_bulk_insert_buffer_size="16M"  
ARG app_mariadb_tuning_tmp_table_size="32M"  
ARG app_mariadb_tuning_max_heap_table_size="32M"  
ARG app_mariadb_query_cache_limit="128K"  
ARG app_mariadb_query_cache_size="64M"  
ARG app_mariadb_query_cache_min_res_unit="4k"  
ARG app_mariadb_query_cache_type="DEMAND"  
ARG app_mariadb_myisam_key_buffer_size="128M"  
ARG app_mariadb_myisam_open_files_limit="2000"  
ARG app_mariadb_myisam_table_open_cache="400"  
ARG app_mariadb_myisam_myisam_sort_buffer_size="512M"  
ARG app_mariadb_myisam_concurrent_insert="2"  
ARG app_mariadb_myisam_read_buffer_size="2M"  
ARG app_mariadb_myisam_read_rnd_buffer_size="1M"  
ARG app_mariadb_innodb_log_file_size="50M"  
ARG app_mariadb_innodb_buffer_pool_size="256M"  
ARG app_mariadb_innodb_buffer_pool_instances="1"  
ARG app_mariadb_innodb_log_buffer_size="8M"  
ARG app_mariadb_innodb_file_per_table="1"  
ARG app_mariadb_innodb_open_files="400"  
ARG app_mariadb_innodb_io_capacity="400"  
ARG app_mariadb_innodb_flush_method="O_DIRECT"  
  
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
# Add foreign repositories and GPG keys  
# - yum.mariadb.org: for MariaDB  
# Install the selected packages  
# Install the mariadb packages  
# - MariaDB-server: for mysqld, the MariaDB relational database management
system server  
# - MariaDB-client: for mysql, the MariaDB relational database management
system client  
# - mytop: for mytop, the MariaDB relational database management system top-
like utility  
# Cleanup the package manager  
RUN printf "Installing repositories and packages...\n" && \  
\  
printf "Install the foreign repositories and refresh the GPG keys...\n" && \  
printf "# MariaDB repository\n\  
[mariadb]\n\  
name = MariaDB\n\  
baseurl = http://yum.mariadb.org/10.1/centos6-amd64\n\  
gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB\n\  
gpgcheck=1\n\  
\n" > /etc/yum.repos.d/mariadb.repo && \  
rpm --import https://yum.mariadb.org/RPM-GPG-KEY-MariaDB && \  
\  
printf "Refresh the package manager...\n" && \  
rpm --rebuilddb && yum makecache && \  
\  
printf "Install the mariadb packages...\n" && \  
yum install -y \  
MariaDB-server MariaDB-client mytop && \  
\  
printf "Cleanup the package manager...\n" && \  
yum clean all && rm -Rf /var/lib/yum/* && rm -Rf /var/cache/yum/* && \  
\  
printf "Finished installing repositories and packages...\n";  
  
#  
# Configuration  
#  
  
# Add users and groups  
RUN printf "Adding users and groups...\n" && \  
\  
printf "Add mariadb user and group...\n" && \  
id -g ${app_mariadb_global_user} \  
|| \  
groupadd \  
\--system ${app_mariadb_global_group} && \  
id -u ${app_mariadb_global_user} && \  
usermod \  
\--gid ${app_mariadb_global_group} \  
\--home ${app_mariadb_global_home} \  
\--shell /sbin/nologin \  
${app_mariadb_global_user} \  
|| \  
useradd \  
\--system --gid ${app_mariadb_global_group} \  
\--no-create-home --home-dir ${app_mariadb_global_home} \  
\--shell /sbin/nologin \  
${app_mariadb_global_user} && \  
\  
printf "Finished adding users and groups...\n";  
  
# Supervisor  
RUN printf "Updading Supervisor configuration...\n" && \  
\  
# /etc/supervisord.d/init.conf \  
file="/etc/supervisord.d/init.conf" && \  
printf "\n# Applying configuration for ${file}...\n" && \  
perl -0p -i -e "s>supervisorctl start rclocal;>supervisorctl start rclocal;
supervisorctl start mysql;>" ${file} && \  
printf "Done patching ${file}...\n" && \  
\  
# /etc/supervisord.d/mysql.conf \  
file="/etc/supervisord.d/mysql.conf" && \  
printf "\n# Applying configuration for ${file}...\n" && \  
printf "# MariaDB\n\  
[program:mysql]\n\  
command=/bin/bash -c \"\$(which mysqld_safe) --defaults-file=/etc/my.cnf\"\n\  
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
# /etc/rc.local  
file="/etc/rc.local" && \  
printf "\n# Applying configuration for ${file}...\n" && \  
perl -0p -i -e "s>\nexit 0>>" ${file} && \  
printf "# Install MySQL\n\  
if [ ! -d \"${app_mariadb_global_home}/mysql\" ]; then\n\  
\$(which mysql_install_db) --user=${app_mariadb_global_user}
--ldata=${app_mariadb_global_home};\n\  
fi;\n\  
mkdir -p /var/log/mysql;\n\  
chown ${app_mariadb_global_user}:${app_mariadb_global_group}
/var/log/mysql;\n\  
\n\  
exit 0\n" >> ${file} && \  
printf "Done patching ${file}...\n" && \  
\  
printf "Finished updading Supervisor configuration...\n";  
  
# MariaDB  
RUN printf "Updading MariaDB configuration...\n" && \  
\  
# ignoring /etc/sysconfig/mysql \  
\  
# ignoring /etc/my.cnf \  
\  
# /etc/my.cnf.d/server.cnf \  
file="/etc/my.cnf.d/server.cnf" && \  
printf "\n# Applying configuration for ${file}...\n" && \  
# run as user \  
perl -0p -i -e "s>\[server\]>\[server\]\nuser\t\t=
${app_mariadb_global_user}>" ${file} && \  
# change home \  
perl -0p -i -e "s>\[server\]>\[server\]\ndatadir\t\t=
${app_mariadb_global_home}>" ${file} && \  
# change logging \  
perl -0p -i -e "s>\[server\]>\[server\]\nlog_error = /var/log/mysql/mariadb-
error.log>" ${file} && \  
if [ "$app_mariadb_global_loglevel" = "notice" ]; then
app_mariadb_global_loglevel_ovr="1"; elif [ "$app_mariadb_global_loglevel" =
"verbose" ]; then app_mariadb_global_loglevel_ovr="2"; else
app_mariadb_global_loglevel_ovr="1"; fi && \  
perl -0p -i -e "s>\[server\]>\[server\]\nlog_warnings =
${app_mariadb_global_loglevel_ovr}>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\nlog_output = FILE>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\ngeneral_log = 1>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\ngeneral_log_file =
/var/log/mysql/mariadb-general.log>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\nslow_query_log = 1>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\nslow_query_log_file =
/var/log/mysql/mariadb-slow.log>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\nlog_slow_admin_statements>" ${file}
&& \  
perl -0p -i -e "s>\[server\]>\[server\]\nlog_queries_not_using_indexes = 1>"
${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\nlog_slow_rate_limit = 1>" ${file} &&
\  
perl -0p -i -e "s>\[server\]>\[server\]\nlong_query_time = 2>" ${file} && \  
# change interface \  
perl -0p -i -e "s>\[server\]>\[server\]\nbind-address\t\t=
${app_mariadb_global_listen_addr}>" ${file} && \  
# change port \  
perl -0p -i -e "s>\[server\]>\[server\]\nport\t\t=
${app_mariadb_global_listen_port}>g" ${file} && \  
# change protocol \  
perl -0p -i -e "s>\[client\]>\[client\]\nprotocol = tcp>" ${file} && \  
# storage engine \  
perl -0p -i -e "s>\[server\]>\[server\]\ndefault_storage_engine =
${app_mariadb_global_default_storage_engine}>" ${file} && \  
# change collation \  
# https://stackoverflow.com/questions/3513773/change-mysql-default-character-
set-to-utf-8-in-my-cnf \  
# https://www.percona.com/blog/2014/01/28/10-mysql-settings-to-tune-after-
installation/ \  
# https://dev.mysql.com/doc/refman/5.6/en/charset-configuration.html \  
perl -0p -i -e "s>\[server\]>\[server\]\ncharacter-set-server =
${app_mariadb_global_default_character_set}>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\ncollation-server =
${app_mariadb_global_default_collation}>" ${file} && \  
# change tuning settings \  
perl -0p -i -e "s>\[server\]>\[server\]\nmax_connections\t\t=
${app_mariadb_tuning_max_connections}>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\nconnect_timeout\t\t=
${app_mariadb_tuning_connect_timeout}>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\nwait_timeout\t\t=
${app_mariadb_tuning_wait_timeout}>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\nmax_allowed_packet\t=
${app_mariadb_tuning_max_allowed_packet}>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\nthread_cache_size =
${app_mariadb_tuning_thread_cache_size}>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\nsort_buffer_size\t=
${app_mariadb_tuning_sort_buffer_size}>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\nbulk_insert_buffer_size\t=
${app_mariadb_tuning_bulk_insert_buffer_size}>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\ntmp_table_size\t\t=
${app_mariadb_tuning_tmp_table_size}>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\nmax_heap_table_size\t=
${app_mariadb_tuning_max_heap_table_size}>" ${file} && \  
# change query cache settings \  
perl -0p -i -e "s>\[server\]>\[server\]\nquery_cache_limit\t\t=
${app_mariadb_query_cache_limit}>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\nquery_cache_size\t\t=
${app_mariadb_query_cache_size}>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\nquery_cache_min_res_unit\t=
${app_mariadb_query_cache_min_res_unit}>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\nquery_cache_type\t\t=
${app_mariadb_query_cache_type}>" ${file} && \  
# change myisam settings \  
perl -0p -i -e "s>\[server\]>\[server\]\nkey_buffer_size\t\t=
${app_mariadb_myisam_key_buffer_size}>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\nopen-files-limit\t=
${app_mariadb_myisam_open_files_limit}>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\ntable_open_cache\t=
${app_mariadb_myisam_table_open_cache}>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\nmyisam_sort_buffer_size\t=
${app_mariadb_myisam_myisam_sort_buffer_size}>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\nconcurrent_insert\t=
${app_mariadb_myisam_concurrent_insert}>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\nread_buffer_size\t=
${app_mariadb_myisam_read_buffer_size}>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\nread_rnd_buffer_size\t=
${app_mariadb_myisam_read_rnd_buffer_size}>" ${file} && \  
# change innodb settings \  
perl -0p -i -e "s>\[server\]>\[server\]\ninnodb_log_file_size\t=
${app_mariadb_innodb_log_file_size}>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\ninnodb_buffer_pool_size\t=
${app_mariadb_innodb_buffer_pool_size}>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\ninnodb_buffer_pool_instances\t=
${app_mariadb_innodb_buffer_pool_instances}>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\ninnodb_log_buffer_size\t=
${app_mariadb_innodb_log_buffer_size}>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\ninnodb_file_per_table\t=
${app_mariadb_innodb_file_per_table}>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\ninnodb_open_files\t=
${app_mariadb_innodb_open_files}>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\ninnodb_io_capacity\t=
${app_mariadb_innodb_io_capacity}>" ${file} && \  
perl -0p -i -e "s>\[server\]>\[server\]\ninnodb_flush_method\t=
${app_mariadb_innodb_flush_method}>" ${file} && \  
# change mysqldump settings \  
perl -0p -i -e "s>\[mysqldump\]\nquick\nquote-names\nmax_allowed_packet\t=
.*>\[mysqldump\]\nquick\nquote-names\nmax_allowed_packet\t=
${app_mariadb_tuning_max_allowed_packet}>" ${file} && \  
# change client settings \  
perl -0p -i -e "s>\[client\]\nport\t\t= .*>\[client\]\nport\t\t=
${app_mariadb_global_listen_port}>g" ${file} && \  
printf "Done patching ${file}...\n" && \  
\  
# /etc/my.cnf.d/client.cnf \  
file="/etc/my.cnf.d/client.cnf" && \  
touch ${file} && \  
printf "\n# Applying configuration for ${file}...\n" && \  
# add missing sections \  
printf "#\n\  
# These two groups are read by the client library\n\  
# Use it for options that affect all clients, but not the server\n\  
#\n\n\n\  
[client]\n\n\  
# This group is not read by mysql client library,\n\  
# If you use the same .cnf file for MySQL and MariaDB,\n\  
# use it for MariaDB-only client options\n\  
[client-mariadb]\n\n" >> ${file} && \  
# change protocol \  
perl -0p -i -e "s>\[client\]>\[client\]\nprotocol = tcp>" ${file} && \  
# change port \  
perl -0p -i -e "s>\[client\]>\[client\]\nport =
${app_mariadb_global_listen_port}>" ${file} && \  
# change engine and collation \  
# https://stackoverflow.com/questions/3513773/change-mysql-default-character-
set-to-utf-8-in-my-cnf \  
# https://www.percona.com/blog/2014/01/28/10-mysql-settings-to-tune-after-
installation/ \  
# https://dev.mysql.com/doc/refman/5.6/en/charset-configuration.html \  
perl -0p -i -e "s>\[client\]>\[client\]\ndefault-character-set =
${app_mariadb_global_default_character_set}>" ${file} && \  
printf "Done patching ${file}...\n" && \  
\  
# /etc/my.cnf.d/mysql-clients.cnf \  
file="/etc/my.cnf.d/mysql-clients.cnf" && \  
printf "\n# Applying configuration for ${file}...\n" && \  
# change performance settings \  
perl -0p -i -e "s>\[mysqldump\]>\[mysqldump\]\nquick\nquote-
names\nmax_allowed_packet = ${app_mariadb_tuning_max_allowed_packet}>" ${file}
&& \  
printf "Done patching ${file}...\n" && \  
\  
printf "\n# Testing configuration...\n" && \  
echo "Testing $(which mysql):"; $(which mysql) -V && \  
echo "Testing $(which mysqld):"; $(which mysqld) -V && \  
printf "Done testing configuration...\n" && \  
\  
printf "Finished updading MariaDB configuration...\n";  
  
#  
# Run  
#  
  
# Command to execute  
# Defaults to /bin/bash.  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf", "--nodaemon"]  
  
# Ports to expose  
# Defaults to 3306  
EXPOSE ${app_mariadb_global_listen_port}  
  

