FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
WORKDIR /root  
  
RUN groupadd -g 5000 vmail && useradd -g vmail -u 5000 vmail -d /var/mail  
  
# Setup build environment  
RUN apt-get -y update && apt-get -y upgrade  
  
RUN apt-get install -y --no-install-recommends mysql-client  
  
# Core mail components  
RUN apt-get install -y --no-install-recommends\  
postfix postfix-mysql \  
dovecot-core dovecot-imapd dovecot-pop3d dovecot-lmtpd dovecot-mysql \  
postgrey amavis clamav clamav-daemon spamassassin  
  
# Addons for mail filtering  
RUN apt-get install -y --no-install-recommends\  
pyzor razor arj cabextract lzop nomarch p7zip-full ripole \  
rpm2cpio tnef unzip unrar-free zip zoo  
  
COPY config/etc /root/config/etc  
COPY entrypoint.sh /  
ADD https://raw.githubusercontent.com/dfrommi/docker-
utils/master/filter_template.sh /  
RUN chmod +x /*.sh  
  
VOLUME /data  
  
EXPOSE 25 465 587 110 995 143 993  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["startall"]  

