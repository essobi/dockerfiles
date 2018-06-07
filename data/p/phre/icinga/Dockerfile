# docker-icinga  
# Copyright (C) 2014 phre <phre@gmx.com>  
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
FROM phre/supervisor-stdout  
MAINTAINER phre phre@gmx.com  
  
RUN apt-get -qq update  
RUN apt-get -y install python-software-properties wget  
  
# For latest icinga  
RUN add-apt-repository -y ppa:formorer/icinga  
  
# For latest PostgreSQL client (needed for creating/updating the db on servers  
# running latest version)  
RUN add-apt-repository -y \  
"deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main"  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |\  
apt-key add -  
  
RUN apt-get -qq update  
  
# possible race between icinga-cgi and apache2; icinga-cgi postconf tries to  
# invoke-rc.d apache2 but only recomends 'apache2 | httpd'; as a workaround  
# just install apache2 first  
# also stop it and clean up logs (postinst starts it, but this leaves
confusing  
# warnings in the logs if it's not shut down cleanly)  
RUN apt-get -y install apache2 libapache2-mod-php5 &&\  
service apache2 stop && rm -f /var/log/apache2/*  
  
# pre-seed some defaults for icinga  
RUN printf '%s\n' \  
'dbconfig-common dbconfig-common/remote-questions-default boolean true' \  
'icinga-cgi icinga/adminpassword password admin' \  
'icinga-cgi icinga/adminpassword-repeat password admin' \  
'icinga-common icinga/check_external_commands boolean true' \  
'icinga-idoutils icinga-idoutils/dbconfig-install boolean false' \  
'icinga-web icinga-web/dbconfig-install boolean false' \  
|debconf-set-selections  
  
# prevent dbconfig-common from trying to configure DB settings on install  
# (we don't know the details yet)  
RUN install -d -o root -g root -m 755 /etc/dbconfig-common &&\  
echo 'dbc_install=false' |\  
tee /etc/dbconfig-common/icinga-web.conf > \  
/etc/dbconfig-common/icinga-idoutils.conf &&\  
chmod 600 /etc/dbconfig-common/icinga-*.conf  
  
# apg for generating passwords; msmtp for sending emails  
RUN apt-get -y install icinga icinga-idoutils icinga-web \  
libdbd-pgsql php5-pgsql postgresql-client apg msmtp-mta  
RUN cp /usr/share/doc/icinga-idoutils/examples/idoutils.cfg-sample \  
/etc/icinga/modules/idoutils.cfg  
  
# allow user nagios to send mail (see di_configure_msmtp in functions.sh)  
RUN gpasswd -a nagios mail  
  
# init scripts  
ADD docker_icinga_functions.sh /usr/local/lib/  
ADD docker_icinga_start.sh /usr/local/sbin/  
  
# supervisor services  
ADD ./supervisor.d /etc/supervisor/conf.d  
  
# ports of provided services  
# 80 : icinga web interface  
EXPOSE 80  
CMD ["/usr/local/sbin/docker_icinga_start.sh"]  

