FROM vguardiola/gentoo  
MAINTAINER Victor Guardiola <victor@masquesoft.net>  
COPY ./etc/portage/package.keywords/opensmtp
/etc/portage/package.keywords/opensmtp  
COPY ./etc/portage/package.use/opensmtp /etc/portage/package.use/opensmtp  
COPY ./etc/locale.nopurge /etc/locale.nopurge  
RUN emerge --unmerge dev-libs/openssl && emerge -ND dev-libs/openssl && emerge
-ND mail-mta/opensmtpd mail-filter/opensmtpd-extras mail-filter/opendkim &&
eclean-dist -dqf && localepurge && rm /usr/portage/distfiles -rf  
RUN chown root:mail /var/spool/mail/ && chmod 03775 /var/spool/mail/  
COPY ./etc/setup.sh /usr/local/bin/setup.sh  
RUN chmod 755 /usr/local/bin/setup.sh  
COPY ./etc/opensmtpd/smtpd.conf /etc/opensmtpd/smtpd.conf  
EXPOSE 25  
CMD [ "/usr/local/bin/setup.sh"]  

