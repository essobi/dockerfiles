FROM minity/php54-console  
  
RUN apt-get -yq update  
  
# php5-fpm  
RUN DEBIAN_FRONTEND=noninteractive apt-get -yq install php5-fpm cron  
  
RUN ln -sf /dev/stderr /var/log/php5-fpm.log  
  
RUN echo "18,48 * * * * find /var/lib/php5 -type f -name 'sess_*' -cmin +30
-delete" | crontab  
  
COPY fpm-pool.conf /etc/php5/fpm/pool.d/www.conf  
  
# nullmailer  
RUN DEBIAN_FRONTEND=noninteractive apt-get -yq install nullmailer  
  
# nginx  
RUN DEBIAN_FRONTEND=noninteractive apt-get -yq install nginx-light  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
RUN mkdir /etc/nginx/default.d  
COPY nginx-site.conf /etc/nginx/sites-enabled/default  
  
RUN echo 'log_format fcgi '\'' === fcgi vars for "$uri":
realpath_root="$realpath_root"; '\''\n
'\''fastcgi_script_name="$fastcgi_script_name"; '\''\n
'\''fastcgi_path_info="$fastcgi_path_info"'\'\; > /etc/nginx/conf.d/fcgi-log-
format.conf  
  
VOLUME ["/var/cache/nginx"]  
  
EXPOSE 80  
RUN mkdir /init.d  
  
ADD init.sh /init.sh  
ADD run.sh /run.sh  
  
CMD /run.sh  
  
# finish  
RUN apt-get clean all && rm -rf /var/lib/apt/lists/*  

