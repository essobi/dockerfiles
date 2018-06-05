FROM ubuntu:14.04  
MAINTAINER Thomas Berger <th.berger@it.piratenpartei.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -qq  
RUN apt-get install -y apache2 rcs diffutils zip cron make gcc g++ pkg-config
libssl-dev  
  
ADD
http://sourceforge.net/projects/twiki/files/TWiki%20for%20all%20Platforms/TWiki-6.0.0/TWiki-6.0.0.tgz/download
/TWiki-6.0.0.tgz  
RUN tar xzf TWiki-6.0.0.tgz -C /var/www  
RUN rm TWiki-6.0.0.tgz  
  
ADD perl/cpanfile /tmp/cpanfile  
ADD http://cpansearch.perl.org/src/THALJEF/Pinto-0.09995/etc/cpanm /tmp/cpanm  
  
RUN chmod +x /tmp/cpanm  
RUN /tmp/cpanm -l /var/www/twiki/lib/CPAN --installdeps /tmp/  
RUN rm -rf /.cpanm /tmp/cpanm /tmp/cpanfile /var/www/twiki/lib/CPAN/man  
  
ADD configs/vhost.conf /etc/apache2/sites-available/twiki.conf  
ADD configs/LocalLib.cfg /var/www/twiki/bin/LocalLib.cfg  
ADD configs/LocalSite.cfg /var/www/twiki/lib/LocalSite.cfg  
ADD configs/setlib.cfg /var/www/twiki/bin/setlib.cfg  
ADD bin/prepare-env.sh /prepare-env.sh  
ADD bin/run.sh /run.sh  
RUN a2enmod cgi expires  
RUN a2dissite '*'  
RUN a2ensite twiki.conf  
RUN chown -cR www-data: /var/www/twiki  
RUN chmod +x /prepare-env.sh  
  
VOLUME ["/data"]  
ENTRYPOINT "/run.sh"  
  
EXPOSE 80

