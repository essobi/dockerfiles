FROM centos:centos6  
  
MAINTAINER Paolo Antinori <pantinor@redhat.com>  
  
# install EPEL repo  
RUN yum -y install http://download.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm  
  
# install tar  
RUN yum -y install tar  
  
# install nagios and a partial list of plugins to limit the number of
dependencies  
RUN yum -y install nagios nagios-common nagios-plugins nagios-plugins-by_ssh
nagios-plugins-disk nagios-plugins-http nagios-plugins-load nagios-plugins-
nagios nagios-plugins-perl nagios-plugins-ping nagios-plugins-procs nagios-
plugins-ssh nagios-plugins-swap nagios-plugins-users  
  
# install perl modules required by jmx4perl component  
RUN yum -y install perl-Class-Accessor perl-common-sense perl-Config-Tiny
perl-Crypt-Blowfish_PP perl-ExtUtils-CBuilder perl-ExtUtils-ParseXS perl-File-
BaseDir perl-JSON perl-JSON-Any perl-JSON-XS perl-Math-Calc-Units perl-Module-
Build perl-Module-Find perl-Nagios-Plugin perl-Term-ShellUI perl-Config-
General perl-Test-Simple perl-Time-HiRes perl-Sys-SigAction perl-Term-Size
perl-Term-Size-Any perl-Term-ReadLine-Gnu  
  
# install additional perl modules not present in Centos and EPEL main repos  
RUN yum -y install
ftp://ftp.pbone.net/mirror/ftp5.gwdg.de/pub/opensuse/repositories/devel:/languages:/perl/CentOS_5/noarch/perl-
Env-Path-0.18-1.2.noarch.rpm http://repo.openfusion.net/centos6-i386/perl-
File-SearchPath-0.06-1.of.el6.noarch.rpm http://pkgs.repoforge.org/perl-Term-
Clui/perl-Term-Clui-1.64-1.el6.rf.noarch.rpm  
  
# download jmx4perl  
ADD http://search.cpan.org/CPAN/authors/id/R/RO/ROLAND/jmx4perl-1.07.tar.gz
/root/  
  
# extract jmx4perl  
RUN tar -xvf /root/jmx4perl* -C /root  
  
# change default values for the list of features to install  
RUN awk '/\$msg,"y"/{c+=1;done=0}{if(done==0 && (c>2 && c != 4)
){sub("\"y\"","\"n\"",$0);done=1};print}' /root/jmx4perl-1.07/Build.PL >
/root/jmx4perl-1.07/BuildAnswered.PL  
  
# install jmx4perl and j4psh  
RUN cd /root/jmx4perl-1.07 ; PERL_MM_USE_DEFAULT=1 perl
/root/jmx4perl-1.07/BuildAnswered.PL  
RUN cd /root/jmx4perl-1.07 ; /root/jmx4perl-1.07/Build test  
RUN cd /root/jmx4perl-1.07 ; /root/jmx4perl-1.07/Build install  
  
#RUN rm /root/jmx4perl-1.07* -rf  
# fix perl bizarre bug
http://osdir.com/ml/network.nagios.devel/2007-07/msg00031.html  
RUN sed -i s/+epn/-epn/g /usr/local/bin/check_jmx4perl  
  
# enable nagios user  
RUN htpasswd -bc /etc/nagios/passwd nagiosadmin nagiosadmin  
  
# set nagios UI filesystem permissions  
RUN chmod -R a+rwx /var/log/nagios /var/spool/nagios/cmd/  
  
# install nagios debug plugin  
ADD http://www.waggy.at/nagios/capture_plugin.txt
/etc/nagios/scripts/capture_plugin.pl  
  
# add sample configuration and plugins  
ADD ./script /bin/  
ADD ./nagios_conf /etc/nagios/conf.d/  
ADD ./nagios_plugin /etc/nagios/scripts/  
  
# set execution permission to helper scripts  
RUN chmod +rx /etc/nagios/scripts/capture_plugin.pl  
RUN chmod +rx /etc/nagios/scripts/check_bundle_by_name.py  
RUN chmod +rx /bin/startNagios.sh  
  
# expose service port  
EXPOSE 80  
# start httpd, nagios and bash  
CMD ["/bin/startNagios.sh"]  
  

