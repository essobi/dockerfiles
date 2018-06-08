FROM bgruening/galaxy-stable  
MAINTAINER Yannick Cogne  
WORKDIR /galaxy-central  
RUN mkdir $GALAXY_ROOT/tools/docker  
ADD tools/*.xml $GALAXY_ROOT/tools/docker/  
ADD conf/job_conf.xml.sample_basic $GALAXY_ROOT/config/job_conf.xml  
ADD conf/tool_conf.xml $GALAXY_ROOT/config/tool_conf.xml  
RUN echo "galaxy ALL = (root) NOPASSWD: SETENV: /usr/bin/docker" >>
/etc/sudoers  
ADD script/docker_pulling.sh $GALAXY_ROOT/  
RUN chmod +x docker_pulling.sh  
VOLUME ["/export/", "/data/", "/var/lib/docker","/backup"]  
RUN mkdir $GALAXY_CONFIG_DIR/web/img_web/  
ADD img_web/* $GALAXY_CONFIG_DIR/web/img_web/  
ADD script/save_duplicity.monthly /etc/cron.monthly  
RUN chmod 755 /etc/cron.monthly/save_duplicity.monthly  
ADD script/save_duplicity.daily /etc/cron.daily/  
RUN chmod 755 /etc/cron.daily/save_duplicity.daily  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y duplicity  
RUN apt-get clean  
ADD web/welcome.html $GALAXY_CONFIG_DIR/web/welcome.html  
# Expose port 80 (webserver), 21 (FTP server),22 (SFTP server), 8800 (Proxy)  
EXPOSE :80  
EXPOSE :21  
EXPOSE :8800  
EXPOSE :22  
ADD /conf/crontab /etc  
RUN crontab /etc/crontab  
# Autostart script that is invoked during container start  
CMD ["/usr/bin/startup"]  

