FROM combro2k/debian-debootstrap:8  
MAINTAINER Martijn van Maurik <docker@vmaurik.nl> / Zerph  
  
# Environment variables  
ENV HOME=/root \  
INSTALL_LOG=/var/log/build.log \  
AMAVISD_DB_HOME=/var/lib/amavis/db  
  
# Software versions  
ENV POSTFIX_VERSION=3.0.2 \  
DOVECOT_VERSION=2.2.18 \  
DOVECOT_PIGEONHOLE=0.4.8 \  
OPENDKIM_VERSION=2.10.3 \  
PYPOLICYD_SPF_MAIN=1.3 \  
PYPOLICYD_SPF_VERSION=1.3.1 \  
CLAMAV_VERSION=0.98.7 \  
AMAVISD_NEW_VERSION=2.10.1 \  
AMAVISD_MILTER=1.6.1 \  
GREYLIST_VERSION=4.5.14 \  
OPENDMARC_VERSION=1.3.1  
# Add resources  
ADD resources/bin/ /usr/local/bin/  
  
RUN chmod +x /usr/local/bin/* && touch ${INSTALL_LOG} && /bin/bash -l -c
'/usr/local/bin/setup.sh build'  
  
# Add remaining resources  
ADD resources/etc/ /etc/  
ADD resources/opt/ /opt/  
  
# Run the last bits and clean up  
RUN /bin/bash -l -c '/usr/local/bin/setup.sh post_install' | tee -a
${INSTALL_LOG} > /dev/null 2>&1  
  
EXPOSE 25 80 110 143 465 587 993 995 4190  
VOLUME ["/var/vmail", "/etc/dovecot", "/etc/postfix", "/etc/amavis" ,
"/etc/opendkim", "/etc/opendmarc", "/var/mailman", "/etc/mailman"]  
  
CMD ["/usr/local/bin/run"]  

