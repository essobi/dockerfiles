FROM debian:wheezy  
  
MAINTAINER Eriksen Costa <eriksencosta@gmail.com>  
  
COPY ansible-php-dev /opt/ansible  
  
RUN DEBIAN_FRONTEND=noninteractive; \  
apt-get update; \  
apt-get install -y \  
python \  
python-pip \  
python-dev; \  
pip install ansible; \  
rm /opt/ansible/.git; \  
ansible-playbook \  
-i /opt/ansible/inventories/local \  
-c local \  
\--extra-vars "php_build_releases=all composer_clean_cache=true" \  
/opt/ansible/site.yml; \  
pip uninstall -y ansible; \  
apt-get remove --purge -y \  
python-apt-common \  
python-apt \  
python-pip \  
python-dev \  
python-minimal \  
python \  
lsb-release; \  
apt-get autoremove -y; \  
apt-get clean; \  
rm -rf /var/lib/apt/lists/*; \  
rm -rf /var/cache/apt; \  
rm -rf /usr/lib/python*; \  
rm -rf /tmp/*;  
  
VOLUME ["/var/log/nginx", "/var/log/php-fpm", "/var/log/php", "/var/www"]  
  
EXPOSE 80 9000  
  
CMD ["/usr/local/bin/webserver", "--foreground", "--redirect-logs", "start"]  

