FROM php:5.6.31-apache  
  
# Install mcrypt, git, ssh-client  
RUN apt-get update &&\  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
mcrypt php5-mcrypt libmcrypt-dev nano git ssh-client &&\  
docker-php-ext-install mcrypt &&\  
apt-get clean && rm -rf /tmp/* /var/tmp/* && rm -rf /var/lib/apt/lists/*  
RUN echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config &&\  
echo "UserKnownHostsFile /dev/null" >> /etc/ssh/ssh_config  
  
RUN a2enmod rewrite  
  
# OpenShift Origin runs containers using an arbitrarily assigned user ID  
# (random UID) and root group. The user ID of the container is generated  
# dynamically, it will not have an associated entry in /etc/passwd.  
# https://docs.openshift.org/latest/creating_images/guidelines.html  
# Thus, in order to drop the root user, we have to:  
# 1. Run apache2 on a custom port (8080), a non-root user does not have access
to port 80.  
# 2. Make some directories world writeable.  
# https://askubuntu.com/a/338239  
# https://github.com/openshift/origin/issues/6629  
RUN sed -i "s/Listen 80/Listen 8080/g" /etc/apache2/ports.conf &&\  
sed -i "s/<VirtualHost \\*:80>/<VirtualHost \\*:8080>/g" /etc/apache2/sites-
enabled/000-default.conf  
RUN mkdir -p /var/run/apache2 && chmod 777 -R /var/run/apache2 &&\  
mkdir -p /var/log/apache2 && chmod 777 -R /var/log/apache2 &&\  
mkdir -p /var/lock/apache2 && chmod 777 -R /var/lock/apache2 &&\  
mkdir -p /etc/apache2/sites-enabled && chmod 777 -R /etc/apache2/sites-enabled
&&\  
mkdir -p /var/www/html && chmod 777 -R /var/www/html  
# Compare also with:  
# https://github.com/sclorg/s2i-php-container/  
# https://github.com/openshift-qe/ssh-git-docker/blob/master/ssh-git-
openshift/Dockerfile  
COPY docker-php-entrypoint /usr/local/bin/  
RUN chmod 755 /usr/local/bin/docker-php-entrypoint &&\  
chmod 664 /etc/passwd &&\  
mkdir -p /home/openshift &&\  
chmod 777 -R /home/openshift  

