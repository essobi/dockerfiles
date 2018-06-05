# Courier IMAP4/POP3/Authdaemon-MySQL  
FROM sameersbn/ubuntu:14.04.20150825  
MAINTAINER Baber <baber@mosga.net>  
RUN mkdir -p /var/run/courier/authdaemon/ && touch
/var/run/courier/authdaemon/pid.lock  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y
courier-imap courier-pop courier-authlib-mysql courier-mta fam  
EXPOSE 110/tcp 143/tcp  
ADD entrypoint.sh /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  

