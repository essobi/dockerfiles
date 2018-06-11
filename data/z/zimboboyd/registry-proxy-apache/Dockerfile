FROM centos:centos6  
  
# Update, Install Node, Cleanup  
RUN yum --setopt=tsflags=nodocs -y update \  
&& yum --setopt=tsflags=nodocs -y install httpd mod_ssl \  
&& rm -rf /var/cache/yum/* \  
&& yum clean all  
  
# The domain this host should run under (should match SSL cert)  
ENV REGISTRY_HOSTNAME "reg.your.domain"  
# Verbosity of logging (see apache LogLevel directive)  
ENV PROXY_LOG_LEVEL warn  
  
# Add the config  
ADD registry-proxy.conf /etc/httpd/conf.d/registry-proxy.conf  
  
# Prep for default startup  
CMD ["apachectl", "-D", "FOREGROUND"]  

