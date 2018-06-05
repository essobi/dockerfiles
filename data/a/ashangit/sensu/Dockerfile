#  
# Sensu  
#  
# Pull base image.  
FROM ashangit/base:latest  
MAINTAINER Nicolas Fraison <nfraison@yahoo.fr>  
  
ENV SENSU_VERSION 0.21.0  
# Mount sensu repo.  
ADD repo/sensu.repo /etc/yum.repos.d/sensu.repo  
  
# Deploy sensu  
RUN yum install sensu-${SENSU_VERSION} gcc-c++ make -y && \  
mv /etc/sensu/config.json.example /etc/sensu/config.json && \  
chown -R sensu:sensu /etc/sensu  
  
# Install mail handler gem  
RUN /opt/sensu/embedded/bin/gem install sensu-plugins-mailer  
  
# Mount sensu config.  
ADD conf/config.json /etc/sensu/config.json  
  
# Expose ports.  
EXPOSE 4567  
COPY docker-entrypoint.sh /entrypoint.sh  
RUN chmod 750 /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
# Default command  
CMD [ "/opt/sensu/bin/sensu-server", "-c", "/etc/sensu/config.json", "-d",
"/etc/sensu/conf.d", "-e", "/etc/sensu/extensions", "-L", "info" ]  

