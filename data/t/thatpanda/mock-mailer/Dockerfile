FROM debian:jessie  
  
RUN echo 'postfix postfix/main_mailer_type string Internet site' >
/preseed.txt && \  
echo 'postfix postfix/mailname string mail.example.com' >> /preseed.txt && \  
apt-get update && \  
debconf-set-selections /preseed.txt && \  
apt-get install -y postfix postfix-pcre && \  
rm /preseed.txt  
RUN postconf -e myhostname=mail.example.com && \  
postconf -e mydestination='mail.example.com, example.com,
localhost.localdomain, localhost' && \  
postconf -e virtual_alias_maps='pcre:/etc/postfix/virtual'  
ADD root/ /  
  
CMD ["/run.sh"]  

