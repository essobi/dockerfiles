# Pull base image  
FROM phalconphp/php-apache:ubuntu-16.04  
MAINTAINER Gamal Abdul Nasser <gamalanpro@gmail.com>  
  
ENV PROVISION_CONTEXT "production"  
# Deploy scripts/configurations  
COPY bin/*.sh /opt/docker/provision/entrypoint.d/  
  
RUN mkdir -p /vendor \  
&& composer --working-dir=/vendor require phalcon/devtools \  
&& ln -s /vendor/vendor/phalcon/devtools/phalcon.php /usr/local/bin/phalcon \  
&& chmod ugo+x /usr/local/bin/phalcon \  
&& composer --working-dir=/vendor require robmorgan/phinx \  
&& ln -s /vendor/vendor/robmorgan/phinx/bin/phinx /usr/local/bin/phinx \  
&& chmod ugo+x /usr/local/bin/phinx \  
# Custom provisions  
&& chmod +x /opt/docker/provision/entrypoint.d/*.sh  
  
RUN apt-get update && apt-get install nano vim htop telnet traceroute dnsutils
iputils-ping bash-completion tmux -y && apt-get clean -y

