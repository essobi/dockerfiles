FROM treesoftware/docker-orocommerce-platform  
MAINTAINER Egor Zyuskin <e.zyuskin@tree-soft.com>  
  
ADD ./etc/yum.repos.d/ /etc/yum.repos.d/  
  
RUN yum install -y docker-engine npm unzip  
  
ADD ./etc/supervisord.d/ /etc/supervisord.d/  
ADD ./usr/ /usr/  
  
RUN composer global require escapestudios/symfony2-coding-standard:~2.0 && \  
~/.composer/vendor/bin/phpcs --config-set installed_paths
~/.composer/vendor/escapestudios/symfony2-coding-standard  
  
EXPOSE 80 9001  
ENTRYPOINT ["/usr/sbin/container-entrypoint.sh"]  
CMD ["supervisord", "--nodaemon"]  

