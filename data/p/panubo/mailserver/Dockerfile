FROM centos:centos6  
  
RUN yum -y install epel-release && yum -y update && \  
yum -y install supervisor amavisd-new busybox clamd dovecot dovecot-mysql
postfix sqlgrey perl-DBD-MySQL spamassassin && \  
# Add voltgrid.py and requirements  
curl -q https://raw.githubusercontent.com/voltgrid/voltgrid-
pie/master/voltgrid.py -o /usr/local/bin/voltgrid.py && \  
chmod +x /usr/local/bin/voltgrid.py && yum -y install python-jinja2 && \  
# Add mail virtual user  
useradd vmail -d /var/vmail --uid 5000 \--shell /bin/false && rm -f
/var/vmail/.bash* && \  
# Cache spool dir as template  
cp -a /var/spool/postfix /var/spool/postfix.cache && \  
# Upgrade supervisor from PyPi (no deps because of
https://github.com/puphpet/puphpet/issues/1492)  
yum -y install python-pip && \  
pip install --no-deps --upgrade supervisor && \  
# Cleanup  
rm -rf /var/cache/yum/* && \  
# Disable logrotate  
rm -f /etc/cron.daily/logrotate && \  
# Ensure freshclam has run  
rm -f /var/lib/clamav/* && \  
freshclam  
  
EXPOSE 25 465 587 993 995  
VOLUME ["/var/vmail", "/var/spool/mail"]  
  
# Base Config  
COPY voltgrid.conf /usr/local/etc/voltgrid.conf  
COPY supervisord.conf /etc/supervisord.conf  
COPY *.sh /  
  
# Complex Config  
COPY amavisd/ /etc/amavisd/  
COPY sqlgrey/ /etc/sqlgrey/  
COPY dovecot/ /etc/dovecot/  
COPY postfix/ /etc/postfix/  
COPY spamassassin/ /etc/mail/spamassassin/  
  
ENTRYPOINT ["/entry.sh", "/usr/local/bin/voltgrid.py"]  
  
CMD ["supervisord", "-n", "-c", "/etc/supervisord.conf"]  
  

