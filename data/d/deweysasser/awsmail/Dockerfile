FROM debian:jessie  
MAINTAINER Dewey Sasser <dewey@sasser.com>  
  
######################################################################  
# Base Packages  
RUN apt-get update  
RUN apt-get -y install postfix ca-certificates mailutils telnet psmisc rsyslog  
  
# Install the dumb-init process to make a reasonable PID1  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.0.0/dumb-
init_1.0.0_amd64 /usr/local/bin/dumb-init  
  
# Be paranoid about making sure this binary is the 'official' release.  
RUN echo 52f9f8ae014cc00021d5563738a83551e101a16ff6fb6e94ab71fbe8c7403631
/usr/local/bin/dumb-init \  
| sha256sum -c - && chmod +x /usr/local/bin/dumb-init  
  
######################################################################  
# Configuration Section  
# Allow mail from all private addresses by default for easy setup  
# while still being reasonably secure  
ENV NETWORKS 127.0.0.0/8 10.0.0.0/8 172.16.0.0/12 192.168.0.0/16  
# AWS credentials  
ENV ID="put your aws ID here" KEY="put your aws secret here"  
# This is a from address used when there is no valid one  
ENV FROM "root@example.com"  
# We'll default to the us-east mail endpoint. Feel free to substitute your own  
ENV SES_ENDPOINT=email-smtp.us-east-1.amazonaws.com SMTP_PORT=587  
# End configuration  
######################################################################  
# Set our system into the proper timezone, for convenience  
RUN ln -sf /usr/share/zoneinfo/posixrules /etc/localtime  
  
# For testing our mail configuration, try "date | mail -s testing  
# user@example.com"  
# Most of the postscript configuration. The parts that are dependent  
# on environment variables are actually in the 'run' script  
RUN postconf -e 'smtp_sasl_auth_enable = yes' ;\  
postconf -e 'smtp_sasl_password_maps = hash:/etc/postfix/sasl-passwords' ;\  
postconf -e 'smtp_sasl_security_options = noanonymous' ;\  
postconf -e 'smtp_use_tls = yes' ;\  
postconf -e 'smtp_tls_security_level = encrypt' ;\  
postconf -e 'smtp_tls_note_starttls_offer = yes' ;\  
postconf -e 'smtp_tls_CAfile = /etc/ssl/certs/ca-certificates.crt'  
  
EXPOSE 25  
VOLUME /var/spool/postfix  
  
COPY run /root/run  
RUN chmod +x /root/run  
CMD /usr/local/bin/dumb-init /root/run  

