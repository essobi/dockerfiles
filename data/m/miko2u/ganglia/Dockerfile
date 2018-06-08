FROM miko2u/web56  
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
&& yum -y install ssmtp \  
&& sed -e 's/^pm.max_children =.*$/pm.max_children = 8/g' \  
-e 's/^pm.start_servers =.*$/pm.start_servers = 2/g' \  
-e 's/^pm.min_spare_servers =.*$/pm.min_spare_servers = 2/g' \  
-e 's/^pm.max_spare_servers =.*$/pm.max_spare_servers = 4/g' \  
-i.dist /etc/php-fpm.d/www.conf \  
&& yum -y install --enablerepo=remi,remi-php56 ganglia ganglia-gmetad ganglia-
gmond ganglia-gmond-python ganglia-web \  
&& find / -xdev -group ganglia -exec chgrp 117 {} \; && groupmod -g 117
ganglia \  
&& find / -xdev -user ganglia -exec chown 117 {} \; && usermod -u 117 ganglia
\  
&& curl -OL https://code.jquery.com/jquery-3.1.0.min.js \  
&& curl -OL https://github.com/mbostock/protovis/raw/v3.3.1/protovis.min.js \  
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
&& chkconfig php-fpm on \  
&& yum -y --enablerepo=remi,remi-php56 clean all \  
&& rm -rf /tmp/* /var/tmp/* /var/lib/yum/* /var/cache/yum/* \  
&& ln -sf /dev/stderr /var/log/messages  
  
COPY rrdcached /etc/rc.d/init.d/rrdcached  
  
# startup  
COPY prepare post /boot/  

