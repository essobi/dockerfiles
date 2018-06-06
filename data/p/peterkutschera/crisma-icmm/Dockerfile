# 2014-11-17  
# Peter.Kutschera@ait.ac.at  
# docker build -t peterkutschera/crisma-icmm icmm  
# docker run -d -p 48014:80 [-v /datadir:/icmmdata] --env
ICMM_ENDPOINT=http://localhost:48014/icmm_api --link c_orion:orion
peterkutschera/crisma-icmm  
# e.g.  
# docker run --name c_icmm -d -p 48014:80 -v $(pwd)/data/icmm:/icmmdata --env
ICMM_ENDPOINT=http://localhost:48014/icmm_api --link c_orion:orion
peterkutschera/crisma-icmm  
# Test:  
# docker run -t -i -P peterkutschera/indicator_e /bin/bash  
# apache2ctl start  
# tail -f /var/log/apache2/error.log &  
FROM debian:7.7  
MAINTAINER Peter.Kutschera@ait.ac.at  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# install java8  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee
/etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 &&
\  
apt-get update && apt-get -y install oracle-java8-installer && \  
apt-get install -y python && \  
apt-get clean  
  
# Apache is only needed for the swagger GUI  
RUN apt-get update && apt-get install -y apache2 vim && apt-get clean  
  
COPY etc/apache2/sites-available /etc/apache2/sites-available/  
  
RUN a2enmod proxy_http rewrite  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
EXPOSE 80  
WORKDIR /root  
  
COPY var/www /var/www/  
COPY home /home  
COPY usr/lib/cgi-bin/nextId.py /usr/lib/cgi-bin/  
  
RUN mkdir /icmmdata  
  
VOLUME /icmmdata  
ENV ICMM_ENDPOINT http://localhost/icmm_api  
ENV ORION_HOST orion  
ENV ORION_PORT 1026  
ENv ORION_PATH ""  
COPY root/bin/runAll.sh /root/bin/runAll.sh  
RUN chmod +x /root/bin/*  
  
CMD ["/root/bin/runAll.sh"]  
  

