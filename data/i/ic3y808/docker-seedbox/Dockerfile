FROM ic3y808/docker-lemp  
MAINTAINER Jesse Nelson "lordkoi303@gmail.com"  
LABEL org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.license="MIT" \  
org.label-schema.name="Docker Seedbox" \  
org.label-schema.vcs-type="Git" \  
org.label-schema.vcs-url="https://github.com/ic3y808/docker-seedbox"  
EXPOSE 22 80 443 9091  
VOLUME /etc/transmission-daemon/torrents  
VOLUME /etc/transmission-daemon/resume  
VOLUME /etc/transmission-daemon/blocklists  
VOLUME /var/lib/transmission-daemon  
VOLUME /usr/share/nginx/tracker/torrents  
VOLUME /usr/share/nginx/tracker/config  
RUN add-apt-repository ppa:transmissionbt/ppa && apt-get update && apt-get
install --no-install-recommends -y apache2-utils nginx php5-cli php5-fpm
php5-mysql php5-mcrypt transmission-cli transmission-common transmission-
daemon  
ADD ./scripts/ /scripts/  
RUN chmod +x /scripts/startup.sh  
RUN chmod +x /scripts/startup_background.sh  
CMD ["/bin/bash", "/scripts/startup.sh"]

