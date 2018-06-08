FROM alpine:latest  
  
RUN \  
apk add --no-cache \  
spamassassin \  
wget \  
&& sa-update  
  
ENTRYPOINT ["spamd"]  
  
EXPOSE 783  
CMD ["--siteconfigpath=/etc/mail/spamassassin", "--max-children", "5", "--
create-prefs" , "--user-config", "--syslog", "/var/log/spamd.log", "--
listen=", "0.0.0.0:783", "-u", "mail"]

