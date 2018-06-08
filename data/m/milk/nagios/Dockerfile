FROM phusion/baseimage:latest  
  
MAINTAINER Emilien Kenler <hello@emilienkenler.com>  
  
CMD ["/sbin/my_init"]  
  
RUN sed -i 's/universe/universe multiverse/' /etc/apt/sources.list && \  
apt-get update -y && \  
apt-get install -y build-essential libgd2-xpm-dev \  
libnet-snmp-perl snmp snmp-mibs-downloader \  
libwww-perl libcrypt-ssleay-perl \  
python python-pip \  
ssmtp mailutils \  
iputils-ping \  
openssl libssl-dev apache2 libapache2-mod-php unzip && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN groupadd nagios  
RUN groupadd nagioscmd  
RUN useradd -g nagios -G nagioscmd -d /opt/nagios nagios  
RUN usermod -G nagioscmd www-data  
  
RUN mkdir -p /opt/nagios /opt/nagios/etc /opt/nagios/var  
  
RUN cd /tmp && \  
curl -L -O
https://github.com/NagiosEnterprises/nagioscore/releases/download/release-4.2.3/nagios-4.2.3.tar.gz
&& \  
tar xvf nagios-4.2.3.tar.gz && \  
rm /tmp/nagios-4.2.3.tar.gz && \  
curl -L -O http://nagios-plugins.org/download/nagios-plugins-2.1.4.tar.gz && \  
tar xvf nagios-plugins-2.1.4.tar.gz && \  
rm /tmp/nagios-plugins-2.1.4.tar.gz && \  
curl -L -O
https://github.com/NagiosEnterprises/nrpe/releases/download/3.0.1/nrpe-3.0.1.tar.gz
&& \  
tar xvf nrpe-3.0.1.tar.gz && \  
rm /tmp/nrpe-3.0.1.tar.gz  
  
RUN a2enmod cgi  
RUN a2enmod rewrite  
  
RUN cd /tmp/nagios-4.2.3 && \  
./configure \  
\--prefix=/opt/nagios \  
\--sysconfdir=/opt/nagios/etc \  
\--localstatedir=/opt/nagios/var \  
\--libexecdir=/opt/nagios/plugins \  
\--with-nagios-group=nagios \  
\--with-command-group=nagioscmd \  
\--with-mail=/usr/sbin/sendmail && \  
make all && \  
make install && \  
make install-commandmode && \  
cp sample-config/httpd.conf /etc/apache2/conf-available/nagios.conf && \  
ln -s /etc/apache2/conf-available/nagios.conf /etc/apache2/conf-
enabled/nagios.conf  
  
RUN cd /tmp/nagios-plugins-2.1.4 && \  
./configure \  
\--prefix=/opt/nagios \  
\--sysconfdir=/opt/nagios/etc \  
\--localstatedir=/opt/nagios/var \  
\--libexecdir=/opt/nagios/plugins \  
\--with-nagios-user=nagios \  
\--with-nagios-group=nagios \  
\--with-openssl && \  
make && \  
make install  
  
RUN cd /tmp/nrpe-3.0.1 && \  
./configure \  
\--prefix=/opt/nagios \  
\--sysconfdir=/opt/nagios/etc \  
\--localstatedir=/opt/nagios/var \  
\--libexecdir=/opt/nagios/plugins \  
\--with-nagios-user=nagios \  
\--with-nagios-group=nagios \  
\--with-ssl=/usr/bin/openssl \  
\--with-ssl-lib=/usr/lib/x86_64-linux-gnu && \  
make check_nrpe && \  
make install-plugin  
  
RUN sed -i "s,DocumentRoot.*,DocumentRoot /opt/nagios/share,"
/etc/apache2/sites-enabled/000-default.conf && \  
sed -i "s,</VirtualHost>,<IfDefine ENABLE_USR_LIB_CGI_BIN>\nScriptAlias /cgi-
bin/ /opt/nagios/sbin/\n</IfDefine>\n</VirtualHost>," /etc/apache2/sites-
enabled/000-default.conf  
  
ADD pagerduty_nagios.pl /usr/local/bin/pagerduty_nagios.pl  
RUN chmod +x /usr/local/bin/pagerduty_nagios.pl  
RUN echo '* * * * * /usr/local/bin/pagerduty_nagios.pl flush' >> /etc/crontab  
  
RUN pip install hipsaint  
  
RUN mkdir -p /etc/service/apache /etc/service/nagios  
ADD apache.init /etc/service/apache/run  
ADD nagios.init /etc/service/nagios/run  
RUN chmod +x /etc/service/apache/run /etc/service/nagios/run  
  
EXPOSE 80  
WORKDIR /opt/nagios  

