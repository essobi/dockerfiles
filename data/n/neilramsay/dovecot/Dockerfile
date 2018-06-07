FROM alpine  
  
RUN set -ex && \  
apk --no-cache add bash openssl ca-certificates dovecot && \  
mkdir /docker-entry.d && \  
sed -i 's!^#log_path = syslog!log_path = /dev/stderr!; \  
s!^#info_log_path =!info_log_path = /dev/stdout!'
/etc/dovecot/conf.d/10-logging.conf  
  
COPY docker-entrypoint.sh docker-utils.sh /usr/local/bin/  
COPY conf/local.conf /docker-entry.d/  
  
# Mail directory needs to be persistent  
# Note you cannot chmod this properly as its sticky bits are cleared  
VOLUME /var/mail  
  
# Expose IMAP ports  
EXPOSE 143/tcp 993/tcp  
  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
CMD ["dovecot","-F"]  

