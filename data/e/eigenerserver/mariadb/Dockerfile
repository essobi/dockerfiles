FROM eigenerserver/ubuntu:1.0  
LABEL description="Hedgehog Cloud by www.eigener-server.ch
https://www.eigener-server.ch/en/igel-cloud \  
is licensed under a Creative Commons Attribution 4.0 International Lizenz \  
http://creativecommons.org/licenses/by/4.0/ \  
To remove the links visit https://www.eigener-server.ch/en/igel-cloud"  
  
ENV MARIADB_LOG_BIN_TRUST=0  
ENV MARIADB_USER=eigenerserver  
ENV MARIADB_PASS=eigenerserver  
ENV MARIADB_ROOT_PASS=eigenerserver  
ENV MARIADB_DATABASE=eigenerserver  
ENV MARIADB_VERSION 10.2  
#
https://downloads.mariadb.org/mariadb/repositories/#mirror=netcologne&distro=Ubuntu&distro_release=xenial
--ubuntu_xenial&version=10.2  
RUN apt-get update && \  
export DEBIAN_FRONTEND=noninteractive && \  
apt-get -y --no-install-recommends install software-properties-common && \  
apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xF1656F24C74CD1D8 && \  
add-apt-repository "deb [arch=amd64,i386,ppc64el]
http://mirror.netcologne.de/mariadb/repo/${MARIADB_VERSION}/ubuntu xenial
main" && \  
apt-get update && \  
apt-get -y --no-install-recommends install mariadb-server locales cron
supervisor && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN locale-gen en_US.UTF-8  
  
RUN mkdir -p /var/log/supervisor && \  
mkdir -p /etc/supervisor/conf.d  
  
EXPOSE 3306  
VOLUME ["/host/mariadb"]  
  
COPY crontab.txt /crontab.txt  
RUN /usr/bin/crontab /crontab.txt  
  
COPY supervisord.conf /etc/supervisor/conf.d/mariadb.conf  
  
COPY mysql_backup /usr/local/bin/mysql_backup  
COPY run.sh /usr/local/bin/run.sh  
RUN chmod +x /usr/local/bin/*  
  
ENTRYPOINT ["/bin/bash","/usr/local/bin/run.sh"]  
  
CMD ["/usr/bin/supervisord"]  

