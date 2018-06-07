FROM craeckie/service-base  
  
MAINTAINER Josia <josia-login@rosskopfs.de>  
  
RUN apt-get install -y dovecot-imapd ca-certificates  
RUN apt-get install -y curl tar python  
  
WORKDIR /root  
  
# Build&Install getmail  
RUN curl http://pyropus.ca/software/getmail/old-versions/getmail-4.48.0.tar |
tar xvz  
RUN cd getmail-4.48.0/; python setup.py install  
RUN rm -r getmail-4.48.0/  
  
# Build&Install offlineimap  
RUN git clone https://github.com/OfflineIMAP/offlineimap.git  
RUN cd offlineimap; make clean; make && python setup.py install  
RUN rm -r offlineimap  
  
# Environment  
# Mail  
ENV MAIL_DOMAIN 'mail.weiltoast.de'  
ENV MAIL_USER vmail  
ENV MAIL_HOME /home/$MAIL_USER  
# Paths  
ENV DC_CONF /etc/dovecot  
ENV LOG_DIR /var/log  
  
RUN useradd --user-group --base-dir /home --home-dir $MAIL_HOME \--create-home
$MAIL_USER  
  
# OfflineIMAP  
# Configuration file  
ADD offlineimap/offlineimaprc offlineimaprc  
# Init script  
ADD offlineimap/init-offlineimap.sh /etc/my_init.d/init-20-offlineimap.sh  
RUN chmod +x /etc/my_init.d/init-20-offlineimap.sh  
# Cron job  
ADD offlineimap/cron /etc/cron.d/offlineimap-cron  
RUN chmod 0744 /etc/cron.d/offlineimap-cron  
ADD offlineimap/run-offlineimap.sh run-offlineimap.sh  
RUN chmod +x run-offlineimap.sh  
  
# getmail  
# Configuration file  
ADD getmail/getmailrc getmailrc  
# Init script  
ADD getmail/init-getmail.sh /etc/my_init.d/init-30-getmail.sh  
RUN chmod +x /etc/my_init.d/init-30-getmail.sh  
# Run script  
RUN mkdir /etc/service/getmail  
ADD getmail/run-getmail.sh /etc/service/getmail/run  
RUN chmod +x /etc/service/getmail/run  
ADD getmail/run-getmail-first.sh run-getmail-first.sh  
RUN chmod +x run-getmail-first.sh  
  
# Dovecot  
# Configuration file  
ADD dovecot/dovecot.conf dovecot.conf  
# Init script  
ADD dovecot/init-dovecot.sh /etc/my_init.d/init-10-dovecot.sh  
RUN chmod +x /etc/my_init.d/init-10-dovecot.sh  
# Conversion from UTF-7-IMAP  
RUN cpan install Encode::IMAPUTF7  
ADD dovecot/convert.pl convert.pl  
# Run script  
RUN mkdir /etc/service/dovecot  
ADD dovecot/run-dovecot.sh /etc/service/dovecot/run  
RUN chmod +x /etc/service/dovecot/run  
  

