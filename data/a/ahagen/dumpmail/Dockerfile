FROM python:alpine  
  
COPY wrapper.sh /assets/wrapper  
ENTRYPOINT ["/bin/ash", "/assets/wrapper"]  
  
RUN apk add --no-cache rsyslog postfix postfix-pcre && \  
printf '\n# Turn off missing UTF-8 support\nsmtputf8_enable = no' >>
/etc/postfix/main.cf && \  
chown root /var/spool/postfix /var/spool/postfix/pid && \  
touch /etc/postfix/aliases && newaliases && \  
mkdir /var/mail && \  
chmod +x /assets/wrapper  
  
EXPOSE 25  
COPY manage.py requirements.txt /srv/dumpmail/  
COPY dumpmail /srv/dumpmail/dumpmail  
COPY mail /srv/dumpmail/mail  
  
RUN adduser -D someone && \  
touch '/var/mail/someone' && \  
chown someone:someone '/var/mail/someone' && \  
chmod 0600 '/var/mail/someone' && \  
printf '/.*/ someone' >> /etc/postfix/virtual && \  
printf '\n# Virtual aliases\nvirtual_alias_maps = pcre:/etc/postfix/virtual'
>> /etc/postfix/main.cf && \  
pip install -r /srv/dumpmail/requirements.txt  
  
CMD ["python", "/srv/dumpmail/manage.py", "runserver", "0.0.0.0:80"]  
  
EXPOSE 80  

