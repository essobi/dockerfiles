  
#  
# CentOS 6 (centos6) HTTPd22 Proxy service (dockerfile)  
# Copyright (C) 2016 SOL-ICT  
# This file is part of the Docker High Performance PHP Stack.  
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
  
FROM solict/general-purpose-system-distro:centos6_standard  
MAINTAINER Luís Pedro Algarvio <lp.algarvio@gmail.com>  
  
#  
# Arguments  
#  
  
ARG app_httpd_global_mods_core_dis=""  
ARG app_httpd_global_mods_core_en=""  
ARG app_httpd_global_mods_extra_dis=""  
ARG app_httpd_global_mods_extra_en=""  
ARG app_httpd_global_user="apache"  
ARG app_httpd_global_group="apache"  
ARG app_httpd_global_home="/var/www"  
ARG app_httpd_global_loglevel="warn"  
ARG app_httpd_global_listen_addr="0.0.0.0"  
ARG app_httpd_global_listen_port_http="80"  
ARG app_httpd_global_listen_port_https="443"  
ARG app_httpd_global_listen_timeout="140"  
ARG app_httpd_global_listen_keepalive_status="On"  
ARG app_httpd_global_listen_keepalive_requests="100"  
ARG app_httpd_global_listen_keepalive_timeout="5"  
ARG app_httpd_vhost_id="default"  
ARG app_httpd_vhost_user="apache"  
ARG app_httpd_vhost_group="apache"  
ARG app_httpd_vhost_listen_addr="0.0.0.0"  
ARG app_httpd_vhost_listen_port_http="80"  
ARG app_httpd_vhost_listen_port_https="443"  
ARG app_httpd_vhost_httpd_wlist="127.0.0.1 10.0.0.0/8 172.16.0.0/12
192.168.0.0/16"  
  
#  
# Packages  
#  
  
