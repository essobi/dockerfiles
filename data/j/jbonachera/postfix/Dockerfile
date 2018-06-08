FROM jbonachera/arch  
MAINTAINER Julien BONACHERA <julien@bonachera.fr>  
EXPOSE 25 465 587  
ENTRYPOINT /sbin/entrypoint.sh  
RUN pacman --noconfirm -S cyrus-sasl cyrus-sasl postfix net-tools  
VOLUME ["/var/spool/postfix", "/var/lib/postfix"]  
COPY smtp-sasl.conf /etc/sasl2/smtpd.conf  
COPY conf.d/* /etc/postfix/  
COPY fake_syslog.ini /etc/fake_syslog.ini  
COPY fake_syslog.py /usr/local/bin/fake_syslog.py  
RUN chmod o-rwx -R /etc/postfix/  
ADD entrypoint.sh /sbin/entrypoint.sh  

