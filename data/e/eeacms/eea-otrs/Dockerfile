#OTRS ticketing system docker image.  
#FROM centos:6.6  
FROM centos:6.8  
MAINTAINER michimau <mauro.michielon@eea.europa.eu>  
  
ENV OTRS_VERSION 4.0.29  
ENV SUB_OTRS_VERSION -01  
ENV OTRS_ROOT /opt/otrs/  
  
ADD addon/Znuny4OTRS-Repo-2.0.25.opm Znuny4OTRS-Repo-2.0.25.opm  
ADD addon/Znuny4OTRS-MarkTicketSeenUnseen-1.1.0.opm Znuny4OTRS-
MarkTicketSeenUnseen-1.1.0.opm  
ADD addon/Znuny4OTRS-SortByLastContact-3.2.1.opm Znuny4OTRS-
SortByLastContact-3.2.1.opm  
ADD addon/FAQ-4.0.91.opm FAQ-4.0.91.opm  
  
RUN yum install -y epel-release && \  
yum update -y && \  
yum -y install cronie httpd httpd-devel mysql mod_perl mod_ssl mod_rewrite \  
perl-core "perl(Crypt::SSLeay)" "perl(Net::LDAP)" "perl(URI)" \  
procmail "perl(Date::Format)" "perl(LWP::UserAgent)" \  
"perl(Net::DNS)" "perl(IO::Socket::SSL)" "perl(XML::Parser)" \  
"perl(Apache2::Reload)" "perl(Crypt::Eksblowfish::Bcrypt)" \  
"perl(Encode::HanExtra)" "perl(GD)" "perl(GD::Text)" "perl(GD::Graph)" \  
"perl(JSON::XS)" "perl(Mail::IMAPClient)" "perl(PDF::API2)" \  
"perl(Text::CSV_XS)" "perl(YAML::XS)" "perl(Text::CSV_XS)" "perl(DBD::mysql)"
\  
supervisor tar which wget git sendmail sendmail-cf openssl-perl perl-IO-
Socket-SSL  
  
RUN yum install -y
http://ftp.otrs.org/pub/otrs/RPMS/rhel/6/otrs-${OTRS_VERSION}${SUB_OTRS_VERSION}.noarch.rpm  
  
#Add configuration file  
ADD config/Config.pm ${OTRS_ROOT}Kernel/Config.pm  
ADD config/ZZZAuto.pm ${OTRS_ROOT}Kernel/Config/Files/ZZZAuto.pm  
ADD config/GenericAgent.pm ${OTRS_ROOT}Kernel/Config/GenericAgent.pm  
ADD config/OutOfOffice.xml ${OTRS_ROOT}Kernel/Config/Files/OutOfOffice.xml  
ADD config/FollowUp.pm ${OTRS_ROOT}Kernel/System/PostMaster/FollowUp.pm  
ADD config/Core.Agent.js ${OTRS_ROOT}var/httpd/htdocs/js/Core.Agent.js  
  
RUN cd /etc/mail && \  
rm virtusertable.db && \  
make && \  
cd \-  
  
#COPY config/local-host-names /etc/mail/local-host-names  
ADD config/sendmail.mc /etc/mail/sendmail.mc  
#COPY config/virtusertable /etc/mail/virtusertable  
##httpd configuration file SSL  
ADD config/zzz_otrs.conf /etc/httpd/conf.d/zzz_otrs.conf  
ADD config/ssl.conf /etc/httpd/conf.d/ssl.conf  
ADD config/mod_headers.conf /etc/httpd/conf.d/mod_headers.conf  
  
#Add change email fetch time script  
#COPY otrs_postmaster_time.sh ${OTRS_ROOT}scripts/  
RUN chmod 755 ${OTRS_ROOT}scripts/*.sh  
  
#Enable mod_filter  
RUN sed -i '/filter_module/s/#//g' /etc/httpd/conf/httpd.conf  
  
#reconfigure httpd  
RUN sed -i "s/error\/noindex.html/otrs\/index.pl/"
/etc/httpd/conf.d/welcome.conf  
  
#Fix pam permissions for crond  
RUN echo "+ : otrs : cron crond" |cat >> /etc/security/access.conf  
RUN sed -i -e '/pam_loginuid.so/ s/^#*/#/' /etc/pam.d/crond  
  
#Configure supervisord  
RUN sed -i -e "s/^nodaemon=false/nodaemon=true/" /etc/supervisord.conf  
ADD etc/supervisord.d/otrs.ini /etc/supervisord.d/  
RUN cat /etc/supervisord.d/otrs.ini >> etc/supervisord.conf  
  
#Fix PostmasterFollowUpState config var, this line on Ticket.xml disallow the
edition  
#of that field through SysConfig  
RUN sed -i -e
'/<ValidateModule>Kernel::System::SysConfig::StateValidate<\/ValidateModule>/
s/^#*/#/' -i ${OTRS_ROOT}Kernel/Config/Files/Ticket.xml  
  
RUN mkdir -p ${OTRS_ROOT}var/{run,tmp}/  
  
#Add run script  
ADD run.sh /  
RUN chmod 755 /*.sh  
  
RUN usermod -G apache otrs  
  
EXPOSE 80 443 25  
CMD ["/run.sh"]  

