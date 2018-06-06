FROM uazlibraries/debian-shibboleth-sp:debian9-shibboleth2.6  
  
# Make apt-get commands temporarily non-interactive  
# Solution from https://github.com/phusion/baseimage-docker/issues/58  
# Update apt cache to use fastest local mirror  
RUN \  
export DEBIAN_FRONTEND=noninteractive && \  
export DEBCONF_NONINTERACTIVE_SEEN=true && \  
apt-get update && \  
apt-get install -y supervisor libcgi-fast-perl ruby-fcgi python-fcgi && \  
apt-get clean  
  
COPY supervisor/shibboleth.conf /etc/supervisor/conf.d/  
  
ENTRYPOINT ["/usr/bin/supervisord", "--nodaemon"]  

