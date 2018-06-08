FROM alpine  
USER root  
  
ARG BUILD_DATE  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="postfix-gmail-relay" \  
org.label-schema.description="Use postfix to relay emails from LAN through
gmail. Great to use in conjunction with other docker images or in a
lab/testing environment." \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/shibz/docker-postfix-gmail-relay"
\  
org.label-schema.docker.cmd="docker run -d -h relay.example.com
--name=mailrelay -e EMAIL=myLogin@gmail.com -e EMAILPASS=myPassword -p 25:25
shibz/postfix-gmail-relay" \  
org.label-schema.docker.cmd.devel="docker run -it -h relay.example.com
--name=mailrelay -e EMAIL=myLogin@gmail.com -e EMAILPASS=myPassword -p 25:25
shibz/postfix-gmail-relay" \  
org.label-schema.docker.cmd.debug="docker exec -it \$CONTAINER /bin/sh" \  
org.label-schema.docker.params="EMAIL=Google-hosted email address to log
into,EMAILPASS=Password for email account. Alternatively specify by binding
/config/credentials file,SYSTEM_TIMEZONE=Alternative timezone if UTC is not
desired,MYNETWORKS=Specify list of space-separated subnets to relay messages
for. The default should be fine for most people." \  
org.label-schema.schema-version="1.0"  
RUN apk add \--no-cache postfix rsyslog supervisor tzdata && \  
# main.cf  
postconf -e smtpd_banner="\$myhostname ESMTP" && \  
postconf -e relayhost=[smtp.gmail.com]:587 && \  
postconf -e smtp_sasl_auth_enable=yes && \  
postconf -e smtp_sasl_password_maps=hash:/etc/postfix/sasl_passwd && \  
postconf -e smtp_sasl_security_options=noanonymous && \  
postconf -e smtp_use_tls=yes && \  
postconf -e mynetworks="10.0.0.0/8 172.16.0.0/12 192.168.0.0/16" && \  
mkdir -p /var/log/supervisor  
  
COPY supervisord.conf /etc/supervisor/  
COPY init.sh /opt/init.sh  
  
EXPOSE 25  
  
CMD ["/opt/init.sh"]  

