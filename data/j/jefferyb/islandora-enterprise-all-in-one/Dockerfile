# To build, do:  
# docker build -t jefferyb/islandora-enterprise-all-in-one:7.x-1.7 --pull .  
#  
# To run, do:  
# docker rm -fv islandora-enterprise-all-in-one  
# docker run -d \  
# -h localhost \  
# --name islandora-enterprise-all-in-one \  
# -p 80:80 \  
# -p 8080:8080 \  
# -v islandora-mysql:/var/lib/mysql \  
# -v islandora-drupal:/var/www/html/sites/default \  
# -v islandora-fedora-data:/usr/local/fedora/data \  
# -v islandora-fedora-config:/usr/local/fedora/server/config \  
# -v islandora-solr:/usr/local/fedora/solr \  
# jefferyb/islandora-enterprise-all-in-one:7.x-1.7  
# docker logs -f islandora-enterprise-all-in-one  
FROM jefferyb/ansible:trusty  
MAINTAINER Jeffery Bagirimvano <jefferyb@uark.edu>  
  
ENV TERM=xterm  
ENV ISLANDORA_PLAYBOOK="/root/islandora-7.x-Enterprise"  
RUN \  
git clone -b islandora-7.x-1.7
https://github.com/jefferyb/islandora-7.x-enterprise-ansible.git
${ISLANDORA_PLAYBOOK} && \  
cd ${ISLANDORA_PLAYBOOK} && \  
ansible-playbook install-islandora-7.x-enterprise.yaml && \  
service apache2 stop && \  
pkill java && \  
service mysql stop && \  
rm -f /var/log/tomcat7/*  
  
# MYSQL  
VOLUME /var/lib/mysql  
# FEDORA  
VOLUME /usr/local/fedora/data  
VOLUME /usr/local/fedora/server/config  
# DRUPAL  
VOLUME /var/www/html/sites  
# SOLR  
VOLUME /usr/local/fedora/solr  
  
WORKDIR ${ISLANDORA_PLAYBOOK}  
  
EXPOSE 80 3306 8080  
CMD \  
ansible-playbook install-islandora-7.x-enterprise.yaml && \  
drush --root=/var/www/html -y updatedb && \  
drush --root=/var/www/html -y core-cron && \  
tail -f /var/log/tomcat7/catalina.out \  
-f /var/log/apache2/*.log \  
-f /usr/local/fedora/server/logs/fedora.log \  
-f /usr/local/fedora/server/logs/fedoragsearch.daily.log  

