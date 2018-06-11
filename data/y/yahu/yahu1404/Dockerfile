FROM ubuntu:14.04  
MAINTAINER ricardoamaro <ricardo.amaro@acquia.com>  
  
#COPY sources.list /etc/apt/sources.list  
ENV HOME /root  
#ADD . /build  
ENV DEBIAN_FRONTEND noninteractive  
# Keep upstart from complaining  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
# Install services  
RUN apt-get update  
RUN apt-get install -y --force-yes ssh cron wget curl  
  
# Install base packages  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -yq install \  
apache2 \  
libapache2-mod-php5 \  
php5-mysql \  
php5-mcrypt \  
php5-gd \  
php5-curl \  
php-pear && \  
rm -rf /var/lib/apt/lists/* && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN /usr/sbin/php5enmod mcrypt  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf && \  
sed -i "s/variables_order.*/variables_order = \"EGPCS\"/g"
/etc/php5/apache2/php.ini  
  
ENV ALLOW_OVERRIDE **True**  
  
# Configure /www folder with sample www  
RUN mkdir -p /www && rm -fr /var/www/html && ln -s /www /var/www/html  
ADD www/ /www  
RUN chown www-data:www-data /www -R  
  
RUN mkdir /var/run/sshd  
RUN mkdir /root/tmp  
ADD authorized_keys /authorized_keys  
ADD sshdconfig.sh /sshdconfig.sh  
RUN chmod 755 /sshdconfig.sh  
RUN bin/bash /sshdconfig.sh && rm /sshdconfig.sh  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH fix for permanent login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
#ADD crontab /etc/crontab  
ADD crontab /var/spool/cron/crontabs/root  
RUN chmod 600 /var/spool/cron/crontabs/root  
  
# Scripts  
ADD ./scripts/start.sh /sbin/start.sh  
ADD ./scripts/sshd.sh /sbin/sshd.sh  
ADD ./scripts/cron.sh /sbin/cron.sh  
ADD ./scripts/run.sh /root/run.sh  
  
# Make them executable  
RUN chmod 755 /sbin/start.sh /sbin/cron.sh /sbin/sshd.sh /root/run.sh  
  
EXPOSE 80  
EXPOSE 22  
WORKDIR /www  
CMD ["/bin/bash", "/sbin/start.sh"]  

