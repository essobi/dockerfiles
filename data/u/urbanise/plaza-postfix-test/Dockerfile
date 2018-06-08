From ubuntu:trusty  
  
EXPOSE 25  
EXPOSE 143  
  
# Set noninteractive mode for apt-get  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get -y install supervisor postfix courier-imap
courier-authdaemon  
  
# Add files  
ADD install.sh /opt/install.sh  
  
RUN maildirmake "/etc/skel/Maildir" && \  
maildirmake "/etc/skel/Maildir/.Sent" && \  
maildirmake "/etc/skel/Maildir/.Trash" && \  
maildirmake "/etc/skel/Maildir/.Drafts" && \  
echo -e "INBOX\nINBOX.Sent\nINBOX.Trash\nInbox.Drafts" >>
"/etc/skel/Maildir/courierimapsubscribed" && \  
touch "/etc/skel/Maildir/.Sent/maildirfolder" && \  
useradd testuser -m  
  
RUN echo /^.*$/ testuser >> /etc/postfix/virtual-regexp && \  
echo virtual_alias_maps = regexp:/etc/postfix/virtual-regexp >>
/etc/postfix/main.cf && \  
postmap /etc/postfix/virtual-regexp && \  
sed -i 's/^mynetworks.*$/mynetworks = 192.168.0.0\/16 10.151.0.0\/16
127.0.0.0\/8/g' /etc/postfix/main.cf && \  
chmod a+x /opt/install.sh && \  
postconf -e "home_mailbox = Maildir/" && \  
postconf -e "mailbox_command = " && \  
sed -i -r 's/daemons=5/daemons=1/g' /etc/courier/authdaemonrc  
# sed -i -r 's/authmodulelist="authpam"/authmodulelist="authuserdb"/g'
/etc/courier/authdaemonrc  
  
  
# Run  
CMD /opt/install.sh;/usr/bin/supervisord -c /etc/supervisor/supervisord.conf  

