# roundcube-docker-image  
# Copyright (C) 2014 jitakizushi  
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
FROM ubuntu:14.04  
MAINTAINER jitakizushi jitakizushi@gmx.com  
  
RUN apt-get -qq update  
# Configure database for roundcube with dbconfig-common,  
# Database type to be used by roundcube  
RUN { echo "roundcube-core roundcube/dbconfig-install boolean true"; \  
echo "roundcube-core roundcube/database-type select sqlite3"; \  
} |debconf-set-selections  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy install \  
roundcube roundcube-sqlite3 curl php5-ldap  
  
RUN sed -i -re '/^\s*DocumentRoot/s, /.*, /var/lib/roundcube,' \  
/etc/apache2/sites-available/000-default.conf \  
/etc/apache2/sites-available/default-ssl.conf  
  
RUN a2ensite 000-default  
RUN a2ensite default-ssl  
RUN a2enmod ssl  
RUN php5enmod mcrypt  
  
ADD docker-rc-init.sh /usr/local/sbin/  
EXPOSE 80 443  
CMD ["/usr/local/sbin/docker-rc-init.sh"]  
# DB in /var/lib/dbconfig-common/sqlite3/roundcube, mount as volume to persist  

