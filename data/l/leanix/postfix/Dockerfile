FROM leanix/ubuntu-ansible  
  
ADD postfix-start.sh /usr/local/bin/  
ADD ansible /ansible  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y postfix libsasl2-modules rsyslog  
  
ENV POSTFIX_RELAYHOST in-v3.mailjet.com  
ENV POSTFIX_RELAYHOST_PORT 587  
ENV POSTFIX_SMTP_SASL_AUTH_ENABLE yes  
ENV POSTFIX_SASL_DOMAIN leanix.net  
ENV POSTFIX_TESTING True  
ENV POSTFIX_TESTING_EMAIL development@leanix.net  
ENV POSTFIX_BCC_EMAIL outgoing@leanix.net  
  
ENV TERM=xterm  
  
EXPOSE 25  
CMD ["/usr/local/bin/postfix-start.sh"]

