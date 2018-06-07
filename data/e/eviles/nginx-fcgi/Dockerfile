FROM eviles/nginx  
  
RUN yum -y install epel-release \  
&& yum -y groupinstall 'Development Tools' \  
&& yum -y install net-tools libstdc++ libstdc++.i686 libcurl libcurl.i686
fcgi-devel spawn-fcgi \  
&& yum clean all \  
&& rm -rf /var/cache/yum/* \  
&& cd /usr/local/src/ \  
&& git clone https://github.com/gnosek/fcgiwrap.git \  
&& cd fcgiwrap \  
&& autoreconf -i \  
&& ./configure \  
&& make \  
&& make install \  
&& echo "[fcgi-program:fcgiwrap]" >> /etc/supervisord.conf \  
&& echo "command=/usr/local/sbin/fcgiwrap" >> /etc/supervisord.conf \  
&& echo "user=nginx" >> /etc/supervisord.conf \  
&& echo "socket=unix:///var/run/%(program_name)s.sock" >>
/etc/supervisord.conf \  
&& echo "socket_owner=nginx:nginx" >> /etc/supervisord.conf \  
&& echo "socket_mode=0770" >> /etc/supervisord.conf \  
&& localedef -i zh_TW -c -f UTF-8 zh_TW.UTF-8  
  
ENV LC_ALL=zh_TW.UTF-8  

