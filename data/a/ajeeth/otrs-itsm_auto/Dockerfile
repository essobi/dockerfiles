FROM centos:centos6  
MAINTAINER Ajeeth Samuel <ajeeth.samuel@gmail.com>  
  
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN yum update -y  
RUN yum -y install openssh-server wget mysql-server mysql apache httpd-devel
perl-core "perl(Crypt::SSLeay)" "perl(Net::LDAP)" "perl(URI)" mod_perl httpd
procmail "perl(Date::Format)" "perl(LWP::UserAgent)" "perl(Net::DNS)"
"perl(IO::Socket::SSL)" "perl(XML::Parser)" "perl(Apache2::Reload)"
"perl(Crypt::Eksblowfish::Bcrypt)" "perl(Encode::HanExtra)" "perl(GD)"
"perl(GD::Text)" "perl(GD::Graph)" "perl(JSON::XS)" "perl(Mail::IMAPClient)"
"perl(PDF::API2)" "perl(Text::CSV_XS)" "perl(YAML::XS)" curl  
  
#MYSQL  
RUN sed -i '/user=mysql/akey_buffer_size=32M' /etc/my.cnf  
RUN sed -i '/user=mysql/amax_allowed_packet=32M' /etc/my.cnf  
  
#OTRS  
RUN wget http://ftp.otrs.org/pub/otrs/RPMS/rhel/6/otrs-5.0.16-01.noarch.rpm  
RUN yum -y install otrs-5.0.16-01.noarch.rpm --skip-broken  
  
#OTRS COPY Configs  
ADD Config.pm /opt/otrs/Kernel/Config.pm  
RUN sed -i -e "s/mod_perl.c/mod_perl.so/" /etc/httpd/conf.d/zzz_otrs.conf  
  
#Get ITSM module  
RUN wget http://ftp.otrs.org/pub/otrs/itsm/bundle5/ITSM-5.0.16.opm  
  
#reconfigure httpd  
RUN sed -i "s/error\/noindex.html/otrs\/index.pl/"
/etc/httpd/conf.d/welcome.conf  
  
#Start web and otrs and configure mysql  
ADD firstrun.sh /firstrun.sh  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
RUN touch /firstrun  
  
#set up sshd  
RUN ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key && ssh-keygen -q
-N "" -t rsa -f /etc/ssh/ssh_host_rsa_key && sed -i
"s/#UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config
&& sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config  
RUN echo "root:root" | chpasswd  
  
#enable crons  
WORKDIR /opt/otrs/var/cron/  
USER otrs  
CMD ["/bin/bash -c 'for foo in *.dist; do cp $foo `basename $foo .dist`;
done'"]  
  
USER root  
EXPOSE 22 80  
CMD ["/bin/bash", "/run.sh"]  

