FROM guyton/centos6  
RUN yum install -y postfix perl cyrus-sasl-plain rsyslog  
COPY master.cf /etc/postfix/  
COPY run_postfix /  
RUN chmod 700 /run_postfix ; postconf -e 'smtp_tls_CAfile = /etc/ssl/certs/ca-
bundle.crt'  
CMD /run_postfix  
EXPOSE 25  

