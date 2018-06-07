FROM minity/php54-webapp  
  
RUN apt-get -yq update  
  
# php5-xdebug  
RUN DEBIAN_FRONTEND=noninteractive apt-get -yq install php5-xdebug  
  
RUN echo 'xdebug.remote_enable =
1\nxdebug.remote_connect_back=1\nxdebug.max_nesting_level=300' >
/etc/php5/conf.d/xdebug-debugger-enable.ini  
  
# xhprof  
RUN DEBIAN_FRONTEND=noninteractive apt-get -yq install graphviz  
  
ADD https://dl.dropboxusercontent.com/u/19430078/php54-xhprof.tar.bz2 /tmp/  
  
RUN tar xjf /tmp/php54-xhprof.tar.bz2 -C /tmp \  
&& cp /tmp/xhprof/xhprof.so /usr/lib/php5/20100525/ \  
&& mkdir -p /usr/share/php \  
&& cp -R /tmp/xhprof/xhprof_* /usr/share/php \  
&& rm /tmp/php54-xhprof.tar.bz2 \  
&& rm -R /tmp/xhprof  
  
VOLUME ["/tmp/xhprofiles"]  
  
RUN echo 'extension=xhprof.so\nxhprof.output_dir=/tmp/xhprofiles' >
/etc/php5/conf.d/xhprof.ini  
RUN echo 'location /.xhp/ {alias /usr/share/php/xhprof_html/;
fastcgi_split_path_info ^/.xhp(/.+\\.php)(.*)$; location ~ \\.php$
{fastcgi_index index.php; fastcgi_pass unix:/var/run/php.sock; include
fastcgi_params; fastcgi_param SCRIPT_FILENAME
$document_root$fastcgi_script_name; access_log /dev/stdout fcgi;}}' >
/etc/nginx/default.d/xhprof.conf  
RUN echo 'chown user:user /tmp/xhprofiles' > /init.d/xhprof  
  
# finish  
RUN apt-get clean all && rm -rf /var/lib/apt/lists/*  

