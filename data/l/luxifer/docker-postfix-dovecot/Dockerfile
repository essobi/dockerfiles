FROM debian:wheezy  
  
RUN useradd -G sudo -p $(perl -e'print crypt("vagrant", "vagrant")') -m -s
/bin/bash -N vagrant  
  
RUN apt-get update  
  
RUN echo "postfix postfix/mailname string packer-virtualbox-iso" | debconf-
set-selections  
RUN echo "postfix postfix/main_mailer_type select Local only" | debconf-set-
selections  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install postfix dovecot-imapd
supervisor  
  
RUN postconf -e "home_mailbox = Maildir/"  
RUN postconf -e "mailbox_command ="  
RUN postconf -e "inet_interfaces = all"  
  
RUN sed -i 's@mail_location = mbox:~/mail:INBOX=/var/mail/%u@mail_location =
maildir:~/Maildir@' /etc/dovecot/conf.d/10-mail.conf  
RUN sed -i 's@#disable_plaintext_auth = yes@disable_plaintext_auth = no@'
/etc/dovecot/conf.d/10-auth.conf  
RUN maildirmake.dovecot /etc/skel/Maildir  
RUN maildirmake.dovecot /etc/skel/Maildir/.Archive  
  
RUN cp -r /etc/skel/Maildir /home/vagrant  
RUN chown -R vagrant /home/vagrant/Maildir  
RUN chmod 700 /home/vagrant/Maildir  
  
VOLUME ["/home/vagrant/Maildir"]  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 25 143 993  
CMD ["/usr/bin/supervisord"]  

