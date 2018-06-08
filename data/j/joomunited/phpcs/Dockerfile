FROM php:7.1.1  
#Workaround to enable nano  
ENV TERM xterm  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y unzip git curl openssh-server  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN composer global require "squizlabs/php_codesniffer=3.2.3"  
RUN echo "export
PATH=$PATH:/root/.composer/vendor/squizlabs/php_codesniffer/bin/" >>
/root/.bashrc  
RUN composer global require "wp-coding-standards/wpcs"  
RUN composer global require "wimg/php-compatibility"  
  
COPY usr/local/bin/ /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker_entrypoint.sh
/usr/local/bin/sshd_foreground.sh  
  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN echo "root:password" | chpasswd  
  
RUN sed -i 's/^Port .*/Port 2223/g' /etc/ssh/sshd_config  
RUN sed -i 's/^PermitRootLogin .*/PermitRootLogin yes/g' /etc/ssh/sshd_config  
  
ENTRYPOINT ["docker_entrypoint.sh"]  
CMD ["sshd_foreground.sh"]  

