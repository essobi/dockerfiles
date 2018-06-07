FROM debian:stretch-slim  
MAINTAINER sysadmin@kronostechnologies.com  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
dovecot-core \  
dovecot-imapd \  
dovecot-mysql \  
dovecot-pop3d \  
procps \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/doc/*  
  
# Install confd  
COPY bin/ /usr/local/bin/  
RUN chmod +x /usr/local/bin/* && \  
mkdir -p /etc/confd/conf.d && \  
mkdir -p /etc/confd/templates  
COPY confd/ /etc/confd/  
  
# Assign dovecot uid  
ARG DOVECOT_USER_UID=204  
ARG DOVECOT_USER_GID=204  
RUN groupmod -g $DOVECOT_USER_GID dovecot && \  
usermod -u $DOVECOT_USER_UID dovecot  
  
# Install start/stop scripts  
COPY ./configuration /k  
  
# Install entrypoint  
ADD https://github.com/kronostechnologies/docker-init-
entrypoint/releases/download/1.2.0/entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/entrypoint.sh  
  
EXPOSE 110  
EXPOSE 998  
EXPOSE 143  
EXPOSE 993  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
  

