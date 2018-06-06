FROM ubuntu:latest  
# We base this on ubuntu  
# Postfix  
# Set env. replace right most column with values specific to your environment  
ARG POSTFIX_SETGID  
ENV POSTFIX_SETGID ${POSTFIX_SETGID:-postfix}  
ARG POSTFIX_SMTP_PORT  
ENV POSTFIX_SMTP_PORT ${POSTFIX_SMTP_PORT:-25}  
ARG POSTFIX_TLS_PORT  
ENV POSTFIX_TLS_PORT ${POSTFIX_TLS_PORT:-589}  
ARG POSTFIX_LISTEN  
ENV POSTFIX_LISTEN ${POSTFIX_LISTEN:-0.0.0.0}  
ARG POSTFIX_LISTEN6  
ENV POSTFIX_LISTEN6 ${POSTFIX_LISTEN6:-::}  
ARG POSTFIX_HOSTNAME  
ENV POSTFIX_HOSTNAME ${POSTFIX_HOSTNAME:-mail}  
ARG POSTFIX_DOMAIN  
ENV POSTFIX_DOMAIN ${POSTFIX_DOMAIN:-yourdomain.com}  
# FQDN for debconf  
ARG POSTFIX_FQDN  
ENV POSTFIX_FQDN ${POSTFIX_FQDN:-${POSTFIX_HOSTNAME}.${POSTFIX_DOMAIN}}  
# This is "mynetworks" in the postfix config  
ARG POSTFIX_LOCAL_ADDRESSES  
ENV POSTFIX_LOCAL_ADDRESSES ${POSTFIX_LOCAL_ADDRESSES:-10.0.0.0/24}  
# We relay to here  
ARG POSTFIX_RELAY_HOST  
ENV POSTFIX_RELAY_HOST ${POSTFIX_RELAY_HOST:-nangiala.localdomain}  
ARG POSTFIX_ADMINISTRATOR  
ENV POSTFIX_ADMINISTRATOR
${POSTFIX_ADMINISTRATOR:-postmaster@${POSTFIX_DOMAIN}}  
# Identify the server to any client/other server  
ARG POSTFIX_BANNERNAME  
ENV POSTFIX_BANNERNAME ${POSTFIX_BANNERNAME:-welcome to my server}  
# Postfix runs as this user  
ARG POSTFIX_USERNAME  
ENV POSTFIX_USERNAME ${POSTFIX_USERNAME:-postfix}  
# This version will be reported to clients/other servers  
ARG POSTFIX_VERSION  
ENV POSTFIX_VERSION ${POSTFIX_VERSION:-latest}  
# Where do we store mail?  
ARG POSTFIX_SPOOL_DIRECTORY  
ENV POSTFIX_SPOOL_DIRECTORY ${POSTFIX_SPOOL_DIRECTORY:-/var/spool/postfix/}  
  
# Who made this version  
LABEL maintainer=dansta  
  
# This ought to work but might not  
HEALTHCHECK \--interval=15s --timeout=3s CMD postfix status || exit 1  
  
# Install config replacement env  
RUN apt-get update && apt-get install -y python3  
  
# Prepare debconf since postfix normally is interactive install  
ADD replace.py /usr/local/bin/replace_conf  
ADD debconf.sh /usr/local/bin/debconf.sh  
ADD setup_start_postfix.sh /usr/local/bin/setup_start_postfix.sh  
ADD postfixalive.sh /usr/local/bin/postfixalive.sh  
ADD wrapper.sh /usr/local/bin/wrapper.sh  
RUN chmod u+x /usr/local/bin/replace_conf \  
/usr/local/bin/debconf.sh \  
/usr/local/bin/setup_start_postfix.sh \  
/usr/local/bin/postfixalive.sh \  
/usr/local/bin/wrapper.sh  
RUN /usr/local/bin/replace_conf /usr/local/bin/debconf.sh POSTFIX  
RUN /usr/local/bin/debconf.sh  
  
# Update and install packages  
RUN apt-get install -y \  
postfix \  
spamass-milter \  
postgrey  
  
# Add our own config file  
ADD files/etc/postfix/main.cf /etc/postfix/main.cf  
# Replace params  
RUN /usr/local/bin/replace_conf /etc/postfix/main.cf POSTFIX  
  
# Remove python3 again  
RUN apt-get remove -y python3 && apt-get -y autoremove  
  
# Document port usage for docker in case you are going to use it as a service  
EXPOSE "${POSTFIX_SMTP_PORT}/tcp" \  
"${POSTFIX_TLS_PORT}/tcp"  
VOLUME /var/spool/ \  
/var/log/postfix \  
/dynamic/ \  
/home/ \  
/certificates/  
  
STOPSIGNAL SIGTERM  
  
# Start postfix  
CMD /usr/local/bin/wrapper.sh  

