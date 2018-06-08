FROM miko2u/web  
MAINTAINER miko@cafelounge.net  
  
# packages  
RUN cd /tmp \  
&& printf "[cafelounge]\n\  
name=cafelounge repository for CentOS \$releasever - \$basearch\n\  
baseurl=http://repo.cafelounge.net/yum/el/\$releasever/\$basearch/\n\  
gpgcheck=1\n\  
enabled=0\n\  
gpgkey=http://repo.cafelounge.net/yum/el/\$releasever/RPM-GPG-KEY-
cafelounge\n\  
" > /etc/yum.repos.d/cafelounge.repo \  
&& yum -y update \  
&& yum -y install ssmtp spawn-fcgi perl-libwww-perl perl-Crypt-SSLeay \  
&& sed -e 's/^pm.max_children =.*$/pm.max_children = 8/g' \  
-e 's/^pm.start_servers =.*$/pm.start_servers = 2/g' \  
-e 's/^pm.min_spare_servers =.*$/pm.min_spare_servers = 2/g' \  
-e 's/^pm.max_spare_servers =.*$/pm.max_spare_servers = 4/g' \  
-i.dist /etc/php-fpm.d/www.conf \  
&& yum -y install --enablerepo=remi,remi-php56,cafelounge \  
nagios nagios-common fcgiwrap \  
&& find / -xdev -group nagios -exec chgrp 119 {} \; && groupmod -g 119 nagios
\  
&& find / -xdev -user nagios -exec chown 119 {} \; && usermod -u 119 nagios \  
&& sed -e "s/^date_format=us/date_format=iso8601/g" \  
-i.dist /etc/nagios/nagios.cfg \  
&& sed -e "s/nagios@localhost.*$/{{REPLACE_ADMIN_EMAIL}}/g" \  
-i.dist /etc/nagios/objects/contacts.cfg \  
&& sed -e "s/^mailhub=.*$/mailhub={{REPLACE_MAILHUB}}/g" \  
-i.dist /etc/ssmtp/ssmtp.conf \  
&& htpasswd -bc /etc/nagios/passwd nagiosadmin nagiosadmin \  
&& mkdir -p /var/run/nagios \  
&& yum -y install --enablerepo=remi nrpe \  
&& find / -xdev -group nrpe -exec chgrp 118 {} \; && groupmod -g 118 nrpe \  
&& find / -xdev -user nrpe -exec chown 118 {} \; && usermod -u 118 nrpe \  
&& yum -y install --enablerepo=remi nagios-plugins nagios-plugins-dummy \  
nagios-plugins-load nagios-plugins-users nagios-plugins-http \  
nagios-plugins-ping nagios-plugins-disk nagios-plugins-ssh nagios-plugins-dig
\  
nagios-plugins-swap nagios-plugins-procs nagios-plugins-nrpe \  
nagios-plugins-nagios nagios-plugins-by_ssh nagios-plugins-perl \  
ganglia ganglia-gmetad ganglia-gmond ganglia-gmond-python ganglia-web \  
&& find / -xdev -group ganglia -exec chgrp 117 {} \; && groupmod -g 117
ganglia \  
&& find / -xdev -user ganglia -exec chown 117 {} \; && usermod -u 117 ganglia
\  
&& curl -OL http://code.jquery.com/jquery-1.9.1.min.js \  
&& curl -OL
https://raw.githubusercontent.com/mbostock/protovis/v3.2.0/protovis-r3.2.js \  
&& cp *.js /usr/share/ganglia/js \  
&& yum -y localinstall
http://repo.cafelounge.net/yum/el/testing/6/x86_64/rrdtool-1.5.5-4.el6.x86_64.rpm
\  
&& printf "#\n\  
RRDCACHED_USER=ganglia\n\  
SOCKFILE=\"/var/run/rrdcached/rrdcached.sock\"\n\  
SOCKGROUP=apache\n\  
SOCKPERMS=0664\n\  
#\n\  
OPTIONS=\"-l 127.0.0.1 -F -w 1800 -z 1800 -f 3600\"\n\  
" > /etc/sysconfig/rrdtool \  
&& printf 'RRDCACHED_ADDRESS="unix:/var/run/rrdcached/rrdcached.sock"' >
/etc/sysconfig/gmetad \  
&& chown -R ganglia:apache /var/run/rrdcached \  
&& chkconfig rrdcached on \  
&& chkconfig gmetad on \  
&& chkconfig nagios on \  
&& chkconfig spawn-fcgi on \  
&& chkconfig php-fpm on \  
&& yum -y --enablerepo=remi,remi-php56 clean all \  
&& rm -rf /tmp/* /var/tmp/* /var/lib/yum/* /var/cache/yum/* \  
&& usermod -aG nagios nginx \  
&& usermod -aG mail nagios \  
&& ln -sf /dev/stderr /var/log/messages  
  
COPY rrdcached /etc/rc.d/init.d/rrdcached  
COPY spawn-fcgi /etc/sysconfig/spawn-fcgi  
  
# optional: Support Slack  
RUN curl -kL -o /usr/local/bin/slack_nagios
https://raw.github.com/tinyspeck/services-examples/master/nagios.pl \  
&& chmod 755 /usr/local/bin/slack_nagios \  
&& chown root:root /usr/local/bin/slack_nagios \  
&& sed -e 's/foo.slack.com/{{REPLACE_SLACK_HOSTS}}/g' \  
-e 's/opt_token = ""/opt_token = "{{REPLACE_SLACK_TOKEN}}"/g' \  
-i /usr/local/bin/slack_nagios  
  
# startup  
COPY prepare post /boot/  