# Install the HTTPd packages  
# - httpd: for httpd, the HTTPd server  
# - httpd-tools: for ab and others, the HTTPd utilities  
# - apachetop: for apachetop, the top-like utility for HTTPd  
# - mod_ssl: the OpenSSL DSO module  
# - mod_authnz_external: the External Authentication DSO module  
# - mod_xsendfile: the X-Sendfile DSO module  
RUN printf "Installing repositories and packages...\n" && \  
\  
printf "Install the HTTPd packages...\n" && \  
rpm --rebuilddb && \  
yum makecache && yum install -y \  
httpd \  
httpd-tools apachetop \  
mod_ssl \  
mod_authnz_external pwauth \  
mod_xsendfile && \  
printf "Cleanup the Package Manager...\n" && \  
yum clean all && rm -Rf /var/lib/yum/*; \  
\  
printf "Finished installing repositories and packages...\n";  
  
#  
# HTTPd DSO modules  
#  
  
# Enable/Disable HTTPd modules  
RUN printf "Start installing modules...\n" && \  
\  
# Module configuration files \  
mkdir /etc/httpd/conf.modules.d; \  
touch /etc/httpd/conf.modules.d/00-dav.conf; \  
touch /etc/httpd/conf.modules.d/00-proxy.conf; \  
touch /etc/httpd/conf.modules.d/00-ssl.conf; \  
touch /etc/httpd/conf.modules.d/01-cgi.conf; \  
touch /etc/httpd/conf.modules.d/00-base.conf; \  
\  
printf "Enabling/disabling modules...\n" && \  
\  
# /etc/httpd/conf.modules.d/00-base.conf \  
file="/etc/httpd/conf.modules.d/00-base.conf"; \  
printf "\n# Applying configuration for ${file}...\n"; \  
# add load module \  
printf "\  
#\n\  
# This file loads most of the modules included with the Apache HTTP\n\  
# Server itself.\n\  
#\n\  
\n\  
LoadModule actions_module modules/mod_actions.so\n\  
LoadModule alias_module modules/mod_alias.so\n\  
LoadModule auth_basic_module modules/mod_auth_basic.so\n\  
#LoadModule auth_digest_module modules/mod_auth_digest.so\n\  
LoadModule authn_alias_module modules/mod_authn_alias.so\n\  
#LoadModule authn_anon_module modules/mod_authn_anon.so\n\  
#LoadModule authn_dbd_module modules/mod_authn_dbd.so\n\  
#LoadModule authn_dbm_module modules/mod_authn_dbm.so\n\  
LoadModule authn_default_module modules/mod_authn_default.so\n\  
LoadModule authn_file_module modules/mod_authn_file.so\n\  
#LoadModule authz_dbm_module modules/mod_authz_dbm.so\n\  
LoadModule authz_default_module modules/mod_authz_default.so\n\  
LoadModule authz_groupfile_module modules/mod_authz_groupfile.so\n\  
LoadModule authz_host_module modules/mod_authz_host.so\n\  
LoadModule authz_owner_module modules/mod_authz_owner.so\n\  
LoadModule authz_user_module modules/mod_authz_user.so\n\  
#LoadModule authnz_ldap_module modules/mod_authnz_ldap.so\n\  
LoadModule autoindex_module modules/mod_autoindex.so\n\  
#LoadModule cache_module modules/mod_cache.so\n\  
#LoadModule disk_cache_module modules/mod_disk_cache.so\n\  
#LoadModule dbd_module modules/mod_dbd.so\n\  
LoadModule deflate_module modules/mod_deflate.so\n\  
LoadModule dir_module modules/mod_dir.so\n\  
#LoadModule dumpio_module modules/mod_dumpio.so\n\  
LoadModule env_module modules/mod_env.so\n\  
LoadModule expires_module modules/mod_expires.so\n\  
#LoadModule ext_filter_module modules/mod_ext_filter.so\n\  
LoadModule filter_module modules/mod_filter.so\n\  
LoadModule headers_module modules/mod_headers.so\n\  
#LoadModule include_module modules/mod_include.so\n\  
LoadModule info_module modules/mod_info.so\n\  
#LoadModule ldap_module modules/mod_ldap.so\n\  
LoadModule log_config_module modules/mod_log_config.so\n\  
LoadModule logio_module modules/mod_logio.so\n\  
#LoadModule mime_magic_module modules/mod_mime_magic.so\n\  
LoadModule mime_module modules/mod_mime.so\n\  
#LoadModule negotiation_module modules/mod_negotiation.so\n\  
LoadModule rewrite_module modules/mod_rewrite.so\n\  
LoadModule setenvif_module modules/mod_setenvif.so\n\  
LoadModule status_module modules/mod_status.so\n\  
#LoadModule substitute_module modules/mod_substitute.so\n\  
#LoadModule suexec_module modules/mod_suexec.so\n\  
#LoadModule unique_id_module modules/mod_unique_id.so\n\  
#LoadModule userdir_module modules/mod_userdir.so\n\  
LoadModule version_module modules/mod_version.so\n\  
#LoadModule vhost_alias_module modules/mod_vhost_alias.so\n\  
\n\  
#LoadModule asis_module modules/mod_asis.so\n\  
#LoadModule cern_meta_module modules/mod_cern_meta.so\n\  
#LoadModule ident_module modules/mod_ident.so\n\  
#LoadModule log_forensic_module modules/mod_log_forensic.so\n\  
#LoadModule usertrack_module modules/mod_usertrack.so\n\  
#LoadModule speling_module modules/mod_speling.so\n\  
" > ${file}; \  
printf "Done patching ${file}...\n"; \  
\  
# /etc/httpd/conf.modules.d/00-dav.conf \  
file="/etc/httpd/conf.modules.d/00-dav.conf"; \  
printf "\n# Applying configuration for ${file}...\n"; \  
# add load module \  
printf "\  
#LoadModule dav_module modules/mod_dav.so\n\  
#LoadModule dav_fs_module modules/mod_dav_fs.so\n\  
" > ${file}; \  
printf "Done patching ${file}...\n"; \  
\  
# /etc/httpd/conf.modules.d/00-proxy.conf \  
file="/etc/httpd/conf.modules.d/00-proxy.conf"; \  
printf "\n# Applying configuration for ${file}...\n"; \  
# add load module \  
printf "\  
# This file configures all the proxy modules:\n\  
LoadModule proxy_module modules/mod_proxy.so\n\  
#LoadModule proxy_ajp_module modules/mod_proxy_ajp.so\n\  
#LoadModule proxy_balancer_module modules/mod_proxy_balancer.so\n\  
#LoadModule proxy_connect_module modules/mod_proxy_connect.so\n\  
#LoadModule proxy_ftp_module modules/mod_proxy_ftp.so\n\  
LoadModule proxy_http_module modules/mod_proxy_http.so\n\  
" > ${file}; \  
printf "Done patching ${file}...\n"; \  
\  
# /etc/httpd/conf.modules.d/00-ssl.conf \  
file="/etc/httpd/conf.modules.d/00-ssl.conf"; \  
printf "\n# Applying configuration for ${file}...\n"; \  
# add load module \  
printf "\  
LoadModule ssl_module modules/mod_ssl.so\n\  
" > ${file}; \  
printf "Done patching ${file}...\n"; \  
\  
# /etc/httpd/conf.modules.d/01-cgi.conf \  
file="/etc/httpd/conf.modules.d/01-cgi.conf"; \  
printf "\n# Applying configuration for ${file}...\n"; \  
# add load module \  
printf "\  
# This configuration file loads a CGI module appropriate to the MPM\n\  
# which has been configured in 00-mpm.conf. mod_cgid should be used\n\  
# with a threaded MPM; mod_cgi with the prefork MPM.\n\  
\n\  
<IfModule mpm_worker_module>\n\  
# LoadModule cgid_module modules/mod_cgid.so\n\  
</IfModule>\n\  
<IfModule mpm_prefork_module>\n\  
# LoadModule cgi_module modules/mod_cgi.so\n\  
</IfModule>\n\  
" > ${file}; \  
printf "Done patching ${file}...\n"; \  
\  
# /etc/httpd/conf.modules.d/authnz_external.conf \  
file="/etc/httpd/conf.modules.d/authnz_external.conf"; \  
printf "\n# Applying configuration for ${file}...\n"; \  
# add load module \  
printf "LoadModule authnz_external_module modules/mod_authnz_external.so\n\n"
> ${file}; \  
printf "Done patching ${file}...\n"; \  
\  
# /etc/httpd/conf.modules.d/xsendfile.conf \  
file="/etc/httpd/conf.modules.d/xsendfile.conf"; \  
printf "\n# Applying configuration for ${file}...\n"; \  
# add load module \  
printf "LoadModule xsendfile_module modules/mod_xsendfile.so\n\n" > ${file}; \  
printf "Done patching ${file}...\n"; \  
\  
# /etc/httpd/conf/httpd.conf \  
file="/etc/httpd/conf/httpd.conf"; \  
printf "\n# Applying configuration for ${file}...\n"; \  
# replace load modules \  
perl -0p -i -e "s># LoadModule foo_module modules/mod_foo.so\n#\n># LoadModule
foo_module modules/mod_foo.so\n#\nInclude conf.modules.d/*.conf\n\n>" ${file};
\  
perl -0p -i -e "s>\nLoadModule .*>>g" ${file}; \  
perl -0p -i -e "s>#\n\# The following modules are not loaded by
default:\n\#\n\#\n\n\n>>" ${file}; \  
perl -0p -i -e "s>\n#LoadModule .*>>g" ${file}; \  
# add load module \  
perl -0p -i -e "s>LanguagePriority en .*>\<IfModule
negotiation_module\>\nLanguagePriority en ca cs da de el eo es et fr he hr it
ja ko ltz nl nn no pl pt pt-BR ru sv zh-CN zh-TW\n\</IfModule\>>" ${file}; \  
perl -0p -i -e "s>ForceLanguagePriority Prefer Fallback>\<IfModule
negotiation_module\>\nForceLanguagePriority Prefer Fallback\n\</IfModule\>>"
${file}; \  
printf "Done patching ${file}...\n"; \  
\  
# /etc/httpd/conf.d/ssl.conf \  
file="/etc/httpd/conf.d/ssl.conf"; \  
printf "\n# Applying configuration for ${file}...\n"; \  
# replace load module \  
perl -0p -i -e "s>LoadModule ssl_module modules/mod_ssl.so>\<IfModule
ssl_module\>>" ${file}; \  
printf "</IfModule>" >> ${file}; \  
printf "Done patching ${file}...\n"; \  
\  
# /etc/httpd/conf.d/xsendfile.conf \  
file="/etc/httpd/conf.d/xsendfile.conf"; \  
printf "\n# Applying configuration for ${file}...\n"; \  
rm -f ${file}; \  
printf "Done patching ${file}...\n"; \  
\  
# /etc/httpd/conf.d/authnz_external.conf \  
file="/etc/httpd/conf.d/authnz_external.conf"; \  
printf "\n# Applying configuration for ${file}...\n"; \  
# replace load module \  
perl -0p -i -e "s>LoadModule .*>\<IfModule authnz_external_module\>>" ${file};
\  
printf "</IfModule>" >> ${file}; \  
printf "Done patching ${file}...\n"; \  
\  
printf "Done enabling/disabling modules...\n"; \  
\  
printf "\n# Checking modules...\n"; \  
$(which apachectl) -l; $(which apachectl) -M; \  
printf "Done checking modules...\n"; \  
\  
printf "Finished installing modules...\n";  
  
#  
# Configuration  
#  
  
# Add users and groups  
RUN printf "Adding users and groups...\n"; \  
\  
printf "Add httpd user and group...\n"; \  
id -g ${app_httpd_global_user} || \  
groupadd \  
\--system ${app_httpd_global_group} && \  
id -u ${app_httpd_global_user} && \  
usermod \  
\--gid ${app_httpd_global_group} \  
\--home ${app_httpd_global_home} \  
\--shell /sbin/nologin \  
${app_httpd_global_user} \  
|| \  
useradd \  
\--system --gid ${app_httpd_global_group} \  
\--no-create-home --home-dir ${app_httpd_global_home} \  
\--shell /sbin/nologin \  
${app_httpd_global_user}; \  
\  
printf "Add vhost user and group...\n"; \  
app_httpd_vhost_home="${app_httpd_global_home}/${app_httpd_vhost_id}"; \  
id -g ${app_httpd_vhost_user} || \  
groupadd \  
\--system ${app_httpd_vhost_group} && \  
id -u ${app_httpd_vhost_user} && \  
usermod \  
\--gid ${app_httpd_global_group} \  
\--home ${app_httpd_vhost_home} \  
\--shell /sbin/nologin \  
${app_httpd_global_user} \  
|| \  
useradd \  
\--system --gid ${app_httpd_vhost_group} \  
\--create-home --home-dir ${app_httpd_vhost_home} \  
\--shell /sbin/nologin \  
${app_httpd_vhost_user}; \  
\  
printf "Setting vhost ownership and permissions...\n"; \  
mkdir -p ${app_httpd_vhost_home}/bin ${app_httpd_vhost_home}/log
${app_httpd_vhost_home}/html ${app_httpd_vhost_home}/tmp; \  
chown -R ${app_httpd_global_user}:${app_httpd_global_group}
${app_httpd_vhost_home}; \  
chmod -R ug=rwX,o=rX ${app_httpd_vhost_home}; \  
\  
printf "Finished adding users and groups...\n";  
  
# Supervisor  
RUN printf "Updading Supervisor configuration...\n"; \  
\  
# init is not working at this point \  
\  
# /etc/supervisord.conf \  
file="/etc/supervisord.conf"; \  
printf "\n# Applying configuration for ${file}...\n"; \  
printf "# HTTPd\n\  
[program:httpd]\n\  
command=/bin/bash -c \"\$(which apachectl) -d /etc/httpd -f
/etc/httpd/conf/httpd.conf -D FOREGROUND\"\n\  
autostart=true\n\  
autorestart=true\n\  
\n" >> ${file}; \  
printf "Done patching ${file}...\n"; \  
\  
printf "Finished updading Supervisor configuration...\n";  
  
# HTTPd  
RUN printf "Updading HTTPd configuration...\n"; \  
\  
# /etc/httpd/conf/httpd.conf \  
file="/etc/httpd/conf/httpd.conf"; \  
printf "\n# Applying configuration for ${file}...\n"; \  
# run as user/group \  
perl -0p -i -e "s># don't use Group #-1 on these systems!\n#\nUser .*\nGroup
.*># don't use Group #-1 on these systems!\n#\nUser
${app_httpd_global_user}\nGroup ${app_httpd_global_group}>" ${file}; \  
# change log level \  
perl -0p -i -e "s># alert, emerg.\n#\nLogLevel .*># alert, emerg.\n#\nLogLevel
${app_httpd_global_loglevel}>" ${file}; \  
# change config directory \  
perl -0p -i -e "s># Do NOT add a slash at the end of the directory
path.\n#\nServerRoot .*># Do NOT add a slash at the end of the directory
path.\n#\nServerRoot \"/etc/httpd\">" ${file}; \  
# replace optional config files \  
perl -0p -i -e "s>#\n# Load config files from the config directory
\"/etc/httpd/conf.d\".\n#\nInclude conf.d/*.conf>>" ${file}; \  
# replace ports with config file \  
perl -0p -i -e "s>#\n# Listen: Allows you to bind Apache to specific IP
addresses and/or\n# ports, in addition to the default. See also the
\<VirtualHost\>\n# directive.\n#\n# Change this to Listen on specific IP
addresses as shown below to \n# prevent Apache from glomming onto all bound IP
addresses \(0.0.0.0\)\n#\n#Listen 12.34.56.78:80\nListen 80\n\n>>" ${file}; \  
printf "\n\  
# Include list of ports to listen on\n\  
Include ports.conf\n\  
" >> ${file}; \  
# add vhost config files \  
printf "\n\  
# Include the virtual host configurations\n\  
Include sites.d/*.conf\n\  
" >> ${file}; \  
# change timeout \  
perl -0p -i -e "s># Timeout: The number of seconds before receives and sends
time out.\n#\nTimeout .*># Timeout: The number of seconds before receives and
sends time out.\n#\nTimeout ${app_httpd_global_listen_timeout}>" ${file}; \  
# change keepalive \  
perl -0p -i -e "s># one request per connection\). Set to \"Off\" to
deactivate.\n#\nKeepAlive .*># one request per connection\). Set to \"Off\" to
deactivate.\n#\nKeepAlive ${app_httpd_global_listen_keepalive_status}>"
${file}; \  
perl -0p -i -e "s># We recommend you leave this number high, for maximum
performance.\n#\nMaxKeepAliveRequests .*># We recommend you leave this number
high, for maximum performance.\n#\nMaxKeepAliveRequests
${app_httpd_global_listen_keepalive_requests}>" ${file}; \  
perl -0p -i -e "s># same client on the same connection.\n#\nKeepAliveTimeout
.*># same client on the same connection.\n#\nKeepAliveTimeout
${app_httpd_global_listen_keepalive_timeout}>" ${file}; \  
# add/replace main directory directives \  
perl -0p -i -e "s>\<Directory /\>\n\  
AllowOverride none\n\  
Allow from None\n\  
\</Directory\>>\<Directory /\>\n\  
Options FollowSymLinks\n\  
AllowOverride None\n\  
Allow from None\n\  
\</Directory\>\  
>" ${file}; \  
perl -0p -i -e "s>#\n# Each directory to which Apache has access can be
configured with respect>#\n\  
# Relax access to content within /var/www.\n\  
#\n\  
\<Directory \"/var/www\"\>\n\  
Options Indexes FollowSymLinks\n\  
AllowOverride None\n\  
\# Allow open access:\n\  
Allow from All\n\  
\</Directory\>\n\  
\n\  
\#\<Directory /srv/\>\n\  
\# Options Indexes FollowSymLinks\n\  
\# AllowOverride None\n\  
\# \# Allow open access:\n\  
\# Allow from All\n\  
\#\</Directory\>\n\  
\n\  
#\n# Each directory to which Apache has access can be configured with respect\  
>" ${file}; \  
printf "Done patching ${file}...\n"; \  
\  
# /etc/httpd/ports.conf \  
file="/etc/httpd/ports.conf"; \  
touch ${file}; \  
printf "\n# Applying configuration for ${file}...\n"; \  
printf "\  
# If you just change the port or add more ports here, you will likely also\n\  
# have to change the VirtualHost statement in\n\  
# /etc/httpd/sites.d/000-default.conf\n\  
\n\  
NameVirtualHost
${app_httpd_global_listen_addr}:${app_httpd_global_listen_port_http}\n\  
Listen ${app_httpd_global_listen_addr}:${app_httpd_global_listen_port_http}\n\  
\n\  
<IfModule ssl_module>\n\  
# If you add NameVirtualHost *:443 here, you will also have to change\n\  
# the VirtualHost statement in /etc/httpd/sites.d/000-default-ssl.conf\n\  
# to <VirtualHost *:443>\n\  
# Server Name Indication for SSL named virtual hosts is currently not\n\  
# supported by MSIE on Windows XP.\n\  
NameVirtualHost
${app_httpd_global_listen_addr}:${app_httpd_global_listen_port_https}\n\  
Listen
${app_httpd_global_listen_addr}:${app_httpd_global_listen_port_https}\n\  
</IfModule>\n\  
\n\  
<IfModule gnutls_module>\n\  
NameVirtualHost
${app_httpd_global_listen_addr}:${app_httpd_global_listen_port_https}\n\  
Listen
${app_httpd_global_listen_addr}:${app_httpd_global_listen_port_https}\n\  
</IfModule>\n\  
" > ${file}; \  
printf "Done patching ${file}...\n"; \  
\  
# /etc/httpd/conf.d/serve-cgi-bin.conf \  
file="/etc/httpd/conf.d/serve-cgi-bin.conf"; \  
printf "\n# Applying configuration for ${file}...\n"; \  
# add universal cgi-bin configuration \  
printf "<IfModule alias_module>\n\  
ScriptAlias /cgi-bin/ /var/www/cgi-bin\n\  
<Directory \"/var/www/cgi-bin\">\n\  
AllowOverride None\n\  
Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch\n\  
Order Allow,Deny\n\  
Allow from All\n\  
</Directory>\n\  
</IfModule>\n\  
\n" > ${file}; \  
printf "Done patching ${file}...\n"; \  
\  
# /etc/httpd/conf.d/security.conf \  
file="/etc/httpd/conf.d/security.conf"; \  
printf "\n# Applying configuration for ${file}...\n"; \  
# add security settings \  
printf "\n\  
# Changing the following options will not really affect the security of the\n\  
# server, but might make attacks slightly more difficult in some cases.\n\  
\n\  
#\n\  
# ServerTokens\n\  
# This directive configures what you return as the Server HTTP response\n\  
# Header. The default is 'Full' which sends information about the OS-Type\n\  
# and compiled in modules.\n\  
# Set to one of: Full | OS | Minimal | Minor | Major | Prod\n\  
# where Full conveys the most information, and Prod the least.\n\  
ServerTokens Minor\n\  
\n\  
#\n\  
# Optionally add a line containing the server version and virtual host\n\  
# name to server-generated pages (internal error documents, FTP directory\n\  
# listings, mod_status and mod_info output etc., but not CGI generated\n\  
# documents or custom error documents).\n\  
# Set to \"EMail\" to also include a mailto: link to the ServerAdmin.\n\  
# Set to one of: On | Off | EMail\n\  
ServerSignature On\n\  
\n" > ${file}; \  
printf "Done patching ${file}...\n"; \  
\  
# /etc/httpd/conf.d/ssl.conf \  
file="/etc/httpd/conf.d/ssl.conf"; \  
printf "\n# Applying configuration for ${file}...\n"; \  
# disable/replace badly configured defaults \  
perl -0p -i -e "s>Listen 443>>" ${file}; \  
perl -0p -i -e "s>.*SSLProtocol all .*>SSLProtocol all -SSLv2 -SSLv3>"
${file}; \  
perl -0p -i -e "s>.*SSLCipherSuite HIGH.*>SSLCipherSuite ECDHE-ECDSA-
CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-
SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-
AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-
ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-
AES256-SHA384:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-
AES256-SHA:ECDHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-
RSA-AES256-SHA256:DHE-RSA-AES256-SHA:ECDHE-ECDSA-DES-CBC3-SHA:ECDHE-RSA-DES-
CBC3-SHA:EDH-RSA-DES-CBC3-SHA:AES128-GCM-SHA256:AES256-GCM-
SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:DES-CBC3-SHA:!DSS>"
${file}; \  
perl -0p -i -e "s>.*SSLHonorCipherOrder on>SSLHonorCipherOrder On>" ${file}; \  
perl -0p -i -e "s>\n\</IfModule\>>\n\  
\n\  
\# See more information at:\n\  
\# https://mozilla.github.io/server-side-tls/ssl-config-
generator/\?server=apache-2.2.15\&openssl=1.0.1e\&hsts=no\&profile=intermediate\n\  
\n\</IfModule\>>" ${file}; \  
printf "Done patching ${file}...\n"; \  
\  
# Additional configuration files \  
mkdir /etc/httpd/incl.d; \  
\  
# HTTPd vhost \  
app_httpd_vhost_home="${app_httpd_global_home}/${app_httpd_vhost_id}"; \  
\  
# /etc/httpd/incl.d/${app_httpd_vhost_id}-httpd.conf \  
file="/etc/httpd/incl.d/${app_httpd_vhost_id}-httpd.conf"; \  
printf "\n# Applying configuration for ${file}...\n"; \  
printf "# HTTPd info and status\n\  
<IfModule info_module>\n\  
# HTTPd info\n\  
<Location /server-info>\n\  
SetHandler server-info\n\  
Allow from ${app_httpd_vhost_httpd_wlist}\n\  
</Location>\n\  
</IfModule>\n\  
<IfModule status_module>\n\  
# HTTPd status\n\  
<Location /server-status>\n\  
SetHandler server-status\n\  
Allow from ${app_httpd_vhost_httpd_wlist}\n\  
</Location>\n\  
</IfModule>\n\  
\n" > ${file}; \  
printf "Done patching ${file}...\n"; \  
\  
# Vhost configuration files \  
mkdir /etc/httpd/sites.d; \  
\  
# /etc/httpd/conf/httpd.conf \  
file="/etc/httpd/conf/httpd.conf"; \  
printf "\n# Applying configuration for ${file}...\n"; \  
# disable/replace badly configured default vhost \  
perl -0p -i -e "s>.*ServerAdmin root@localhost>#ServerAdmin root@localhost>"
${file}; \  
perl -0p -i -e "s>.*ServerName www.example.com:80>#ServerName
www.example.com:80>" ${file}; \  
perl -0p -i -e "s>.*DocumentRoot \"/var/www/html\">#DocumentRoot
\"/var/www/html\">" ${file}; \  
perl -0p -i -e "s>\<Directory \"/var/www/html\"\>>#\<Directory
\"/var/www/html\"\>>" ${file}; \  
perl -0p -i -e "s> Options Indexes FollowSymLinks># Options Indexes
FollowSymLinks>" ${file}; \  
perl -0p -i -e "s>#\n AllowOverride None>#\n# AllowOverride None>" ${file}; \  
perl -0p -i -e "s>#\n Order allow,deny\n Allow from all\n\n\</Directory\>>#\n#
Order Allow,Deny\n# Allow from All\n\n#\</Directory\>>" ${file}; \  
perl -0p -i -e "s>ScriptAlias /cgi-bin/ \"/var/www/cgi-bin/\">>" ${file}; \  
perl -0p -i -e "s>\<Directory \"/var/www/cgi-bin\"\>\n\  
AllowOverride None\n\  
Options None\n\  
Order allow,deny\n\  
Allow from all\n\  
\</Directory\>>>" ${file}; \  
printf "Done patching ${file}...\n"; \  
\  
# /etc/httpd/conf.d/ssl.conf \  
file="/etc/httpd/conf.d/ssl.conf"; \  
printf "\n# Applying configuration for ${file}...\n"; \  
# disable/replace badly configured default vhost \  
perl -0p -i -e "s>\<VirtualHost _default_:443\>>#\<VirtualHost
_default_:443\>>" ${file}; \  
perl -0p -i -e "s>.*DocumentRoot \"/var/www/html\">#DocumentRoot
\"/var/www/html\">" ${file}; \  
perl -0p -i -e "s>.*ServerAdmin root@localhost>#ServerAdmin root@localhost>"
${file}; \  
perl -0p -i -e "s>.*ServerName www.example.com:443>#ServerName
www.example.com:443>" ${file}; \  
perl -0p -i -e "s>.*ErrorLog logs/ssl_error_log\nTransferLog
logs/ssl_access_log\nLogLevel warn>#ErrorLog logs/ssl_error_log\n#TransferLog
logs/ssl_access_log\n#LogLevel warn>" ${file}; \  
perl -0p -i -e "s>.*SSLEngine on>#SSLEngine on>" ${file}; \  
perl -0p -i -e "s>.*SSLCertificateFile
/etc/pki/tls/certs/localhost.crt>#SSLCertificateFile
/etc/pki/tls/certs/localhost.crt>" ${file}; \  
perl -0p -i -e "s>.*SSLCertificateKeyFile
/etc/pki/tls/private/localhost.key>#SSLCertificateKeyFile
/etc/pki/tls/private/localhost.key>" ${file}; \  
perl -0p -i -e "s>.*SSLCertificateChainFile /etc/pki/tls/certs/server-
chain.crt>#SSLCertificateChainFile /etc/pki/tls/certs/server-chain.crt>"
${file}; \  
perl -0p -i -e "s>.*SSLCACertificateFile /etc/pki/tls/certs/ca-
bundle.crt>#SSLCACertificateFile /etc/pki/tls/certs/ca-bundle.crt>" ${file}; \  
perl -0p -i -e "s>\<Files ~>#\<Files ~>" ${file}; \  
perl -0p -i -e "s> SSLOptions \+StdEnvVars># SSLOptions \+StdEnvVars>"
${file}; \  
perl -0p -i -e "s>\</Files\>>#\</Files\>>" ${file}; \  
perl -0p -i -e "s>\<Directory \"/var/www/cgi-bin\"\>\n\  
SSLOptions \+StdEnvVars\n\  
\</Directory\>>#\<Directory \"/var/www/cgi-bin\"\>\n\  
# SSLOptions \+StdEnvVars\n\  
#\</Directory\>\  
>" ${file}; \  
perl -0p -i -e "s>CustomLog logs/ssl_request_log>#CustomLog
logs/ssl_request_log>" ${file}; \  
perl -0p -i -e "s> \"%t># \"%t>" ${file}; \  
perl -0p -i -e "s>\</VirtualHost\>>#\</VirtualHost\>>" ${file}; \  
printf "Done patching ${file}...\n"; \  
\  
# /etc/httpd/sites.d/${app_httpd_vhost_id}-http.conf \  
file="/etc/httpd/sites.d/${app_httpd_vhost_id}-http.conf"; \  
printf "\n# Applying configuration for ${file}...\n"; \  
printf "Done patching ${file}...\n"; \  
\  
# /etc/httpd/sites.d/${app_httpd_vhost_id}-https.conf \  
file="/etc/httpd/sites.d/${app_httpd_vhost_id}-https.conf"; \  
printf "\n# Applying configuration for ${file}...\n"; \  
printf "Done patching ${file}...\n"; \  
\  
printf "\n# Testing configuration...\n"; \  
echo "Testing $(which apachectl):"; $(which apachectl) -V; $(which apachectl)
configtest; $(which apachectl) -S; \  
printf "Done testing configuration...\n"; \  
\  
printf "Finished updading HTTPd configuration...\n";  
  

