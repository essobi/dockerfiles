### Dockerfile for guacamole  
### Includes all the optional authentication modules preinstalled  
FROM hall/guacamole  
MAINTAINER Randy Hall <randy.hall@open-source.guru>  
CMD ["/usr/local/sbin/guacd","-b","0.0.0.0","-p","/var/run/guacd.pid","-f"]  
EXPOSE 4822  
### cleanup  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh
/etc/rc.local  
  

