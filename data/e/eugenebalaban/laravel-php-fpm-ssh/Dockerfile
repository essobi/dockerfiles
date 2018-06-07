FROM eugenebalaban/laravel-php-fpm-debug  
  
RUN apk --update add openssh \  
&& sed -i s/#PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config \  
&& echo "root:root" | chpasswd \  
&& rm -rf /var/cache/apk/*  
  
COPY entrypoint.sh /entrypoint.sh  
  
RUN chmod 777 /entrypoint.sh \  
&& ln -s /usr/local/bin/php /usr/bin/php  
  
EXPOSE 22  
ENTRYPOINT ["/entrypoint.sh"]

