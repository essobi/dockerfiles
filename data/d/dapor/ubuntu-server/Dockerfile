FROM ubuntu:14.04  
MAINTAINER dapor2000  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-
install-recommends \  
apt-utils \  
apt-transport-https \  
ca-certificates \  
net-tools \  
openssh-server \  
python-simplejson \  
zip unzip \  
vim locate software-properties-common \  
apache2 php5 libapache2-mod-php5 imagemagick phpmyadmin \  
nano cronolog php5-curl  
  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get update  
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true" | debconf-set-selections  
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 seen
true" | debconf-set-selections  
RUN apt-get install wget oracle-java8-installer -y  
RUN apt-get install oracle-java8-set-default -y  
  
RUN mkdir /traccar  
RUN cd /traccar && wget
https://github.com/tananaev/traccar/releases/download/v3.5/traccar-
linux-64-3.5.zip  
RUN cd /traccar && unzip traccar-linux-64-3.5.zip  
RUN cd /traccar && chmod +x traccar.run  
RUN cd /traccar && ./traccar.run  
RUN mkdir -p /config/traccar  
RUN cd /traccar && cp /opt/traccar/conf/* /config/traccar/  
  
RUN mkdir /var/run/sshd && mkdir /root/.ssh/ && touch
/root/.ssh/authorized_keys  
  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
# Configure user nobody to match unRAID's settings  
RUN usermod -u 99 nobody  
RUN usermod -g 100 nobody  
RUN usermod -d /home nobody  
RUN chown -R nobody:users /home  
  
COPY ./docker-entrypoint.sh /scripts/docker-entrypoint.sh  
COPY ./run.sh /scripts/run.sh  
RUN chmod a+x /scripts/docker-entrypoint.sh && chmod a+x /scripts/run.sh  
  
RUN echo "export AUTHORIZED_KEYS=" >> /etc/profile  
RUN echo "export ROOT_PASSWORD=" >> /etc/profile  
RUN echo "upload_tmp_dir = /var/www/tmp" >> /etc/php5/apache2/php.ini  
RUN echo "upload_max_filesize = 50M" >> /etc/php5/apache2/php.ini  
RUN echo "max_execution_time = 300" >> /etc/php5/apache2/php.ini  
RUN echo "short_open_tag = On" >> /etc/php5/apache2/php.ini  
  
VOLUME /config/traccar  
VOLUME /var/www  
VOLUME /etc/letsencrypt  
VOLUME /home/hlx  
  
EXPOSE 80 443 82 22  
ENTRYPOINT ["/scripts/docker-entrypoint.sh"]  
  
CMD ["/scripts/run.sh"]  

