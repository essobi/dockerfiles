# guacamole with mysql authentication  
FROM hall/guacamole  
MAINTAINER Randy Hall <randy.hall@open-source.guru>  
  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh || true  
RUN apt-get update && \  
apt-get -y install mysql-client && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
ENV GUACAMOLE_DB guacamole  
ADD guacdb /usr/local/bin/guacdb  
ADD rc.local /etc/rc.local  
RUN chmod a+x /etc/rc.local &&\  
chmod a+x /usr/local/bin/guacdb  

