FROM zabbix/zabbix-server-mysql  
COPY sendmail.sh /usr/lib/zabbix/alertscripts/  
RUN touch /tmp/mailtmp.txt \  
&& echo "http://nl.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories
\  
&& echo "http://nl.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
&& echo "http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& apk update \  
&& apk add heirloom-mailx dos2unix\  
&& sed -i '4iecho "set from=${MAIL_SENDER}" > /etc/nail.rc'
/run_zabbix_component.sh \  
&& sed -i '5iecho "set smtp=${MAIL_MTA}" >> /etc/nail.rc'
/run_zabbix_component.sh \  
&& sed -i '6iecho "set smtp-auth-user=${MAIL_SENDER}" >> /etc/nail.rc'
/run_zabbix_component.sh \  
&& sed -i '7iecho "set smtp-auth-password=${MAIL_PASSWD}" >> /etc/nail.rc'
/run_zabbix_component.sh \  
&& sed -i '8iecho "set smtp-auth=login" >> /etc/nail.rc'
/run_zabbix_component.sh \  
&& sed -i '9ichmod +x /usr/lib/zabbix/alertscripts/sendmail.sh'
/run_zabbix_component.sh \  
&& rm -rf /var/cache/apk/*

