FROM stowers/php-base:7.1  
  
LABEL maintainer="eric.poe@gmail.com"  
  
# Set up MySQL Client  
RUN yum update && \  
yum install -y mysql  
  
COPY resources/usr/local/etc/php/php.ini /usr/local/etc/php/  
  
# Set up Apache  
COPY resources/etc/httpd/conf/httpd.conf /etc/httpd/conf/httpd.conf  
  
WORKDIR /var/www/html/Symfony  
  
# Create user to run webserver and shell commands as  
# These need to be the same because the web app requires writable access to
many  
# directories  
RUN useradd --create-home --uid 5000 --shell /bin/bash limsuser && \  
usermod \--lock limsuser && \  
chown -R limsuser:limsuser ~limsuser/  
  
#  
# a+r on /root/.bash_profile to prevent error message when doing su -p -
limsuser in shell commands  
#  
RUN echo "Configuring directories..." \  
&& mkdir -p /var/lims/composer/vendor \  
&& mkdir -p /var/lims/composer/cache \  
&& mkdir -p /var/lims/composer/bin \  
&& mkdir -p /var/lims/symfony/bootstrap \  
&& mkdir -p /var/lims/symfony/cache \  
&& mkdir -p /var/lims/symfony/logs \  
&& mkdir -p /var/lims/symfony/www \  
&& mkdir -p /var/lims/symfony/sessions \  
&& mkdir -p /var/lims/datastore \  
&& mkdir -p /var/lims/zanmodules/smarty \  
&& mkdir -p /var/lims/environment \  
&& mkdir -p /var/lims/external-drives/n/projects \  
\  
&& chown -R limsuser:limsuser /var/lims \  
&& echo "DONE"  
  
COPY resources/root/docker-entrypoint.sh /root/  
COPY resources/usr/local/bin/dockerlims-shell /usr/local/bin/  
COPY resources/usr/local/bin/dockerlims-test /usr/local/bin/  
  
COPY resources/var/lims/setup/legacy-setup.sql /var/lims/setup/  
COPY resources/var/lims/setup/setup.sql /var/lims/setup/  
  
COPY resources/var/lims/environment/test /var/lims/environment/  
  
COPY resources/home/limsuser/.zan/zanmodules-defaults /home/limsuser/.zan/  
COPY resources/home/limsuser/bin/auto-sf-console /home/limsuser/bin/  
COPY resources/home/limsuser/.profile /home/limsuser/  
  
# NOTE: must use json syntax process is not started in a subshell (and signals
are passed correctly)  
ENTRYPOINT ["/root/docker-entrypoint.sh"]

