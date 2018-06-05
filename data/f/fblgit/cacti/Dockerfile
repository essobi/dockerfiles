#name of container: ubuntu-cacti  
#version of container 0.1  
FROM fblgit/ubuntu-base  
MAINTAINER FBLGIT  
VOLUME /var/lib/cacti/rra  
VOLUME /var/lib/mysql  
RUN sed -i '/session required pam_loginuid.so/c\\#session required
pam_loginuid.so' /etc/pam.d/cron  
COPY files/ubuntu-cacti.sh /data/ubuntu-cacti.sh  
RUN chmod +x /data/*.sh  
ENTRYPOINT ["/data/ubuntu-cacti.sh"]  

