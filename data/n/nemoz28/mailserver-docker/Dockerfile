FROM debian:jessie  
MAINTAINER Jerome Zamaroczy  
  
ARG DOMAINE="zamaroczy.fr"  
ARG USER="jerome"  
ARG PASSWORD="password"  
ENV TERM=xterm \  
DIRPATH="/etc/init.d" \  
PF_VERSION="2.11.3-1" \  
DOMAINE=${DOMAINE} \  
USER=${USER} \  
PASSWORD=${PASSWORD} \  
CWD_PSTF="/etc/postfix" \  
CWD_COR="/etc/courier" \  
HOME="/home/${USER}" \  
MAILDIR="Maildir/" \  
DH_BITS="2048" \  
DAYS="3650"  
LABEL vendor=ACME\ Incorporated \  
$DOMAINE.roundcube-beta="mailserver-docker" \  
$DOMAINE.roundcube-production="prod" \  
$DOMAINE.version="postfix-$PF_VERSION" \  
$DOMAINE.release-date="2017-04-03"  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
RUN (apt-get update && \  
apt-get install -f -qq -y spamassassin procmail sasl2-bin clamav clamav-
freshclam curl vim net-tools htop rsyslog \  
courier-authdaemon courier-authlib courier-authlib-userdb courier-imap
courier-imap-ssl courier-ssl apt-utils postfix courier-base gamin && \  
apt-get clean)  
  
COPY etc/courier/authdaemonrc $CWD_COR/authdaemonrc  
COPY etc/courier/imapd.cnf $CWD_COR/imapd.cnf  
COPY etc/courier/imapd $CWD_COR/imapd  
COPY etc/courier/imapd-ssl $CWD_COR/imapd-ssl  
  
COPY etc/postfix/dynamicmaps.cf $CWD_PSTF/dynamicmaps.cf  
COPY etc/postfix/main.cf $CWD_PSTF/main.cf  
COPY etc/postfix/master.cf $CWD_PSTF/master.cf  
COPY etc/postfix/postfix-files $CWD_PSTF/postfix-files  
COPY etc/postfix/sasl/smtpd.conf $CWD_PSTF/sasl/smtpd.conf  
COPY etc/postfix/extfile.cnf $CWD_PSTF/extfile.cnf  
  
COPY etc/init.d/gen-cert-smtps-sasl.sh $DIRPATH/gen-cert-smtps-sasl.sh  
  
COPY etc/procmailrc /etc/procmailrc  
COPY etc/sasldb2 /var/spool/postfix/etc/sasldb2  
COPY etc/mailname /etc/mailname  
  
COPY etc/default/spamassassin /etc/default/spamassassin  
COPY etc/default/saslauthd /etc/default/saslauthd  
  
COPY etc/init.d/start.sh $DIRPATH/start.sh  
  
#SYSTEM CONFIGURATION PARAMETERS  
RUN chmod +x $DIRPATH/gen-cert-smtps-sasl.sh  
RUN chown postfix:sasl /var/spool/postfix/etc/sasldb2  
RUN chmod 640 /var/spool/postfix/etc/sasldb2  
RUN rm -rf /etc/sasldb2  
RUN ln -s /var/spool/postfix/etc/sasldb2 /etc/sasldb2  
RUN chmod +x $DIRPATH/start.sh $DIRPATH/gen-cert-smtps-sasl.sh  
RUN ln -sf /dev/stdout /var/log/syslog.log  
  
#Mount Home directory user  
#VOLUME ["$HOME"]  
EXPOSE 587 465 25 993 143  
#START ENVIRONNEMENT MAIL-SERVER MAYBE USE DATA USER ELSE CREATE NEW MAILDIR  
CMD ["/bin/bash", `$DIRPATH/start.sh`, "-d"]  
  

